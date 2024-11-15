class IncorrectVinNumber(Exception):
    def __init__(self,message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self,message):
        self.message = message

class Car():
    def __init__(self,model,__vin,__numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = str(__numbers)
        self.__is_valid_vin()
        self.__is_valid_numbers()

    def __is_valid_vin(vin_number):
        if isinstance(vin_number.__vin, int):
            if vin_number.__vin in range(1000000, 9999999):
                True
            else: raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else: raise IncorrectVinNumber('Некорректный тип vin номер')

    def __is_valid_numbers(numbers):
        if isinstance(numbers.__numbers, str):
            if len(numbers.__numbers) == 6 :
                True
            else: raise IncorrectCarNumbers('Неверная длина номера')
        else:raise IncorrectCarNumbers('Некорректный тип данных для номеров')

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
     print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')