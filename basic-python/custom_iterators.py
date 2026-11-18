# An iterator can have two main methods.
#
# __iter__() = returns the iterator object
# __next__() = returns the next values or raises StopIteration
#
# they're part of the "Iteration Protocol" of Python
# when we type next(iterator), python calls for iterator.__next__()


class Counter:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 3:
            raise StopIteration

        value = self.current
        self.current += 1 
        return value

counter = Counter()

for number in counter:
    print(number)
