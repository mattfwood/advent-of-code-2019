from part1 import calculate_fuel, values


def total_fuel(mass):
    total = 0
    remaining_mass = mass

    # scary loop
    while True:
        # get fuel for remaining mass
        fuel = calculate_fuel(remaining_mass)

        # if the fuel required would be 0 or less, break
        if fuel < 1:
            break

        # add fuel to total
        total += fuel
        # update remaining mass to fuel value
        remaining_mass = fuel

    return total


total = 0
for value in values:
    total += total_fuel(value)

print(total)
