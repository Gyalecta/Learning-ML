# Iterable = object from where we can get an iterator, for example a list.
# Iterator = object that returns progressively its own elements using next()
# Generator = particular type of iterator, that I already used in the previous lab 

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator)) # 10
print(next(iterator)) # 20

# But what happens if we combine next() with a for loop?

numbersCopy = [10, 20, 30, 40]

iteratorCopy = iter(numbersCopy)

print(next(iteratorCopy))

for x in iterator:
    print(x)

