class Employee:
    __id_counter = 100000
    def __init__(self, name, surname):
        self.id = Employee.__id_counter
        Employee.__id_counter += 1 # TODO: take care of overflow after 999 999
        self.name = name
        self.surname = surname
    pass

class Hourly(Employee):
    pass

class Executive(Employee):
    pass

class Commercial(Employee):
    pass

class Director(Employee):
    pass
