import movement_test as mt

# Testing Code
lis = [[1, 1, 1], [-1, 1, 1], [1, -1, 1], [-1, -1, 1], [0, 1, 1], [1, 0, 1], [0, -1, 1], [-1, 0, 1]]
for x in lis:
    x1, x2 = mt.calc_arm_pos(x[0], x[1], x[2])
    new_cord = []
    for y in x2:
        z = mt.cyl_to_car(y[0], x1[0], y[1])
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
        dis = mt.calc_len_3d(new_cord[i-1], new_cord[i])
        print(round(dis, 3))
