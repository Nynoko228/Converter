# Это не совсем старый конвертер. Тут посто сокращённые названия единиц, которые отличны от названий в программе
import math

from openpyxl.styles import NamedStyle, Font, Alignment, PatternFill, Border, Side
from AllUnits import AllUnits

# Density
def density_converter(value, from_unit, to_unit):
    """Конвертер плотности."""
    units = {
        "kg/m3": 1,
        "g/cm3": 1000,
        "lb/ft3": 16.0185,
        "lb/in3": 27679.9,
    }
    value_in_kgm3 = value * units[from_unit]
    return value_in_kgm3 / units[to_unit]

# Distance
def distance_converter(value, from_unit, to_unit):
    """Конвертер расстояния."""
    units = {
        "m": 1,
        "km": 1000,
        "cm": 0.01,
        "mm": 0.001,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mile": 1609.34,
        "nautical_mile": 1852
    }
    value_in_meters = value * units[from_unit]
    return value_in_meters / units[to_unit]


# Energy
def energy_converter(value, from_unit, to_unit):
    """Конвертер энергии."""
    units = {
        "J": 1,
        "kJ": 1000,
        "cal": 4.184,
        "kcal": 4184,
        "Wh": 3600,
        "kWh": 3600000,
        "BTU": 1055.06,
    }
    value_in_joules = value * units[from_unit]
    return value_in_joules / units[to_unit]

# Flow (Volume Flow Rate)
def flow_converter(value, from_unit, to_unit):
    """Конвертер объемного расхода."""
    units = {
        "m3/s": 1,
        "m3/h": 1/3600,
        "L/s": 0.001,
        "L/min": 0.001/60,
        "L/h": 0.001/3600,
        "gal/min": 0.00006309, # US Gallons
        "gal/h": 0.00006309/60
    }
    value_in_m3s = value * units[from_unit]
    return value_in_m3s / units[to_unit]

# Force
def force_converter(value, from_unit, to_unit):
    """Конвертер силы."""
    units = {
        "N": 1,
        "kN": 1000,
        "lbf": 4.44822,
        "kgf": 9.80665,
    }
    value_in_newtons = value * units[from_unit]
    return value_in_newtons / units[to_unit]

# Light (Illuminance)
def illuminance_converter(value, from_unit, to_unit):
    """Конвертер освещенности."""
    units = {
        "lux": 1,
        "footcandle": 10.7639,
    }
    value_in_lux = value * units[from_unit]
    return value_in_lux / units[to_unit]


# Mass
def mass_converter(value, from_unit, to_unit):
    """Конвертер массы."""
    units = {
        "kg": 1,
        "g": 0.001,
        "mg": 0.000001,
        "lb": 0.453592,
        "oz": 0.0283495,
        "ton": 1000,  # Metric ton
    }
    value_in_kg = value * units[from_unit]
    return value_in_kg / units[to_unit]

# Power
def power_converter(value, from_unit, to_unit):
    """Конвертер мощности."""
    units = {
        "W": 1,
        "kW": 1000,
        "MW": 1000000,
        "hp": 745.7, # mechanical horsepower
    }
    value_in_watts = value * units[from_unit]
    return value_in_watts / units[to_unit]

# Pressure
def pressure_converter(value, from_unit, to_unit):
    """Конвертер давления (расширенный)."""
    units = AllUnits.pressure_units
    value_in_pascals = value * units[from_unit]
    return value_in_pascals / units[to_unit]

def speed_converter(value, from_unit, to_unit):
    """Конвертер скорости (расширенный)."""
    units = AllUnits.speed_units
    value_in_ms = value * units[from_unit]
    return value_in_ms / units[to_unit]

# Temperature
def temperature_converter(value, from_unit, to_unit):
    """Конвертер температуры."""
    if from_unit == to_unit:
        return value

    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5/9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        raise ValueError("Неизвестная исходная единица измерения температуры.")

    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return (celsius * 9/5) + 32
    elif to_unit == "K":
        return celsius + 273.15
    else:
        raise ValueError("Неизвестная конечная единица измерения температуры.")


