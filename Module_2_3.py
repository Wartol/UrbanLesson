my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_number = 0
while len(my_list) > list_number:
    if my_list[0 + list_number] > 0:
        print(my_list[0 + list_number])
        list_number = list_number + 1
    else:
        list_number = list_number + 1
    if my_list[0 + list_number] == 0:
        break

