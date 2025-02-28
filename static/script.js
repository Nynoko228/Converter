document.addEventListener('DOMContentLoaded', () => {
    const categorySelect = document.getElementById('category');
    const fromUnitSelect = document.getElementById('fromUnit');
    const toUnitSelect = document.getElementById('toUnit');
    const inputValue = document.getElementById('inputValue');
    const resultDiv = document.getElementById('result');

    // Загрузка категорий
    fetch('/api/categories')
        .then(r => r.json())
        .then(categories => {
            categories.forEach(cat => {
                const option = document.createElement('option');
                option.value = cat;
                option.textContent = cat.charAt(0).toUpperCase() + cat.slice(1);
                categorySelect.appendChild(option);
            });
        });

    // Переписанный обработчик изменения категории
    categorySelect.addEventListener('change', async () => {
        const category = categorySelect.value;
        fromUnitSelect.disabled = true;
        toUnitSelect.disabled = true;

        try {
            // Получаем новые единицы измерения
            const response = await fetch(`/api/units/${category}`);
            if (!response.ok) throw new Error('Ошибка загрузки единиц');

            const units = await response.json();
            if (units.length === 0) throw new Error('Нет доступных единиц');

            // Полностью пересоздаем опции
            fromUnitSelect.innerHTML = units.map(u => `<option value="${u}">${u}</option>`).join('');
            toUnitSelect.innerHTML = units.map(u => `<option value="${u}">${u}</option>`).join('');

            // Выбираем разумные значения по умолчанию
            fromUnitSelect.value = units[0];
            toUnitSelect.value = units.length > 1 ? units[1] : units[0];

            fromUnitSelect.disabled = false;
            toUnitSelect.disabled = false;

            // Принудительно запускаем конвертацию с новыми значениями
            updateResult();

        } catch (error) {
            resultDiv.textContent = error.message;
            resultDiv.classList.add('alert-danger');
            fromUnitSelect.innerHTML = '';
            toUnitSelect.innerHTML = '';
        }
    });

    // Автоматическая конвертация при изменении параметров
    [categorySelect, fromUnitSelect, toUnitSelect, inputValue].forEach(element => {
        element.addEventListener('change', updateResult);
        element.addEventListener('input', updateResult);
    });

async function updateResult() {
    if (!categorySelect.value || !fromUnitSelect.value || !toUnitSelect.value || !inputValue.value) return;

    try {
        const response = await fetch('/api/convert', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                category: categorySelect.value,
                from_unit: fromUnitSelect.value,
                to_unit: toUnitSelect.value,
                value: inputValue.value
            })
        });

        if (!response.ok) {
            throw new Error('Ошибка сервера');
        }

        const data = await response.json();

        if (data.error) {
            throw new Error(data.error);
        }

        resultDiv.textContent = `${inputValue.value} ${fromUnitSelect.value} = ${data.result.toFixed(4)} ${toUnitSelect.value}`;
        resultDiv.classList.remove('alert-danger');
        resultDiv.classList.add('alert-success');

    } catch (error) {
        resultDiv.textContent = error.message;
        resultDiv.classList.remove('alert-success');
        resultDiv.classList.add('alert-danger');
    }
    }
});