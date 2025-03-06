import psycopg2

from AllUnits import AllUnits


# Функция для создания таблиц
def create_tables(table_name):
    if table_name == "temperature_units":
        cur.execute(f"""
        CREATE TABLE IF NOT EXISTS public.{table_name} (
            id SERIAL PRIMARY KEY,
            key TEXT NOT NULL,
            value JSONB NOT NULL
        )
    """)
    else:
        cur.execute(f"""
            CREATE TABLE IF NOT EXISTS public.{table_name} (
                id SERIAL PRIMARY KEY,
                key TEXT NOT NULL,
                value FLOAT NOT NULL
            )
        """)
    conn.commit()
    print(f"Table '{table_name}' created successfully.")

# Функция для вставки данных
def insert_data(units_dict, table_name):
    for key, value in units_dict.items():
        cur.execute(f"""
            INSERT INTO public.{table_name} (key, value)
            VALUES (%s, %s)
        """, (key, value))
    conn.commit()
    print(f"Data inserted into table '{table_name}'.")

if __name__ == "__main__":
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

        all_units = AllUnits()
        for attr_name, units_dict in vars(AllUnits).items():  # Используем vars(AllUnits)
            if isinstance(units_dict, dict):
                print(f"Processing attribute: {attr_name}")
                table_name = attr_name.replace(" ", "_")  # Заменяем пробелы на подчеркивания
                create_tables(table_name)
                insert_data(units_dict, table_name)

        # Проверка наличия таблиц
        cur.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """)
        tables = cur.fetchall()
        print("Tables in the database:")
        for table in tables:
            print(table[0])

    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Закрытие курсора и соединения
        if cur:
            cur.close()
        if conn:
            conn.close()
        print("Connection closed.")