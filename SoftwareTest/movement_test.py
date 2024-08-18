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
    if y >= 0:
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
def calc_arm_ang(x, y, z):
    r, t = car_to_pol(x, y)  # Turn cartersional to polar cords

    # Calculate target information
    target_ang = math.pi / 2  # Default value if r == 0
    if r != 0.0:
        target_ang = math.atan(z/r)  # Angle above table of the target
    target_len = calc_len([0, 0], [r, z])  # Length from base to target

    # Set base rotater's angle
    arm0_ang = t

    # Calculate first hinge's angle
    arm1_ang = (3 * math.pi) / 4  # Default angle
    arm1_pos = [arm_len[1] * math.cos(arm1_ang), arm_len[1] * math.sin(arm1_ang)]
    hinge1_target_len = calc_len([r, z], arm1_pos)
    # Ensure arm can reach target
    while hinge1_target_len > (arm_len[2] + arm_len[3]):
        arm1_ang -= (arm1_ang - target_ang) * 0.1
        arm1_pos = [arm_len[1] * math.cos(arm1_ang), arm_len[1] * math.sin(arm1_ang)]
        hinge1_target_len = calc_len([r, z], arm1_pos)

    # Calculate second hinge's angle
    arm2_ang = calc_ang(target_len, arm_len[1], hinge1_target_len) + calc_ang(arm_len[3], arm_len[2], hinge1_target_len)

    # Calculate third hinge's angle
    arm3_ang = calc_ang(hinge1_target_len, arm_len[2], arm_len[3])

    # Calculate fourth hinge's angle
    arm4_ang = (3 * math.pi) - arm1_ang - arm2_ang - arm3_ang

    # Calculate hand rotater's angle
    arm5_ang = math.pi - arm0_ang

    return [arm0_ang, arm1_ang, arm2_ang, arm3_ang, arm4_ang, arm5_ang]

def calc_arm_pos(ang_lis):

    # Set base rotater's position
    arm0_pos = [0.0, 0.0]

    # Calculate first hinge's position
    arm1_pos = [arm_len[1] * math.cos(ang_lis[1]),
                arm_len[1] * math.sin(ang_lis[1])]

    # Calculate second hinge's position
    arm2_pos = [arm1_pos[0] + arm_len[2] * math.cos(ang_lis[1] + ang_lis[2] - math.pi),
                arm1_pos[1] + arm_len[2] * math.sin(ang_lis[1] + ang_lis[2] - math.pi)]

    # Calculate third hinge's position
    arm3_pos = [arm2_pos[0] + arm_len[3] * math.cos(ang_lis[1] + ang_lis[2] + ang_lis[3] - (2 * math.pi)),
                arm2_pos[1] + arm_len[3] * math.sin(ang_lis[1] + ang_lis[2] + ang_lis[3] - (2 * math.pi))]

    # Set fourth hinge's position
    arm4_pos = [arm3_pos[0], arm3_pos[1]]

    # Set hand rotater's position
    arm5_pos = [arm4_pos[0], arm4_pos[1]]

    return [arm0_pos, arm1_pos, arm2_pos, arm3_pos, arm4_pos, arm5_pos]

# Returns a list of angles and positions
def arm_move_lis(target, step):
    pass
