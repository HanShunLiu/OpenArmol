import math

car_pos = [[0.0, 0.0]] # List of all cartesional positions
pol_pos = [[0.0, 0.0]] # List of all polar positions

car_list = [[1.0, 2.0], [4.0, 6.0], [-1.0, 3.0]] # List of all additional positions in cartesional

# Convert cartensional cords to polar
def car_to_pol(x, y):
    r = math.sqrt((x**2) + (y**2))
    t = math.atan(y/x)
    return [r, t]

# Print cartesional cords
def print_car(pos):
    s = ""
    for cord in pos:
        s += ("(" + str(cord[0]) + ", " + str(cord[1]) + "), ")
    print(s)

# Print polar cords in cartesional form
def print_pol(pos):
    s = ""
    for cord in pos:
        s += ("(" + str(cord[0] * math.cos(cord[1])) + ", " + str(cord[0] * math.sin(cord[1])) + "), ")
    print(s)

# Add positions to both lists
for pos in car_list:
    car_pos.append(pos)
    pol_pos.append(car_to_pol(pos[0], pos[1]))

print_car(car_pos)
print_pol(pol_pos)
