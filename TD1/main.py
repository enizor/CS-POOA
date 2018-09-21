#! /bin/python3
import models
from datetime import datetime

if __name__ == "__main__":
    global employees
    employees = []

    print("Welcome to SAP 0.0.0.1.alpha.prototype.mvp")

    command = input('>')
    while command != 'exit':
        execute(command.split())
        command = input('>')

    print("Shutting off...")

def execute(command):
    if command[0] == "create":
        create(command)
    elif command[0] == "payroll":
        payroll(command)
    elif command[0] == "show":
        list(command)

def create(command):
    if command[1] == "hourly":
        models.Hourly(command[2])
    elif command[1] == "executive":
        models.Executive
def payroll(command):
    pass

def show(command):
    pass
