import redis

client = redis.Redis(host="localhost", port=6379, decode_responses=True)
table_name = "Users"


def read_all_rows():
    users = client.hgetall(table_name)
    print("Список всех пользователей:")
    for user_id, user_data in users.items():
        name, surname = user_data.split(":")
        print(f"ID: {user_id}, Имя: {name}, Фамилия: {surname}")


def read_one_row(user_id):
    user_data = client.hget(table_name, user_id)
    if user_data:
        name, surname = user_data.split(":")
        print(f"ID: {user_id}, Имя: {name}, Фамилия: {surname}")
    else:
        print(f"Пользователь с ID {user_id} не найден.")


def write_row(user_id, name, surname):
    user_data = f"{name}:{surname}"
    client.hset(table_name, user_id, user_data)
    print(f"Пользователь {name} {surname} добавлен с ID {user_id}.")


def delete_row(user_id):
    result = client.hdel(table_name, user_id)
    if result:
        print(f"Пользователь с ID {user_id} удален.")
    else:
        print(f"Пользователь с ID {user_id} не найден.")


if __name__ == "__main__":
    write_row("1", "Denis", "Akimov")
    write_row("2", "Petr", "Petrov")
    write_row("3", "Sidor", "Sidorov")

    print("\nЧтение всех строк:")
    read_all_rows()

    print("\nЧтение одной строки:")
    read_one_row("2")

    print("\nУдаление строки:")
    delete_row("2")

    print("\nЧтение всех строк после удаления:")
    read_all_rows()
