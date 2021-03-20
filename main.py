def main(value):
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
