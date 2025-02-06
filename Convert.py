import pint


class Converter:
    def __init__(self):
        self.ureg = pint.UnitRegistry()

        # Определим группы для удобства:
        self.categories = {
            "Давление": ["pascal", "bar", "psi", "atmosphere"],
            "Скорость": ["meter/second", "kilometer/hour", "mile/hour", "knot"],
            "Ускорение": ["meter/second**2", "g"],
            "Плотность": ["kilogram/meter**3", "gram/centimeter**3"],
            "Температура": ["kelvin", "celsius", "fahrenheit"],
            "Количество вещества": ["mol"],
            "Расстояние": ["meter", "kilometer", "mile", "foot", "inch"],
            "Время": ["second", "minute", "hour", "day"],
            "Угол": ["radian", "degree"],
            "Энергия": ["joule", "kilojoule", "calorie", "kilowatt_hour"],
            "Крутящий момент": ["newton*meter", "pound*foot"],
            "Область": ["meter**2", "centimeter**2", "kilometer**2", "acre"],
            "Поток": ["liter/second", "cubic_meter/second"],
            "Объем": ["liter", "cubic_meter", "gallon"],
            "Компьютер": ["bit", "byte", "kilobyte", "megabyte", "gigabyte"],
            "Сила": ["newton", "pound-force"],
            "Свет": ["lumen", "lux"],
            "Объем - Сухой": ["bushel", "pint"],
            "Концентрация": ["mol/liter", "milligram/liter"],
            "Масса": ["kilogram", "gram", "pound", "ounce"],
            "Мощность": ["watt", "kilowatt", "horsepower"]
        }

    def convert(self, value, from_unit, to_unit):
        """
        Конвертирует значение из одной единицы измерения в другую.

        Args:
            value (float): Значение для конвертации.
            from_unit (str): Исходная единица измерения (например, "meter").
            to_unit (str): Целевая единица измерения (например, "kilometer").

        Returns:
            float: Конвертированное значение.

        Raises:
            pint.errors.UndefinedUnitError: Если указана некорректная единица измерения.
            pint.errors.DimensionalityError: Если единицы несовместимы.
        """

        try:
            quantity = self.ureg.Quantity(value, from_unit)
            converted = quantity.to(to_unit)
            return converted.magnitude
        except pint.errors.UndefinedUnitError as e:
            raise ValueError(f"Неизвестная единица измерения: {e}")
        except pint.errors.DimensionalityError as e:
            raise ValueError(f"Несовместимые единицы измерения: {e}")

    def list_units(self, category=None):
        """
        Выводит список доступных единиц измерения для выбранной категории, или всех если категория не выбрана.

        Args:
            category (str, optional): Категория единиц измерения (например, "Расстояние").
                                      Если None, то будут возвращены все категории.

        Returns:
            dict или list: Если указана категория - список единиц измерения в категории.
                           Иначе - словарь, где ключи - категории, а значения - списки единиц измерения.
        """
        if category:
            if category in self.categories:
                return self.categories[category]
            else:
                raise ValueError(f"Неизвестная категория: {category}")

        return self.categories

    def is_valid_unit(self, unit):
        """
        Проверяет, является ли данная единица измерения корректной.

        Args:
          unit (str): Строка, представляющая единицу измерения (например, "meter").

        Returns:
          bool: True, если единица измерения корректна, False в противном случае.
        """
        try:
            self.ureg.parse_units(unit)
            return True
        except pint.errors.UndefinedUnitError:
            return False