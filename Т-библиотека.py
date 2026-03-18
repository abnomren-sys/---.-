import json
import os

# файл
file = "books.json"


# загрузить
def load():
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    else:
        return []


# сохранить
def save(data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# добавить
def add(data):
    name = input("Название: ")
    avtor = input("Автор: ")
    janr = input("Жанр: ")

    book = {
        "name": name,
        "avtor": avtor,
        "janr": janr,
        "status": "не прочитана",
        "fav": False
    }

    data.append(book)
    print("Книга добавлена")


# список
def list(data):
    if len(data) == 0:
        print("Пусто")
        return

    i = 1
    for b in data:
        if b["fav"] == True:
            z = "★"
        else:
            z = " "

        print(str(i) + ". " + b["name"] + " - " + b["avtor"] + " [" + b["status"] + "] " + z)
        i = i + 1


# прочитано
def read(data):
    list(data)

    if len(data) == 0:
        return

    n = input("Номер книги: ")
    n = int(n)

    if n >= 1 and n <= len(data):
        data[n - 1]["status"] = "прочитана"
        print("Статус изменнён")
    else:
        print("Нет такой книги")


# избранное (добавить/убрать)
def fav(data):
    list(data)

    if len(data) == 0:
        return

    n = input("Номер книги: ")
    n = int(n)

    if n >= 1 and n <= len(data):
        if data[n - 1]["fav"] == True:
            data[n - 1]["fav"] = False
            print("Удаленно из избранного")
        else:
            data[n - 1]["fav"] = True
            print("Добавленно в избранное")
    else:
        print("Нет такой книги")


# показать только избранные
def show_fav(data):
    print("\n=== ИЗБРАННОЕ ===")

    # найти все избранные книги
    fav_books = []
    for b in data:
        if b["fav"] == True:
            fav_books.append(b)

    if len(fav_books) == 0:
        print("Нет избранных книг")
        return

    i = 1
    for b in fav_books:
        print(str(i) + ". " + b["name"] + " - " + b["avtor"] + " [" + b["status"] + "]")
        i = i + 1

    print("\n1. Удалить книгу из избранного")
    print("2. Назад")

    v = input("Выбери действие: ")

    if v == "1":
        n = input("Номер книги в списке: ")
        n = int(n)

        if n >= 1 and n <= len(fav_books):
            # найти эту книгу в основном списке
            kniga = fav_books[n - 1]
            for b in data:
                if b["name"] == kniga["name"] and b["avtor"] == kniga["avtor"]:
                    b["fav"] = False
                    print("Удалено из избранного")
                    break
        else:
            print("Нет такой книги")


# удалить
def delit(data):
    list(data)

    if len(data) == 0:
        return

    n = input("Номер книги: ")
    n = int(n)

    if n >= 1 and n <= len(data):
        b = data[n - 1]
        data.pop(n - 1)
        print("Удалил " + b["name"])
    else:
        print("Нет такой книги")


# главное
def main():
    data = load()

    while True:
        print("\n=== Т-БИБЛИОТЕКА ===")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Изменить статус книги")
        print("4. Избранное (добавить/убрать)")
        print("5. Список избранного")
        print("6. Удалить книгу")
        print("7. Сохранить и выйти")

        v = input("Выбрать действие: ")

        if v == "1":
            add(data)
        elif v == "2":
            list(data)
        elif v == "3":
            read(data)
        elif v == "4":
            fav(data)
        elif v == "5":
            show_fav(data)
        elif v == "6":
            delit(data)
        elif v == "7":
            save(data)
            print("Изменения сохранены")
            break
        else:
            print("Нет действия")


# старт
if __name__ == "__main__":
    main()