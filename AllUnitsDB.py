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
        amount_unit = {}
        angle_unit = {}
        area_unit = {}
        comuter_unit = {}

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
        'port': 5432
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