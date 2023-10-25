def read_file(csv_file: str) -> tuple[list[str], list[str]]:
    """
    Функция принимает файл в формате .csv,
    выводит список, который содержит данные файла,
    разбитые по строкам, и заголовки.
    """

    if not isinstance(csv_file, str):
        raise TypeError('Инпут должен содержать строковые значения')

    if not csv_file.endswith('.csv'):
        raise ValueError('Инпут должен быть .csv файлом')

    with open(csv_file, 'r') as file:
        csv_data = file.read()

    lines = csv_data.split('\n')
    header = lines[0].split(';')

    return lines, header


def create_department_dict(
    file='Corp_Summary.csv',
    department='Департамент',
    first_header='Отдел',
    second_header='Оклад',
) -> dict[str, dict[str, list[str | float]]]:
    """
    Из .csv файла создает словарь, где ключом является департамент.
    Значениями словаря являются данные других столбцов в файле,
    которые относятся к тому или иному департаменту.
    Содержит аргументы, заданные по умолчанию.
    Использует функцию чтения .csv файлов read_file()
    """

    new_dict = {}

    result = read_file(file)

    lines = result[0]
    header = result[1]

    department_index = header.index(department)
    first_index = header.index(first_header)
    second_index = header.index(second_header)

    for line in lines[1:]:
        if line:
            text = line.split(';')
            dict_key = text[department_index]
            first_value = text[first_index]
            second_value = text[second_index]
            if dict_key in new_dict:
                if first_value not in new_dict[dict_key][first_header]:
                    new_dict[dict_key][first_header].append(first_value)
                new_dict[dict_key][second_header].append(int(second_value))
            else:
                new_dict[dict_key] = {
                    first_header: [first_value],
                    second_header: [int(second_value)],
                }

    return new_dict


def offices_in_department() -> str:
    """
    Печатает иерархию отделов в департаменте.
    Сохраняет созданный вывод.
    """

    result_dict = create_department_dict()

    output = ''

    for department, values in result_dict.items():
        output += f'\n{department}:\n'
        for item in values['Отдел']:
            output += f'- {item}\n'

    print(output)

    return output


def department_info() -> tuple[str, list[list[str | float]]]:
    """
    Выводит следующую информацию о департаменте:
    - Название департамента
    - Численность сотрудников
    - Зарплатную вилку
    - Средний оклад
    Сохраняет вывод, а также создает список,
    где содержатся данные по департаменту,
    чтобы к нему можно было обратиться при необходимости.
    Использует словарь из функции create_department_dict().
    """

    result_dict = create_department_dict()

    output = ''
    info_list = []

    for department, info in result_dict.items():
        salaries = info['Оклад']
        length = len(salaries)
        min_salary = min(salaries)
        max_salary = max(salaries)
        avg_salary = sum(salaries) / length

        list = []

        list.append(department)
        list.append(length)
        list.append(f'{min_salary} - {max_salary}')
        list.append(f'{avg_salary:.2f}\n')

        info_list.append(list)

        output += f'\n{department}:\n'
        output += f'- Численность: {length}\n'
        output += f'- Вилка: {min_salary} - {max_salary}\n'
        output += f'- Средний оклад: {avg_salary:.2f}\n'

    return output, info_list


def save_report() -> None:
    """
    Создает .csv файл под названием 'department_info.csv',
    куда записывает данные по департаментам.
    Использует список из функции department_info().
    """

    report = department_info()
    info_list = report[1]

    with open('department_info.csv', 'w') as csv_file:
        csv_file.write('Департамент, Численность, Вилка, Средний оклад\n')

        for row in info_list:
            csv_file.write(','.join(map(str, row)))

    return


def menu():
    """
    Функция выводит на экран доступные для пользователя опции,
    которые он может сделать с csv файлом.
    Затем она предлагает выбрать одну из 3-х опций.
    В зависимости от ввода, вызывается одна из 3-х функций.
    Если пользователь вводит число, для которого нет вызываемой функции,
    его просят выбрать среди доступных номеров.
    """

    print(
        'Меню\n'
        'Опции:\n'
        '1. Вывести иерархию команд\n'
        '2. Вывести сводный отчёт по департаментам\n'
        '3. Сохранить сводный отчёт по департаментам в виде csv-файла\n'
    )

    while True:
        choice = input('Введите номер необходимой опции:\n')

        if choice == '1':
            offices_in_department()
            break

        elif choice == '2':
            result = department_info()
            print(result[0])
            break

        elif choice == '3':
            save_report()
            break

        else:
            print(
                'Данная опция отсутствует. Выберите номер из доступных опций.'
            )

    return


if __name__ == '__main__':
    menu()
