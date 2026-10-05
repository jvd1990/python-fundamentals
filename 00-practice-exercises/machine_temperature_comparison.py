temperatures = {
    "M1": 72,
    "M2": 85,
    "M3": 64,
    "M4": 91,
    "M5": 78,
}

average_temperature = sum(temperatures.values()) / len(temperatures)
print(f"Average temperature: {average_temperature:.1f}\n")

above_average = []
below_average = []
equal_to_average = []

for machine, temperature in temperatures.items():
    if temperature > average_temperature:
        above_average.append(machine)
        print(f"{machine}: {temperature} — above average")
    elif temperature < average_temperature:
        below_average.append(machine)
        print(f"{machine}: {temperature} — below average")
    else:
        equal_to_average.append(machine)
        print(f"{machine}: {temperature} — equal to average")

print(f"\nAbove average ({len(above_average)}): {above_average}")
print(f"Below average ({len(below_average)}): {below_average}")
print(f"Equal to average ({len(equal_to_average)}): {equal_to_average}")