# Basic variables declarations 

age = 21 # Integer 
name = "Domenico" # Decimal
height = 1.75 # String
student = True # Boolean

x = 10 
x = "Python"

print(x)

# Mutable and immutable objects

numbers = [10, 20, 30]
numbers[0] = 99

print(numbers)


# Scope, where does a variable exists?

x = 10 

def example():
    x = 20 
    print(x)

example()
print(x)


# Truthiness, how does Python interpret a boolean?

numbers = []

if numbers:
    print("The list contains elements")
else:
    print("The list is empty")

# Some falsy: 0, 0.0, "", [], {}, None and False 


# Unpacking: assigning more values altogether

coordinates = (10, 20)

x, y = coordinates 

print(x)
print(y)

# we can also use operator * to collect more items 

numbers = [10, 20, 30, 40]

first, *remaining = numbers
print(first) # 10
print(remaining) # [20, 30, 40]

