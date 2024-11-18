import random
first = 'Мама мыла раму'
second = 'Рамена мало было'
test1 = lambda i,k: i == k
print(list(map(test1, first, second)))

def get_advanced_writer(file_name):
    test2 = open("example.txt", 'w',encoding='utf-8')
    def write_everything(*data_set):
        for i in data_set:
            test2.write(str(i) + '\n')

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self,*words):
        self.words = words

    def __call__(self):
        i = random.choice(self.words)
        return i

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

