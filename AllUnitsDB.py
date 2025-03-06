# Логин postgres
# Пароль admin
import psycopg2


class AllUnits:
    pressure_units = {}
    speed_units = {}
    concentration_units = {}
    density_units = {}
    distance_units = {}
    energy_units = {}
    flow_units = {}
    force_units = {}
    light_units = {}
    mass_units = {}
    power_units = {}
    time_units = {}
    torque_units = {}
    volume_units = {}
    dry_volume_units = {}
    acceleration_units = {}
    amount_units = {}
    angle_units = {}
    area_units = {}
    computer_units = {}
    temperature_units = {}
    custom_units = {}


# Функция для загрузки данных из таблицы в словарь
def load_data_from_table(table_name, cur):
    cur.execute(f"SELECT key, value FROM public.{table_name}")
    rows = cur.fetchall()
    return {key: value for key, value in rows}  # Создаем словарь из строк


def main():
    # Параметры подключения
    conn_params = {
        'dbname': 'Converter_units',
        'user': 'postgres',
        'password': 'admin',
        'host': 'localhost',
        'port': 5432,
        'client_encoding': 'utf8'
    }

    try:
        # Подключение к базе данных
        conn = psycopg2.connect(**conn_params)
        print("Connected to the database.")
        cur = conn.cursor()

        # Создаем экземпляр класса AllUnits
        all_units = AllUnits()

        # Загружаем данные из таблиц в словари
        for attr_name in vars(AllUnits):  # Перебираем атрибуты класса
            if isinstance(getattr(AllUnits, attr_name), dict):  # Проверяем, что атрибут - словарь
                table_name = attr_name.replace(" ", "_")  # Заменяем пробелы на подчеркивания
                print(f"Loading data from table '{table_name}' into attribute '{attr_name}'")
                loaded_dict = load_data_from_table(table_name, cur)  # Загружаем данные из таблицы
                setattr(all_units, attr_name, loaded_dict)  # Сохраняем словарь в атрибут

        # Выводим загруженные данные для проверки
        print("\nLoaded data:")
        cnt = 0
        for attr_name, units_dict in vars(all_units).items():
            if isinstance(units_dict, dict):
                print(f"{attr_name}: {units_dict}")
                cnt += 1
        print(cnt)
        # print(all_units.temperature_units["Celsius"][0])
        # Преобразуем строки в лямбда-функции
        # all_units.temperature_units = {
        #     key: [eval(value[0]), eval(value[1])] for key, value in all_units.temperature_units.items()
        # }


        # Преобразуем строки в лямбда-функции
        # for unit, formulas in all_units.temperature_units.items():
        #     # print(formulas)
        #     all_units.temperature_units[unit] = [eval(formula.replace('x =>', 'lambda x:')) for formula in formulas]

        # all_units.temperature_units.update(temperature_units)

        # print(all_units.temperature_units)

        # print(all_units.temperature_units["Celsius"])
        all_units.temperature_units.update(
            Celsius=[lambda x: x, lambda x: x],
            Fahrenheit=[lambda x: (x - 32) * 5 / 9, lambda x: (x * 9 / 5) + 32],
            Kelvin=[lambda x: x - 273.15, lambda x: x + 273.15],
            Rankine=[lambda x: (x - 491.67) * 5 / 9, lambda x: (x + 273.15) * 9 / 5])
        # print(all_units.temperature_units)

    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Закрытие курсора и соединения
        if cur:
            cur.close()
        if conn:
            conn.close()
        print("Connection closed.")
        return all_units


if __name__ == "__main__":
    main()
