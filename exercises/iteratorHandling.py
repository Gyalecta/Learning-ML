measurements = [12, 18, 24, 30]

iterator = iter(measurements)

print(f"First measurement: {next(iterator)}")

print("Remaining measurements: ")
for x in iterator:
    print(x)


print("Second iteration: ")
first_remaining = next(iterator, None)
if first_remaining is None:
    print("No elements remaining")
else:
    print(first_remaining)

iterator2 = iter(measurements)

print(f"New iterator first value: {next(iterator2)}")
