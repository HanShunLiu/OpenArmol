import movement_test as mt

# Testing Code
x1, x2 = mt.calc_arm_pos(0.5, 0.5, 0.5)
new_cord = []
for y in x2:
    z = mt.cyl_to_car(y[0], x1[0], y[1])
    new_cord.append(z)
print(new_cord[-1])
for i in range(1, 4):
    dis = mt.calc_len_3d(new_cord[i-1], new_cord[i])
    print(dis)