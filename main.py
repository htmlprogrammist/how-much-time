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
    if result.is_integer():
        return diff_minutes // 60
    else:
        return result


for i in range(1, 8):
    letter = chr(65 + i)
    lyceum_result = 0
    tutoring_result = 0
    rows = spreadsheet.read_values(letter)
    # print(rows)
    try:
        lyceum_result = calculate(rows[0]['values'][0][0])
    except KeyError:
        pass
    tutoring_result = calculate(rows[1]['values'][0][0])
    try:
        tutoring_result += calculate(rows[2]['values'][0][0])
    except KeyError:
        pass
    # print(lyceum_result, tutoring_result)
    
