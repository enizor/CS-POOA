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
        self.queue = multiprocessing.Queue()
        self.lock = threading.Lock()

    def printjob(self, doc):
        self.lock.acquire()
        for p in range(doc.page_nb):
            time.sleep(0.5)
            print("Doc #{}: page {}".format(doc.id, p))
        self.lock.release()

def synced():
    epson = SyncedPrinter()
    for i in range(10):
        t = threading.Thread(epson.printjob(Document(i, random.randint(1,5))))
        t.start()

if __name__ == "__main__":
    synced()
