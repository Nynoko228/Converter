from flask import Flask, jsonify, request, render_template
from AllUnitsDB import main  # Импортируем вашу функцию main()
import converters
from urllib.parse import unquote
app = Flask(__name__)

# Инициализация единиц измерения
AllUnits = main()

# Словарь для связи категорий с функциями конвертации
CONVERTERS = {
    'density': lambda v, f, t: converters.density_converter(v, f, t, AllUnits.density_units),
    'distance': lambda v, f, t: converters.distance_converter(v, f, t, AllUnits.distance_units),
    'energy': lambda v, f, t: converters.energy_converter(v, f, t, AllUnits.energy_units),
    'flow': lambda v, f, t: converters.flow_converter(v, f, t, AllUnits.flow_units),
    'force': lambda v, f, t: converters.force_converter(v, f, t, AllUnits.force_units),
    'illuminance': lambda v, f, t: converters.illuminance_converter(v, f, t, AllUnits.light_units),
    'mass': lambda v, f, t: converters.mass_converter(v, f, t, AllUnits.mass_units),
    'power': lambda v, f, t: converters.power_converter(v, f, t, AllUnits.power_units),
    'pressure': lambda v, f, t: converters.pressure_converter(v, f, t, AllUnits.pressure_units),
    'speed': lambda v, f, t: converters.speed_converter(v, f, t, AllUnits.speed_units),
    'temperature': lambda v, f, t: converters.temperature_converter(v, f, t, AllUnits.temperature_units),
    'time': lambda v, f, t: converters.time_converter(v, f, t, AllUnits.time_units),
    'torque': lambda v, f, t: converters.torque_converter(v, f, t, AllUnits.torque_units),
    'volume': lambda v, f, t: converters.volume_converter(v, f, t, AllUnits.volume_units),
    'dry_volume': lambda v, f, t: converters.dry_volume_converter(v, f, t, AllUnits.dry_volume_units),
    'acceleration': lambda v, f, t: converters.acceleration_converter(v, f, t, AllUnits.acceleration_units),
    'amount': lambda v, f, t: converters.amount_converter(v, f, t, AllUnits.amount_units),
    'angle': lambda v, f, t: converters.angle_converter(v, f, t, AllUnits.angle_units),
    'area': lambda v, f, t: converters.area_converter(v, f, t, AllUnits.area_units),
    'computer': lambda v, f, t: converters.data_converter(v, f, t, AllUnits.computer_units),
    'concentration': lambda v, f, t: converters.concentration_converter(v, f, t, AllUnits.concentration_units),
    'custom': lambda v, f, t: converters.custom_converter(v, f, t, AllUnits.custom_units)
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/categories')
def get_categories():
    # Получаем все категории из класса AllUnits если они не пустые
    # categories = sorted([key.replace('_units', '').replace('_unit', '') for key in AllUnits.__dict__
    #               if (key.endswith('_units') or key.endswith('_unit')) and getattr(AllUnits, key)])
    categories = sorted([key.replace('_units', '').replace('_unit', '') for key in AllUnits.__dict__
                  if (key.endswith('_units') or key.endswith('_unit'))])
    return jsonify(categories)


@app.route('/api/units/<category>')
def get_units(category):
    # Получаем единицы измерения для категории
    units = getattr(AllUnits, f"{category}_units", getattr(AllUnits, f"{category}_unit", None))
    # print(f"UNITS: {units}")
    return jsonify(list(units.keys()) if units else [])


@app.route('/api/units/custom')
def get_custom_units():
    try:
        # Получаем custom_units из AllUnits
        custom_units = getattr(AllUnits, 'custom_units', {})

        # Возвращаем список всех единиц
        return jsonify(sorted(list(custom_units.keys())))

    except Exception as e:
        return jsonify({'error': str(e)}), 400
@app.route('/api/add_custom_unit', methods=['POST'])
def add_custom_unit():
    data = request.get_json()
    try:
        category = data['category']
        new_unit_name = data['new_unit_name']
        new_unit_value = float(data['new_unit_value'])
        base_unit_name = data['base_unit_name']

        # Проверяем, существует ли категория custom_units
        if not hasattr(AllUnits, 'custom_units'):
            AllUnits.custom_units = {}

        # Добавляем базовую единицу, если её ещё нет
        if base_unit_name not in AllUnits.custom_units:
            AllUnits.custom_units[base_unit_name] = {
                'base_unit': base_unit_name,  # Базовая единица ссылается на саму себя
                'value': 1.0  # Значение базовой единицы всегда 1.0
            }

        # Добавляем новую единицу в custom_units
        AllUnits.custom_units[new_unit_name] = {
            'base_unit': base_unit_name,
            'value': new_unit_value
        }


        print(AllUnits.custom_units)
        return jsonify({'message': f'Единица "{new_unit_name}" успешно добавлена!'})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/convert', methods=['POST'])
def convert():
    data = request.json
    try:
        print(data)
        category = data['category']
        from_unit = data['from_unit']
        to_unit = data['to_unit']
        value = float(data['value'])

        print(f"category: {category}, from_unit: {from_unit}, to_unit: {to_unit}, value: {value}")
        # Получаем нужную функцию конвертации
        converter = CONVERTERS.get(category)
        print(f"CONVERTER: {converter(value, from_unit, to_unit)}")
        if not converter:
            print("ERROR CONVERTER")
            return jsonify({'error': 'Invalid category'}), 400

        result = converter(value, from_unit, to_unit)
        print(f"RESULT: {result}")
        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)