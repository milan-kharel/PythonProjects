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

print(Employee.num_of_emps)

import datetime
my_date = datetime.date(2025, 1, 1)

print(Employee.is_workday(my_date))

emp_1 = Employee('milan', 'kharel', 50000)
emp_2 = Employee('Melon', 'Musk', 60000)
emp_3 = Employee('Malon', 'Sharma', 75000)

emp_str_4 = 'Mahesh-Sah-70000'

new_emp_4 = Employee.from_string(emp_str_4)

print(new_emp_4.email)

print(Employee.num_of_emps)

print(emp_1.fullname()) # instance with method we not need have to pass self is intance as the code recognize
print(Employee.fullname(emp_2)) #method is passed in class we need to pass instance

# regular methods and a class method automatically takes instance as it first argumnetts


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

emp_1.raise_amount = 1.10

print(emp_1.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)

Employee.set_raise_amt(1.15)

print(Employee.raise_amount)