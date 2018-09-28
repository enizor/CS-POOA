#! /usr/bin/python3

import threading
import time
import random
import multiprocessing

class Document():
    def __init__(self, id, page_nb):
        self.id = id
        self. page_nb = page_nb

class NaivePrinter():

    def printjob(self, doc):
        for p in range(doc.page_nb):
            time.sleep(0.5)
            print("Doc #{}: page {}".format(doc.id, p))


def naive():
    epson = NaivePrinter()
    for i in range(10):
        t = threading.Thread(epson.printjob(Document(i, random.randint(1,5))))
        t.start()
    # all the docs are printed at the same time!


class SyncedPrinter():
    def __init__(self):
        self.lock = threading.Lock()

    def printjob(self, doc):
        self.lock.acquire()
        for p in range(doc.page_nb):
            time.sleep(5)
            print("Doc #{}: page {}".format(doc.id, p))
        self.lock.release()

def synced():
    epson = SyncedPrinter()
    for i in range(10):
        t = threading.Thread(epson.printjob(Document(i, random.randint(1,5))))
        t.start()
    # Evervy document gets printed when the printer actually has the time to!

class MultipleDocPrinter():
    def __init__(self, n):
        self.locks = [ threading.Lock() for i in range(n)]
        self.n = n

    def find_lock(self):
        """
        Returns the first available lock
        """
        p = 0
        found = False
        while not found:
            if self.locks[p].acquire(blocking=False):
                return p
            else:
                p += 1
                p %= self.n

    def printjob(self, document):
        l = self.find_lock()
        print('printing doc {} from printer #{}'.format(document.id, l))
        for p in range(document.page_nb):
            time.sleep(0.5)
            print("Doc #{}: page {}".format(document.id, p))
        print('releasing: ', l)
        self.locks[l].release()

def multiple():
    epson = MultipleDocPrinter(2)
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=epson.printjob(Document(i, random.randint(1,5)))))
    for t in threads:
        t.start()
        print("started a thread")
    # Every document gets printed on lock 0, not sure why the threads cant start at the same time...


if __name__ == "__main__":
    multiple()
