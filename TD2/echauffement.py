#! /usr/bin/python3

import threading

iterations = 100


class Compteur():
    value = 0

class Stupidthread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(10_000):
            Compteur.value += 1
            Compteur.value -= 1
        Compteur.value += 1


def naivethreads():
    compteur = Compteur()
    threads = []
    for t in range(10000):
        t = Stupidthread()
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(Compteur.value) # Without joining we finish and get 0


# We do not get to 10_000
# we need locks
class Syncthread(threading.Thread):
    def __init__(self, lock):
        threading.Thread.__init__(self)
        self.lock = lock

    def run(self):
        self.lock.acquire()
        for i in range(10_000):
            Compteur.value += 1
            Compteur.value -= 1
        Compteur.value += 1
        self.lock.release()

def syncthreads():
    compteur = Compteur()
    threads = []
    lock = threading.Lock()
    for t in range(10000):
        t = Syncthread(lock)
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(Compteur.value) # Wooo we get 10 000!


if __name__ == "__main__":
    naivethreads()
