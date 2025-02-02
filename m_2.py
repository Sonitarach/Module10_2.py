import threading
from threading import Thread
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)
        self.enemies = 100
        self.days = 0


    def run(self):
        print(f'{self.name} на нас напали')
        while self.enemies > 0:
            self.enemies -= self.power
            self.days += 1
            time.sleep(1)
            print(f"{self.name} сражается {self.days} день(дня)...,"
                  f" осталось {max(0, self.enemies)} воинов.")
        print(f"{self.name} одержал победу спустя {self.days} день(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Все битвы окончены!')
