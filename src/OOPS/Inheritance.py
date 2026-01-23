
#Inheritance with Constructor (__init__)
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, course):
        Person.__init__(self, name)
        self.course = course

s = Student("Mohan", "Data Engineering")
print(s.name, s.course)


print("\n #####")


#Real Data Engineering Example — Inheritance
class DataSource:
    def connect(self):
        print("Connecting to data source")

class CSVSource(DataSource):
    def read(self):
        print("Reading CSV")

class DBSource(DataSource):
    def read(self):
        print("Reading Database")

csv = CSVSource()
csv.connect()
csv.read()
