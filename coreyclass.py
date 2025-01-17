class Employee():
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
emp_1 = Employee('milan', 'kharel', 50000)
emp_2 = Employee('Melon', 'Musk', 60000)

print(emp_1.fullname()) # instance with method we not need have to pass self as the code recognize
print(Employee.fullname(emp_2)) #method is passed in class we need to pass instance