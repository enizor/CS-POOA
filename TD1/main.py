class Employee:
    __id_counter = 100000
    def __init__(self, name, surname):
        self.id = Employee.__id_counter
        Employee.__id_counter += 1 # TODO: take care of overflow after 999 999
        self.name = name
        self.surname = surname

class Hourly(Employee):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    wage_points = 290

class Executive(Employee):
    pass

class Commercial(Employee):
    pass

class Director(Employee):
    pass
