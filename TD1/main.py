import models
from datetime import datetime

if __name__ == "__main__":
    date = datetime.today()
    employees = []

    print("Welcome to SAP 0.0.0.1.alpha.prototype.mvp")

    command = input('>')
    while command != 'exit':
        execute(command)
        command = input('>')

    print("Shutting off...")

def execute(command):
    if command[1] == "create":
        create(command)
    elif command[1] == "payroll":
        payroll(command)
    elif command[1] == "show":
        list(command)

def create(command):
    pass

def payroll(command):
    pass

def show(command):
    pass
