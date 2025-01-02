import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="root",
        host="localhost",
        port="5432",
    )
    print("Соединение установлено")
except Exception as e:
    print(f"Error connecting to the database: {e}")
    exit()

cursor = conn.cursor()

try:
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS public.users
        (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INTEGER
        );
        """
    )
    conn.commit()
    print("Таблица 'users' успешно создана.")
except Exception as e:
    print(f"Error creating table: {e}")
    conn.rollback()


def create_user(name, age):
    try:
        cursor.execute(
            """
            INSERT INTO public.users (name, age)
            VALUES (%s, %s)
            RETURNING id;
            """,
            (name, age),
        )
        user_id = cursor.fetchone()[0]
        conn.commit()
        print(f"Пользователь {name} успешно добавлен с ID {user_id}.")
    except Exception as e:
        print(f"Error adding user: {e}")
        conn.rollback()


def read_all_users():
    try:
        cursor.execute("SELECT * FROM public.users;")
        rows = cursor.fetchall()
        print("Все пользователи:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
    except Exception as e:
        print(f"Error reading all users: {e}")


def read_one_user(user_id):
    try:
        cursor.execute("SELECT * FROM public.users WHERE id = %s;", (user_id,))
        user = cursor.fetchone()
        if user:
            print(
                f"Пользователь найден: ID: {user[0]}, Name: {user[1]}, Age: {user[2]}"
            )
        else:
            print(f"Пользователь с ID {user_id} не найден.")
    except Exception as e:
        print(f"Error reading user: {e}")


def update_user(user_id, name=None, age=None):
    try:
        if name and age:
            cursor.execute(
                "UPDATE public.users SET name = %s, age = %s WHERE id = %s;",
                (name, age, user_id),
            )
        elif name:
            cursor.execute(
                "UPDATE public.users SET name = %s WHERE id = %s;", (name, user_id)
            )
        elif age:
            cursor.execute(
                "UPDATE public.users SET age = %s WHERE id = %s;", (age, user_id)
            )
        else:
            print("No updates provided.")
            return
        conn.commit()
        print(f"Пользователь с ID {user_id} обновлен успешно.")
    except Exception as e:
        print(f"Error updating user: {e}")
        conn.rollback()


def delete_user(user_id):
    try:
        cursor.execute("DELETE FROM public.users WHERE id = %s;", (user_id,))
        conn.commit()
        print(f"Пользователь с ID {user_id} успешно удален.")
    except Exception as e:
        print(f"Error deleting user: {e}")
        conn.rollback()


if __name__ == "__main__":
    create_user("Denis", 39)
    create_user("Ivan", 25)
    create_user("Vladislav", 35)

    print("\nВывод всех пользователей:")
    read_all_users()

    print("\nВывод информации об одном пользователе:")
    read_one_user(2)

    print("\nОбновление информации о пользователе:")
    update_user(2, name="Robert", age=26)

    print("\nВывод информации об одном пользователе:")
    read_one_user(2)

    print("\nУдаление пользователя:")
    delete_user(3)

    print("\nВывод всех пользователей:")
    read_all_users()

cursor.close()
conn.close()
