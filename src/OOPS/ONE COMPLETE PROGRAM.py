from abc import ABC, abstractmethod

# =======================
# ABSTRACTION
# =======================
class Employee(ABC):

    def __init__(self, name, salary):
        # ENCAPSULATION (private variable)
        self.__salary = salary
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    # ENCAPSULATION (getter)
    def get_salary(self):
        return self.__salary

    # ENCAPSULATION (setter)
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary


# =======================
# INHERITANCE + POLYMORPHISM
# =======================

class FullTimeEmployee(Employee):

    def calculate_salary(self):
        return self.get_salary()


class PartTimeEmployee(Employee):

    def calculate_salary(self):
        return self.get_salary() * 0.5


# =======================
# MAIN PROGRAM
# =======================

employees = [
    FullTimeEmployee("Mohan", 50000),
    PartTimeEmployee("Ravi", 30000)
]

for emp in employees:
    print("Name:", emp.name)
    print("Final Salary:", emp.calculate_salary())
    print("--------------------")
