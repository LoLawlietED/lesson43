import threading
from random import randint
from time import sleep
from threading import Thread, Lock
class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()
    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            rand_2 = randint(50,500)
            self.balance += rand_2
            print(f'Пополнение: {rand_2}.Баланс:{self.balance}')
            sleep(0.001)
    def take(self):
        for y in range(100):
            rand = randint(50,500)
            print(f'Запрос на {rand}')
            if rand <= self.balance:
                self.balance -= rand
                print(f'Снятие:{rand}.Баланс:{self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')