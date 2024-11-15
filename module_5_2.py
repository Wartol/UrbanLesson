class House():
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
    def go_to(self,new_floor):
        self.new_floor = new_floor
        for i in range(new_floor+1):
            if i < self.number_of_floors and i != 0:
                print(i)
                if i == new_floor:
                    print(f"{i} последний этаж")
            if i == self.number_of_floors:
                print(f"{self.new_floor} этажа не существует, {i} последний этаж")

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(len(h1))
print(len(h2))