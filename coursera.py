# Create Your First Python Program From UST

#Function
def add (a,b):
  total = a+b
  return total

output = add(9,10)
print (output)

#List
people = ['milan', 'Melon']
people.append('Malone')
print(people)
name = people.pop()
print(name)
print(people)
people.remove('milan')
print(people)
people.append(9)
print(people)

#Tuples

hell = ('rita', 'gita')
print(hell)
hell = (1,3,4,5)
print(hell)

#conditional Statements

age = 2

if age < 19:
  print('you are young')
elif age < 70:
  print('You are adult')
else:
  print('Ohhh senior citizen')

  #for loop

people = ['milan', 'Melon', 'Malone', 'Rita', 'Gita']
for person in people:
  print(person)

def square_value(value):
  for n in value:
    sq = n*n
    print('The square of', n, 'is', sq)

value = [1,2,3,4,5]
square_value(value)

#user input and the while loop

user = input('Enter your name: ')
while user != 'quit':
  print('Hello', user)
  user = input('Enter your name: ')
  print('you entered: ', user)

print(type(user))

numbers = [1, 2, 3, 4, 5]
numbers.pop()
numbers.remove(1)
print(numbers)

def print_square_value(numbers):
    for number in numbers:
        if number != 2:
            squared = number * number
            print(squared)

numbers = [1, 2, 3, 4]

print_square_value(numbers)

