document.addEventListener('DOMContentLoaded', () => {
    const categorySelect = document.getElementById('category');
    const fromUnitSelect = document.getElementById('fromUnit');
    const toUnitSelect = document.getElementById('toUnit');
    const inputValue = document.getElementById('inputValue');
    const resultDiv = document.getElementById('result');
    const addButton = document.getElementById('addButton');

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
            console.log(typeof category);

            if (category === 'custom') {
                document.getElementById('addButton').style.display = 'block'; // Показываем кнопку
            } else {
                document.getElementById('addButton').style.display = 'none'; // Скрываем кнопку
            }
            // Получаем новые единицы измерения
            const response = await fetch(`/api/units/${category}`);
            if (!response.ok) throw new Error('Ошибка загрузки единиц');

            const units = await response.json();
            if (units.length === 0) throw new Error('Нет доступных единиц');

            resultDiv.textContent = "Результат появится здесь...";
            resultDiv.classList.remove('alert-danger');
            resultDiv.classList.add('alert-primary');



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
            resultDiv.classList.remove('alert-primary');
            resultDiv.classList.add('alert-danger');
            fromUnitSelect.innerHTML = '';
            toUnitSelect.innerHTML = '';
        }
    });

    addButton.addEventListener('click', async () => {
        // Запрашиваем у пользователя название новой единицы
        const newUnitName = prompt('Введите название новой единицы измерения:');
        if (!newUnitName) return; // Если пользователь нажал "Отмена", выходим

        // Запрашиваем значение новой единицы относительно базовой
        const newUnitValue = parseFloat(prompt('Введите значение новой единицы относительно базовой (например, 1000, если 1 новая единица = 1000 базовых):'));
        if (isNaN(newUnitValue)) {
            alert('Некорректное значение!');
            return;
        }

        // Запрашиваем название базовой единицы
        const baseUnitName = prompt('Введите название базовой единицы (например, "метр"):');
        if (!baseUnitName) return; // Если пользователь нажал "Отмена", выходим

        try {
            // Отправляем данные на сервер для добавления новой единицы
            const response = await fetch('/api/add_custom_unit', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    category: 'custom',
                    new_unit_name: newUnitName,
                    new_unit_value: newUnitValue,
                    base_unit_name: baseUnitName
                })
            });

            if (!response.ok) throw new Error('Ошибка при добавлении единицы');

            const result = await response.json();
            alert(result.message); // Показываем сообщение об успешном добавлении

            // Обновляем список единиц для категории "custom"
            const unitsResponse = await fetch('/api/units/custom');
            const units = await unitsResponse.json();

            // Очищаем и заполняем выпадающие списки
            fromUnitSelect.innerHTML = units.map(u => `<option value="${u}">${u}</option>`).join('');
            toUnitSelect.innerHTML = units.map(u => `<option value="${u}">${u}</option>`).join('');

            // Выбираем первую единицу по умолчанию
            fromUnitSelect.value = units[0];
            toUnitSelect.value = units.length > 1 ? units[1] : units[0];

            fromUnitSelect.disabled = false;
            toUnitSelect.disabled = false;
            resultDiv.textContent = "Результат появится здесь...";
            resultDiv.classList.remove('alert-danger');
            resultDiv.classList.add('alert-primary');

        } catch (error) {
            alert(error.message); // Показываем сообщение об ошибке
        }
    });

    // Автоматическая конвертация при изменении параметров
    [categorySelect, fromUnitSelect, toUnitSelect, inputValue].forEach(element => {
//        element.addEventListener('change', updateResult);
        element.addEventListener('input', updateResult);
    });

// Функция для удаления лишних нулей
function formatResult(value) {
    let roundedValue = value.toFixed(8);
    return parseFloat(roundedValue).toString();
}

async function updateResult() {
    if (!categorySelect.value || !fromUnitSelect.value || !toUnitSelect.value || !inputValue.value) return;

    try {
        const fromUnitText = fromUnitSelect.options[fromUnitSelect.selectedIndex].text;
        const toUnitText = toUnitSelect.options[toUnitSelect.selectedIndex].text;

        console.log("Sending data:", {
        category: categorySelect.value,
        from_unit: fromUnitText,
        to_unit: toUnitText,
        value: inputValue.value
        });
        const response = await fetch('/api/convert', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                category: categorySelect.value,
                from_unit: fromUnitText,
                to_unit: toUnitText,
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

        resultDiv.textContent = `${inputValue.value} ${fromUnitText} = ${formatResult(data.result)} ${toUnitText}`;
        resultDiv.classList.remove('alert-danger');
        resultDiv.classList.add('alert-success');

    } catch (error) {
        resultDiv.textContent = error.message;
        resultDiv.classList.remove('alert-success');
        resultDiv.classList.add('alert-danger');
    }
    }
});