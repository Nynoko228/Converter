from flask import Flask, jsonify, request, render_template
from AllUnitsDB import main  # Импортируем вашу функцию main()
import converters
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
    'temperature': lambda v, f, t: converters.temperature_converter(v, f, t),
    'time': lambda v, f, t: converters.time_converter(v, f, t, AllUnits.time_units),
    'torque': lambda v, f, t: converters.torque_converter(v, f, t, AllUnits.torque_units),
    'volume': lambda v, f, t: converters.volume_converter(v, f, t, AllUnits.volume_units),
    'dry_volume': lambda v, f, t: converters.dry_volume_converter(v, f, t, AllUnits.dry_volume_units),
    'acceleration': lambda v, f, t: converters.acceleration_converter(v, f, t, AllUnits.acceleration_units),
    'amount': lambda v, f, t: converters.amount_converter(v, f, t, AllUnits.amount_unit),
    'angle': lambda v, f, t: converters.angle_converter(v, f, t, AllUnits.angle_unit),
    'area': lambda v, f, t: converters.area_converter(v, f, t, AllUnits.area_unit),
    'data': lambda v, f, t: converters.data_converter(v, f, t, AllUnits.comuter_unit),
    'concentration': lambda v, f, t: converters.concentration_converter(v, f, t, AllUnits.concentration_units),
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/categories')
def get_categories():
    # Получаем все категории из класса AllUnits
    categories = [key.replace('_units', '') for key in AllUnits.__dict__
                  if key.endswith('_units') and getattr(AllUnits, key)]
    return jsonify(categories)


@app.route('/api/units/<category>')
def get_units(category):
    # Получаем единицы измерения для категории
    units = getattr(AllUnits, f"{category}_units", None)
    print(f"UNITS: {units}")
    return jsonify(list(units.keys()) if units else [])


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