temperatures = [21.5, 22.0, 19.8, 25.3, 23.1]

filtered = (x for x in temperatures if x > 22)

print(f"First value: {next(filtered)}")

print(f"Remaining values: {list(filtered)}")

filtered_list = list(filtered)

print(f"After exhaustion: {filtered_list}")
