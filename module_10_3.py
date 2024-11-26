import random
import threading
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            time.sleep(0.1)
            random1 = random.randint(50, 500)
            self.balance += random1
            if self.balance >= 500 and self.lock.locked() == True:
                print(self.lock.locked())
                self.lock.release()
                print(f"Пополнение: {random1}")

    def take(self):
        for i in range(100):
            random2 = random.randint(50, 500)
            print(f"Запрос на {random2}")
            if random2 <= self.balance:
                self.balance -= random2
                print(f"Снятие: {random2}. Баланс: {self.balance}")
            if random2 >= self.balance:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()



bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')