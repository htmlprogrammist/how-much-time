import spreadsheet


def calculate(value):
    start_time_hours = int(value.split(' - ')[0].split(':')[0])  # получаю значение часа
    start_time_minutes = int(value.split(' - ')[0].split(':')[1])  # получаю значение минут
    end_time_hours = int(value.split(' - ')[1].split(':')[0])  # Аналогично
    end_time_minutes = int(value.split(' - ')[1].split(':')[1])  # Аналогично
    # 8:15 - 10:05 => '8:15', '10:05' => 8, 15, 10, 5
    diff_hours = end_time_hours - start_time_hours
    diff_minutes = end_time_minutes - start_time_minutes
    if diff_minutes < 0:
        diff_hours -= 1
        diff_minutes = 60 + diff_minutes  # 60 + (-10) = 50
    if diff_hours > 0:
        diff_minutes += diff_hours * 60
    result = round(diff_minutes / 60, 2)
    if result.is_integer():  # Чтобы выводило не 8.0, а 8
        return diff_minutes // 60
    else:
        return result


def call_calcutale(index):
    try:
        return calculate(rows[index]['values'][0][0])
    except KeyError:
        pass
# Проблема: будет считывать с каждой строчки, но при этом он ведь не суммирует количество часов
# Возможные пути решения:
# - Создаём глобальные переменные, а в функциях переменные будут через +=
# - Изначально, try и except был нужен только для лицея и второго вычисления времени после репы...
# ... мб тогда функцию адаптировать именно под эти задачи?
# Проблема тогда: а как обнулять эти значения для каждой новой буквы?

for i in range(1, 8):
    letter = chr(65 + i)  # Получаю букву (колонку), которую потом передам в функцию read_values()
    lyceum_result = 0
    tutoring_result = 0
    rows = spreadsheet.read_values(letter)  # len(rows) => 3 (т.к. range_names по 3 ячейки)
    for j in range(3):
        if j == 0:
            spreadsheet.write_values(call_calcutale(j), letter + '9')
        else:
            spreadsheet.write_values(call_calcutale(j), letter + '13')
    # spreadsheet.write_values(lyceum_result, letter + '9')
    # spreadsheet.write_values(tutoring_result, letter + '13')
