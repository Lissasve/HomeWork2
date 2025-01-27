from random import randint
import threading
from time import sleep


class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for n in range(100):
            random_number = randint(50, 500)

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            self.balance += random_number
            print(F'Пополнение: {random_number}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for n in range(100):
            random_number = randint(50, 500)
            print(F'Запрос на {random_number}')

            if random_number <= self.balance:
                self.balance -= random_number
                print(F'Снятие: {random_number}. Баланс: {self.balance}')

            if random_number > self.balance:
                print(F'Запрос отклонен, недостаточно средств')
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
