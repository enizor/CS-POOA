import random


class Employee:
    __id_counter = 100000
    def __init__(self, name, surname):
        self.id = Employee.__id_counter
        Employee.__id_counter += 1 # TODO: take care of overflow after 999 999
        self.name = name
        self.surname = surname
        self.login = "{}{}{}".format(name[1],surname[1], self.id)

class Hourly(Employee):
    def __init__(self, name, surname):
        self.wage_points = 290
        super().__init__(name, surname)

class Executive(Employee):
    def __init__(self, name, surname):
        self.wage_points = 600
        super().__init__(name, surname)

class Commercial(Executive):
    def __init__(self, name, surname, phone_number=random.randint(100_000_000, 999_999_999)):
        self.phone = Phone(number)
        super().__init__(name, surname)


class Director(Executive):
    def __init__(self, name, surname, phone_number=random.randint(100_000_000, 999_999_999)):
        self.phone = Phone(phone_number)
        self.wage_points = 1_000
        super().__init__(name, surname)


class Phone:
    def __init__(self, phone_number):
        # TODO: format with spaces and hyphens
        self.number = "{:10}".format(phone_number)
        self.mac = "{:0x}".format(random.randint(0, 2**48))
