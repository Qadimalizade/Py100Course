# TODO Напишите функцию find_common_participant
def find_common_participants(list1, list2, x= ','):
    list1 = list(set(list1.split('|')))
    list2 = list(set(list2.split('|')))
    list3 = []
    for i in list1:
        if i in list2:
            list3.append(i)
    list4 = x.join(list3)
    return list4




participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '.'))
