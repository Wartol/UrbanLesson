class Vehicle:
    def __init__(self,owner,_model,_engine_power,__color):
        self.owner = owner
        self._model = _model
        self._engine_power = _engine_power
        self.__color = __color

    __COLOR_VARIANTS = ['черный', 'красный', 'зелёный', 'чёрный', 'белый','фиолетоый']
    def get_model(self):
        print(f"Модель:{self._model}")
    def get_horsepower(self):
        print(f"Мощность движка:{self._engine_power}")
    def get_color(self):
        print(f"Цвет:{self.__color}")
    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f"Владелец:{self.owner}")

    def set_color(self,new_color):
        new_color = new_color.lower()
        for i in (self.__COLOR_VARIANTS):
            if i == new_color:
                self.__color = new_color
        if new_color != self.__color:
            print(f'Нельзя покрасить в {new_color}! Ты в розыске')
        if new_color == self.__color:
            print(f'Отличная покраса в {new_color}! Копы теперь тебя не узнают')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500,'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('серо-буро-малиноый')
vehicle1.set_color('фиолетоый')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()