"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Дан список покупок в приложении. Предоставить пользователю возможность удалять
товар по его номеру (не индексу)
"""
shopping_list = ["молоко", "сметана", "сыр"]


def del_by_num(collection: list, num: int) -> list:
    # TODO вставить код сюда
    # collection.pop(num - 1)
    del collection[num - 1]
    return collection


if __name__ == '__main__':
    print("Удаляем второй товар - сметана...")
    result = del_by_num(shopping_list, 2)
    if "сметана" not in shopping_list:
        print("Удаление прошло успешно!")
    else:
        print("Произошла ошибка при удалении...")
