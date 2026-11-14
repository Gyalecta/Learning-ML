temperatures = [21.5, 22.0, 19.8, 25.3, 23.1]

if len(temperatures) == 0:
    raise ValueError("The list is empty")

def main():
    print(f"Number of recorded temperatures: {len(temperatures)}")

    print(f"Max temperature: {max(temperatures)}")
    print(f"Min temperature: {min(temperatures)}")

    average = sum(temperatures) / len(temperatures)
    print(f"Average temperature: {average}")

    filtered_temperatures = [x for x in temperatures if x > 22]
    print(f"temperatures above 22C: {filtered_temperatures}")

    first, *remaining = temperatures
    print(f"First temperature: {first}")
    print(f"Remaining temperatures: {remaining}")

main()
