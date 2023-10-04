

def step2_option1():

    """
    Функция открывает csv файл.
    Выделяет департамент и отдел по индексам.
    Создает словарь, где ключом является департамент,
    а значениями - отделы, принадлежащие ему.
    Затем выводит на экран получившийся отчет в красивом виде.
    """

    with open('Corp_Summary.csv', 'r') as file:
        csv_data = file.read()

    lines = csv_data.split('\n')
    header = lines[0].split(';')
    department_index = header.index('Департамент')
    office_index = header.index('Отдел')

    department_office_dict = {}

    for line in lines[1:]:
        if line:
            text = line.split(';')
            department = text[department_index]
            office = text[office_index]
            if department in department_office_dict:
                department_office_dict[department].add(office)
            else:
                department_office_dict[department] = {office}

    for department, offices in department_office_dict.items():
        print(f"Департамент: {department}")
        print("Отделы:")
        for office in offices:
            print(f"- {office}")
        print()

    return


def step2_option2():

    """
    Функция открывает csv файл.
    Выделяет департамент и оклад по индексам.
    Создает два словаря - один с информацией по сотрудникам,
    другой - с информацией по окладам.
    Функция считает количество сотрудников в департаменте,
    а также сумму окладов, минимальный, максимальный и средний оклады.
    Затем выводит на экран получившийся отчет в красивом виде.
    Возвращает два словаря:
    - department_people_dict - информация по сотрудникам
    - department_money_dict - информация по окладам
    """

    with open('Corp_Summary.csv', 'r') as file:
        csv_data = file.read()

    lines = csv_data.split('\n')
    header = lines[0].split(';')
    department_index = header.index('Департамент')
    money_index = header.index('Оклад')

    department_people_dict = {}
    department_money_dict = {}

    for line in lines[1:]:
        if line:
            text = line.split(';')
            department = text[department_index]
            payment = int(text[money_index])

            if department in department_people_dict:
                department_people_dict[department] += 1
            else:
                department_people_dict[department] = 1

            if department in department_money_dict:
                department_money_dict[department]['total'] += payment
                department_money_dict[department]['min'] = min(department_money_dict[department]['min'], payment)
                department_money_dict[department]['max'] = max(department_money_dict[department]['max'], payment)
            else:
                department_money_dict[department] = {'total': payment, 'min': payment, 'max': payment}

    for department, data in department_money_dict.items():
        data['average'] = data['total'] / department_people_dict[department]

    for department, data in department_money_dict.items():
        print(f"Департамент: {department}")
        print(f"Численность: {department_people_dict[department]}")
        print(f"Минимальный оклад: {data['min']}")
        print(f"Максимальный оклад: {data['max']}")
        print(f"Средний оклад: {data['average']:.2f}")
        print()

    return department_people_dict, department_money_dict


def step2_option3():

    """
    Функция использует словари, полученные в результате выполнения функции step2_option2().
    Используя эти данные, она создает новый csv файл, который содержит информацию
    о сотрудниках и их заработной плате.
    Файл создается со следующим названием: department_info.csv
    Заголовки: Департамент, Численность, Минимальный оклад, Максимальный оклад, Средний оклад
    Пользователя оповещают, когда csv файл создан и готов к использованию.
    """

    department_people_dict, department_money_dict = step2_option2()
    with open('department_info.csv', 'w') as csv_file:
        csv_file.write("Департамент,Численность,Минимальный оклад, Максимальный оклад,Средний оклад\n")
        for department, data in department_money_dict.items():
            csv_file.write(f"{department}, {department_people_dict[department]}, {data['min']},{data['max']},{data['average']:.2f}\n")
    print("Информация о департаментах сохранена как 'department_info.csv'.")

    return


def step1():

    """
    Функция выводит на экран доступные для пользователя опции, которые он может сделать с csv файлом.
    Затем она предлагает выбрать одну из 3-х опций.
    В зависимости от ввода, вызывается одна из 3-х функций.
    Если пользователь вводит число, для которого нет вызываемой функции,
    его просят выбрать среди доступных номеров.
    """

    print(
        'Меню\n'
        'Опции:\n'
        '1. Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него\n'
        '2. Вывести сводный отчёт по департаментам: название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату\n'
        '3. Сохранить сводный отчёт по департаментам в виде csv-файла\n'
    )
    choice = input("Введите номер необходимой опции\n")

    if choice == '1':
        step2_option1()

    if choice == '2':
        step2_option2()

    if choice == '3':
        step2_option3()

    if choice != '1' and choice != '2' and choice != '3':
        print('Данная опция отсутствует. Пожалуйста, выберите номер из доступных опций.')

    return


if __name__ == '__main__':
    step1()
