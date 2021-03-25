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


def getting_hours(even, hours):
    if even:
        hours += calculate(rows[1]['values'][0][0])


for i in range(1, 15):
    letter = chr(65 + i)  # Получаю букву (колонку), которую потом передам в функцию read_values()
    hours = 0
    if i % 2 != 0:
        even = False
    else:
        even = True
    rows = spreadsheet.read_values(letter, even)
    # Лицей не всегда встречается в таблице (в свободном времени), поэтому try except
    # необходим. Хмммм... как бы выкрутиться здесь...
    try:
        # hours += calculate(rows[0]['values'][0][0])
        getting_hours(even, )
    except KeyError:
        pass

    if not even:
        spreadsheet.write_values(hours, letter + '9')
    else:
        try:
            hours += calculate(rows[1]['values'][0][0])
        except KeyError:
            pass
        spreadsheet.write_values(hours, letter + '13')
