import psycopg2

try:
    # Подключение к базе данных
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='root',
        host='localhost',
        port='5432'
    )
    print('Connection established')
except Exception as e:
    print(f'Error connecting to the database: {e}')
    exit()  # Завершить программу, если соединение не удалось

# Создаем курсор для выполнения запросов
cursor = conn.cursor()

try:
    # Создание таблицы customers
    cursor.execute('''
        CREATE TABLE customers (
            id SERIAL PRIMARY KEY,     -- Автоинкрементирующий идентификатор
            name VARCHAR(100),         -- Имя клиента (максимум 100 символов)
            email VARCHAR(100) UNIQUE, -- Уникальный email
            phone VARCHAR(15)          -- Телефон (максимум 15 символов)
        );
    ''')
    conn.commit()  # Применяем изменения
    print("Table 'customers' created successfully.")
except Exception as e:
    print(f"Error creating table: {e}")
    conn.rollback()  # Откатываем изменения в случае ошибки

# Закрываем соединение
cursor.close()
conn.close()