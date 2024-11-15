class House():
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return self.number_of_floors + value

    def __radd__(self, value):
        return self.number_of_floors + value

    def __iadd__(self, value):
        return self.number_of_floors + value

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(list(args)[0])
        return super().__new__(cls)

    def __del__(self):
        print(f"{self} снесён, но он останется в истории")
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        for i in range(new_floor + 1):
            if i < self.number_of_floors and i != 0:
                print(i)
                if i == new_floor:
                    print(f"{i} последний этаж")
            if i == self.number_of_floors:
                print(f"{self.new_floor} этажа не существует, {i} последний этаж")

    houses_history = []


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2: House = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
