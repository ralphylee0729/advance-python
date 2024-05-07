class Employee:
    def __init__(self, name, id, level, salary):
        self.name = name
        self.id = id
        self.level = level
        self.salary = salary

    def __str__(self) :
        return f'Name:{self.name}\nId:{self.id}'



e1 = Employee("Andy Lee", 1, 5, 300000)

print(e1)

