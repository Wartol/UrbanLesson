from pprint import pprint
class Product:
    def __init__(self,name,weight,category):
        self.name = name
        self.weight = str(weight)
        self.category = category
    def __str__(self):
        return (self.name +", "+ self.weight +", "+ self.category) #Запятая после каждого атрибута
class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        line1 = set(file.read().split())
        file.close()
        return line1 #не понимаю как правильно это сделать... и помощи ждать не откуда
    def add(self, *products):
        current_products = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            if product.name + ',' not in current_products: #чёртова запитая
                print(1)
                #file.write('\n'+str(product))
            else: print(product.name,'Такой продукт уже есть в списке')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())