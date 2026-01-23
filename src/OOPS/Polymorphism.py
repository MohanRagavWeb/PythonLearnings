
#Mini Program — Inheritance + Polymorphism
class Employee:
    def get_role(self):
        print("Employee")

class Manager(Employee):
    def get_role(self):
        print("Manager")

class Intern(Employee):
    def get_role(self):
        print("Intern")

staff = [Manager(), Intern()]

for person in staff:
    person.get_role()

print("\n")
#Polymorphism in Inheritance (Key Idea)

class DataSource:
    def read(self):
        print("Reading data")

class CSVSource(DataSource):
    def read(self):
        print("Reading CSV file")

class APISource(DataSource):
    def read(self):
        print("Reading API data")

sources = [CSVSource(), APISource()]

for s in sources:
    s.read()
