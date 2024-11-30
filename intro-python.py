# Variables and data types
# We have 4 types of data types
# Integer, Float, String, Boolean

# Integer
x = 20
y = 30
print(x + y)

# Float
price = 2.5
size = 7.8
quantity = 10
print(f'The price of the ball you want to buy is {price}')
print(f'The size of the each item we have for now is {size}')
print(f'And we still have like {quantity} stuck inside our store')

#String
name = 'Akinola Femi'
age = 20
skills = 'Software Engineer'
print(f'My name is {name}, I am {age} years old, I am {skills}')

# Boolean
Online = False
Product = False
print(f'Is this product still remain inside our store?? {True}')
print(f'Did you still have this product is your store because of I want to make an order soon {Product}')

if Online:
    print('the user is active online right now at this moment')
else:
    print('The user has not been active since all this while')

# Group variable
location , city,  states = 'Nigeria', 'Ikorodu City', 'Lagos State'
print(location + ' ' + city + " " + states)