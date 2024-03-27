def calculate_parking_load(total_parking_spaces, occupied_parking_spaces):
    if total_parking_spaces < occupied_parking_spaces or total_parking_spaces < 0:
        print ('вводные ошибочны')
    total = occupied_parking_spaces/total_parking_spaces * 100
    return total

print(f'Парковка занята на {calculate_parking_load(5,3)}%')