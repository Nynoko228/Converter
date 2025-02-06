from Convert import Converter

converter = Converter()

# Конвертация расстояния
try:
  meters = 100
  kilometers = converter.convert(meters, "meter", "kilometer")
  print(f"{meters} метров = {kilometers} километров")
except ValueError as e:
    print(f"Ошибка конвертации: {e}")

# Конвертация температуры
try:
  celsius = 25
  fahrenheit = converter.convert(celsius, "celsius", "fahrenheit")
  print(f"{celsius} градусов Цельсия = {fahrenheit} градусов Фаренгейта")
except ValueError as e:
    print(f"Ошибка конвертации: {e}")


# Конвертация скорости
try:
  speed_kmh = 100
  speed_ms = converter.convert(speed_kmh, "kilometer/hour", "meter/second")
  print(f"{speed_kmh} км/ч = {speed_ms} м/с")
except ValueError as e:
    print(f"Ошибка конвертации: {e}")

# Получение списка доступных единиц для "Расстояние"
print(f"Доступные единицы для 'Расстояние': {converter.list_units('Расстояние')}")

# Получение списка доступных категорий и единиц
print("Доступные категории и единицы:")
all_units = converter.list_units()
for category, units in all_units.items():
    print(f"{category}: {units}")


# Проверка корректности единицы измерения
print(f"Является ли 'kilometer' корректной единицей измерения? {converter.is_valid_unit('kilometer')}")
print(f"Является ли 'xyz' корректной единицей измерения? {converter.is_valid_unit('xyz')}")