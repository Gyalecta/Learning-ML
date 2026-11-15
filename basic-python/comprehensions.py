# List comprehension

filtered = [x for x in temperatures if x > 22] # creates a new List

filtered_v2 = (x for x in temperatures if x > 22) # generates an iterator that calculates values progressively when requested

# output would be similar to this: <generator object <genexpr> at 0x...>


# Lazy evaluation 

numbers = [1, 2, 3, 4, 5]
result = (x * 2 for x in numbers if x > 2)

print(next(result)) # 6
print(next(result)) # 8
print(next(result)) # 10

#  next() asks the generator for the next available element.
#  When all values are consumed, another call would give StopIteration exception
#  alternatively we can use:

print(list(result))
