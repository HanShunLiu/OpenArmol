import movement_test as mt
import math

# Testing Code
lis = [[-0.5, 0, 0], [-0.5, 0, 1], [-0.5, 1, 1], [-0.5, 1, 0],
       [0.5, 0, 0], [0.5, 0, 1], [0.5, 1, 1], [0.5, 1, 0], [0, 0, 0]]
for x in lis:
    ang = mt.calc_arm_ang(x[0], x[1], x[2])
    pos = mt.calc_arm_pos(ang)

    new_cord = []
    for y in pos:
        z = mt.cyl_to_car(y[0], ang[0], y[1])
        new_cord.append([round(z[0],3), round(z[1],3), round(z[2],3)])

    stri = ""
    for i in range(4):
        stri += "("
        for j in range(3):
            stri += str(new_cord[i][j])
            if j < 2:
                stri += ", "
        stri += ")"
        if i < 3:
            stri += ", "
    print(stri)


    for i in range(1, 4):
        dis = math.sqrt(((new_cord[i][0] - new_cord[i-1][0])**2) +
                        ((new_cord[i][1] - new_cord[i-1][1])**2) +
                        ((new_cord[i][2] - new_cord[i-1][2])**2))
        print(round(dis, 3))