# Time
def time_converter(value, from_unit, to_unit):
    """Конвертер времени."""
    units = {
        "s": 1,
        "min": 60,
        "h": 3600,
        "day": 86400,
        "week": 604800,
        "month": 2592000,  # Approximate (30 days)
        "year": 31536000, # Approximate (365 days)
    }
    value_in_seconds = value * units[from_unit]
    return value_in_seconds / units[to_unit]

# Torque
def torque_converter(value, from_unit, to_unit):
    """Конвертер крутящего момента."""
    units = {
        "N.m": 1,
        "kN.m": 1000,
        "lbf.ft": 1.35582,
        "lbf.in": 0.112985,
    }
    value_in_Nm = value * units[from_unit]
    return value_in_Nm / units[to_unit]

# Volume
def volume_converter(value, from_unit, to_unit):
    """Конвертер объема."""
    units = {
        "m3": 1,
        "L": 0.001,
        "mL": 0.000001,
        "gal": 0.00378541,  # US Gallon
        "ft3": 0.0283168,
        "in3": 0.0000163871,
    }
    value_in_m3 = value * units[from_unit]
    return value_in_m3 / units[to_unit]

# Volume - Dry (US)
def dry_volume_converter(value, from_unit, to_unit):
    """Конвертер сухого объема (US)."""
    units = {
        "bushel": 0.0352391,  # US bushel
        "quart": 0.00110122, # US dry quart
        "pint": 0.00055061,  # US dry pint
    }
    value_in_bushels = value * units[from_unit]
    return value_in_bushels / units[to_unit]

# Acceleration
def acceleration_converter(value, from_unit, to_unit):
    """Конвертер ускорения."""
    units = {
        "m/s2": 1,
        "cm/s2": 0.01,
        "ft/s2": 0.3048,
        "g": 9.80665, # Standard gravity
    }
    value_in_ms2 = value * units[from_unit]
    return value_in_ms2 / units[to_unit]

# Amt. of Substance (Amount of Substance)
def amount_converter(value, from_unit, to_unit):
    """Конвертер количества вещества."""
    units = {
        "mol": 1,
        "kmol": 1000,
        "millimol": 0.001,
    }
    value_in_mol = value * units[from_unit]
    return value_in_mol / units[to_unit]

# Angle
def angle_converter(value, from_unit, to_unit):
  """Конвертер углов."""
  units = {
      "rad": 1,
      "deg": math.pi / 180,
      "grad": math.pi / 200, # Gradian or gon
  }
  value_in_radians = value * units[from_unit]
  return value_in_radians / units[to_unit]

# Area
def area_converter(value, from_unit, to_unit):
    """Конвертер площади."""
    units = {
        "m2": 1,
        "km2": 1000000,
        "cm2": 0.0001,
        "mm2": 0.000001,
        "ft2": 0.092903,
        "in2": 0.00064516,
        "ha": 10000, # Hectare
        "acre": 4046.86
    }
    value_in_m2 = value * units[from_unit]
    return value_in_m2 / units[to_unit]

# Computer (Data Storage)
def data_converter(value, from_unit, to_unit):
    """Конвертер объема данных."""
    units = {
        "bit": 1/8, # 1 byte = 8 bits
        "byte": 1,
        "kB": 1024,
        "MB": 1024**2,
        "GB": 1024**3,
        "TB": 1024**4,
    }
    value_in_bytes = value * units[from_unit]
    return value_in_bytes / units[to_unit]

# Concentration (Mass Concentration)
def concentration_converter(value, from_unit, to_unit):
  """Конвертер концентрации (массовой)."""
  units = {
      "kg/m3": 1,
      "g/L": 1, # Grams per liter is the same as kg per m3
      "mg/L": 0.001,
      "ppm": 0.001, # Parts per million (assuming density of water)
      "ppb": 0.000001, # Parts per billion (assuming density of water)
  }
  value_in_kgm3 = value * units[from_unit]
  return value_in_kgm3 / units[to_unit]

