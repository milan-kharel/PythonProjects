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

print(Employee.num_of_emps)

emp_1 = Employee('milan', 'kharel', 50000)
emp_2 = Employee('Melon', 'Musk', 60000)
emp_3 = Employee('Malon', 'Sharma', 75000)

print(Employee.num_of_emps)

print(emp_1.fullname()) # instance with method we not need have to pass self is intance as the code recognize
print(Employee.fullname(emp_2)) #method is passed in class we need to pass instance

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

emp_1.raise_amount = 1.10

print(emp_1.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)