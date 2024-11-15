import math
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (math.fabs(len(i)-len(k)) for i,k in zip(first,second) if len(i) != len(k))
second_result = (bool(i) if len(first[i]) == len(second[i]) else False for i in range(3))
print(range(len(first)))
print(list(first_result))
print(list(second_result))
