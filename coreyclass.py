class Employee():

    num_of_emps = 0

    raise_amount = 1.05
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount): #working with class rather than the instances
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
class Developer(Employee):
    raise_amount = 1.25

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())

dev_1 = Developer('Milan', 'Kharel', 50000, 'Python')
dev_2 = Developer('Melon', 'Musk', 60000, 'Java')

mgr_1 = Manager('Mahesh','Sah', 95000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()

print(isinstance(mgr_1, Manager)) #checks the instances

print(issubclass(Developer, Employee))

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(Employee.num_of_emps)

# import datetime
# my_date = datetime.date(2025, 1, 1)

# print(Employee.is_workday(my_date))

# emp_1 = Employee('milan', 'kharel', 50000)
# emp_2 = Employee('Melon', 'Musk', 60000)
# emp_3 = Employee('Malon', 'Sharma', 75000)

# emp_str_4 = 'Mahesh-Sah-70000'

# new_emp_4 = Employee.from_string(emp_str_4)

# print(new_emp_4.email)

# print(Employee.num_of_emps)

# print(emp_1.fullname()) # instance with method we not need have to pass self is intance as the code recognize
# print(Employee.fullname(emp_2)) #method is passed in class we need to pass instance

# regular methods and a class method automatically takes instance as it first argumnetts


# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# emp_1.raise_amount = 1.10

# print(emp_1.__dict__)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)

# Employee.set_raise_amt(1.15)

# print(Employee.raise_amount)