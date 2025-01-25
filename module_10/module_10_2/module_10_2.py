import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        days = 0
        print(F'{self.name}, на нас напали!')
        while enemies > 0:
            enemies -= self.power
            sleep(1)
            days += 1
            print(F'{self.name} сражается {days} дней(дня)..., осталось {enemies} воинов.')
        print(F'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(F'Все битвы закончились!')