def test_converter(units, type, function):
    """Тестирует pressure_converter, преобразуя во все единицы измерения."""

    value = float(input("Введите значение: "))
    from_unit = input("Введите исходную единицу измерения: ")

    if from_unit not in units:  # Проверяем, есть ли такая единица
        print("Ошибка: Недопустимая исходная единица измерения.")
        return

    # 1. Сортировка ключей в список:

    sorted_units_keys = sorted(units.keys(), key=lambda s: s.lower())
    print("Отсортированные ключи:", sorted_units_keys)

    # 2. Сортировка и итерация по отсортированным ключам:

    print("\nИтерация по отсортированным ключам:")
    for key in sorted_units_keys:
        print(f"{key}: {units[key]}")

    # 3. Получение отсортированного словаря (если требуется):
    #    (Обратите внимание, что это создаст *новый* отсортированный словарь.
    #     Исходный словарь units не изменится.)

    import collections

    sorted_units = collections.OrderedDict((key, units[key]) for key in sorted_units_keys)
    excel_creater(value, from_unit, sorted_units, type, function)




def excel_creater(value, from_unit, to_units, type, conversion_function_name):
    from openpyxl import Workbook

    """
    Создаёт Excel-файл с результатами конвертации.

    :param value: Значение для конвертации.
    :param from_unit: Начальная единица измерения.
    :param to_units: Список единиц измерения, в которые нужно конвертировать.
    """
    # Создаём новую книгу Excel и выбираем активный лист
    wb = Workbook()
    ws = wb.active

    # Заголовки таблицы
    ws.append(["Значение", "Начальная величина", "Значение", "Сконвертированная величина"])

    # Получаем функцию конвертации по её имени
    try:
        conversion_function = globals()[conversion_function_name]
    except KeyError:
        print(f"Ошибка: Функция конвертации '{conversion_function_name}' не найдена.")
        return  # Завершаем функцию, если функция не найдена

    # Конвертируем значение в каждую из указанных единиц измерения
    for to_unit in to_units:
        try:
            converted_value = conversion_function(value, from_unit, to_unit)
            ws.append([value, from_unit, converted_value, to_unit])
            print(f"{value} {from_unit} = {converted_value} {to_unit}")
        except Exception as e:
            print(f"Ошибка при конвертации {from_unit} в {to_unit}: {e}")

    # Настраиваем стили для красивого вида
    header_style = NamedStyle(name='header')
    header_style.font = Font(bold=True, color='FFFFFF')
    header_style.alignment = Alignment(horizontal='center', vertical='center')
    header_style.fill = PatternFill(start_color='4F81BD', end_color='4F81BD', fill_type='solid')
    border_style = Border(
        left=Side(border_style='thin', color='000000'),
        right=Side(border_style='thin', color='000000'),
        top=Side(border_style='thin', color='000000'),
        bottom=Side(border_style='thin', color='000000')
    )
    header_style.border = border_style

    cell_style = NamedStyle(name='cell')
    cell_style.alignment = Alignment(horizontal='left', vertical='center')
    cell_style.border = border_style

    for cell in ws[1]:  # Применяем стиль к заголовкам
        cell.style = header_style

    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
        for cell in row:
            cell.style = cell_style

    # Автоматическое изменение ширины столбцов
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2)
        ws.column_dimensions[column].width = adjusted_width

    # Сохраняем файл
    filename = f"conversion_results_{type}.xlsx"
    wb.save(filename)
    print(f"Файл '{filename}' успешно создан.")


# # Пример использования
# value = 1  # Значение для конвертации
# from_unit = "atm"  # Начальная единица измерения
# to_units = ["Pa", "kPa", "MPa", "bar", "mmHg", "PSI"]  # Список единиц для конвертации
#
# excel_creater(value, from_unit, to_units)

if __name__ == "__main__":
    # Устанавливаем defaults для корректной работы
    # pressure_converter.__defaults__ = (list(pressure_converter.__code__.co_consts[1].keys()),)
    unit = AllUnits.speed_units
    test_converter(unit, "speed", "speed_converter")
