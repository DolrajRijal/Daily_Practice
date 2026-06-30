class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: £{self.salary}")

    def annual_salary(self):
        return self.salary * 12


emp1 = Employee("John", 3000)

emp1.display()
print("Annual Salary:", emp1.annual_salary())