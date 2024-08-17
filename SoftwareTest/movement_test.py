import copy
import math

# Arm angle and data
# Base rotater, first hinge, second second, third hinge, fourth hinge, hand rotater
arm_len = [0.0, 0.75, 0.5, 0.5, 0.0, 0.0]
arm_ang = [math.pi/2, math.pi/2, math.pi, math.pi, math.pi, 0.0]
arm_pos = [[0.0, 0.0],
           [0.0, arm_len[1]],
           [0.0, arm_len[1] + arm_len[2]],
           [0.0, arm_len[1] + arm_len[2] + arm_len[3]],
           [0.0, arm_len[1] + arm_len[2] + arm_len[3]],
           [0.0, arm_len[1] + arm_len[2] + arm_len[3]]]

# Convert cartesian cords to polar
def car_to_pol(x, y):
    r = math.sqrt((x**2) + (y**2))
    t = 0.0  # Default value if y and x == 0

    # 90 or 270 degrees if y != 0 and x == 0
    if y > 0:
        t = math.pi / 2
    elif y < 0:
        t = (3 * math.pi) / 2

    # Prevent divide by zero error
    if x > 0:
        t = math.atan(y/x)
    elif x < 0:
        t = math.atan(y/x) + math.pi

    return r, t

# Convert cylindrical cords to cartesian
def cyl_to_car(r, t, z):
    x = r * math.cos(t)
    y = r * math.sin(t)
    return [x, y, z]

# Calculate length of line segment between 2 points
def calc_len(p1, p2):
    return math.sqrt(((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2))

def calc_len_3d(p1, p2):
    return math.sqrt(((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2) + ((p2[2] - p1[2])**2))

# Calculate angle using Cosine Rule
def calc_ang(a, b, c):
    num = (-1 * a**2) + b**2 + c**2
    den = 2 * b * c
    return math.acos(num/den)

# Returns the position of the end points of each segment of the arm in cartesian format
def car_pos():
    pos = []
    for p in arm_pos:
        pos.append(cyl_to_car(p[0], arm_ang[0], p[1]))
    return pos

# Calculate the arm angle and positions to reach cartesian cords (x,y,z)
def calc_arm_pos(x, y, z):
    new_ang = copy.deepcopy(arm_ang)  # Copy all arm angles
    new_pos = copy.deepcopy(arm_pos)  # Copy all arm positions

    r, t = car_to_pol(x, y)  # Turn cartersional to polar cords

    target_ang = math.pi / 2  # Default value if r == 0
    if r != 0.0:
        target_ang = math.atan(z/r)  # Angle above table of the target
    target_len = calc_len([0, 0], [r, z])  # Length from base to target

    # Update base rotater's angle, position remains constant
    new_ang[0] = t

    # Update first hinge's angle and position
    new_ang[1] = (3 * math.pi) / 4
    new_pos[1] = [arm_len[1] * math.cos(new_ang[1]), arm_len[1] * math.sin(new_ang[1])]
    hinge1_target_len = calc_len([r, z], new_pos[1])
    # Ensure arm can reach target
    while hinge1_target_len > (arm_len[2] + arm_len[3]):
 #       print("1: " + str((new_ang[1] - target_ang) * 0.1))
  #      print("2: " + str(hinge1_target_len))
   #     print("3: " + str(arm_len[2] + arm_len[3]))
    #    print("4: " + str(new_ang[1]))
     #   print("5: " + str(target_ang))
        new_ang[1] -= (new_ang[1] - target_ang) * 0.1
        new_pos[1] = [arm_len[1] * math.cos(new_ang[1]), arm_len[1] * math.sin(new_ang[1])]
        hinge1_target_len = calc_len([r, z], new_pos[1])

    # Update second hinge's angle and position
    new_ang[2] = calc_ang(target_len, arm_len[1], hinge1_target_len) + calc_ang(arm_len[3], arm_len[2], hinge1_target_len)
    new_pos[2] = [new_pos[1][0] + arm_len[2] * math.cos(new_ang[1] + new_ang[2] - math.pi),
                  new_pos[1][1] + arm_len[2] * math.sin(new_ang[1] + new_ang[2] - math.pi)]

    # Update third hinge's angle and position
    new_ang[3] = calc_ang(hinge1_target_len, arm_len[2], arm_len[3])
    new_pos[3] = [new_pos[2][0] + arm_len[3] * math.cos(new_ang[1] + new_ang[2] + new_ang[3] - (2 * math.pi)),
                  new_pos[2][1] + arm_len[3] * math.sin(new_ang[1] + new_ang[2] + new_ang[3] - (2 * math.pi))]

    # Update fourth hinge's angle and positon
    new_ang[4] = (3 * math.pi) - new_ang[1] - new_ang[2] - new_ang[3]
    new_pos[4] = new_pos[3]

    # Update hand rotater's angle and position
    new_ang[5] = math.pi - new_ang[0]
    new_pos[5] = new_pos[4]

    return new_ang, new_pos
