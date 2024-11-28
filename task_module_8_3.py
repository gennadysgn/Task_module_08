def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    numbers_list = []
    for i in numbers:
        if type(i) is int:
            numbers_list.append(i)
    try:
        return list(personal_sum(numbers))[0] / len(numbers_list)
    except ZeroDivisionError:
        return 0


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
try:
    print(f'Результат 3: {calculate_average(567)}')
except TypeError:
    print('В numbers записан некорректный тип данных')
    print(f'Результат 3: None')  # Функция ничего не возвращает, None вывел сам
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
