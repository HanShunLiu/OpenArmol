import math

# Arm 1: First segment of arm, connected to base
arm1_len = 1.5
arm1_pos = [0.0, arm1_len]
arm1_ang = 90.0

# Arm 2: Second segment of arm, in the middle
arm2_len = 1.0
arm2_pos = [0.0, arm1_len + arm2_len]
arm2_ang = 90.0

# Arm 3: Third segment of arm, connected to hand
arm3_len = 1.0
arm3_pos = [0.0, arm1_len + arm2_len + arm3_len]
arm3_ang = 90.0

car_pos = [[0.0, 0.0]] # List of all cartesional positions
pol_pos = [[0.0, 0.0]] # List of all polar positions

# Convert cartensional cords to polar
def car_to_pol(x, y):
    r = math.sqrt((x**2) + (y**2))
    t = math.atan(y/x)
    return [r, t]

# Convert degrees to radians
def deg_to_rad(x):
    return (x * math.pi) / 180

def calc_len(p1, p2):
    return math.sqrt(((p2[0] - p1[1])**2) + ((p2[0] - p1[1])**2))

# Calculate angle of line segment from origin to (x, y)
# Uses angle between 2 vector formula, p2 is where p1 and p3 originate
def pos_to_ang(p1, p2, p3):
    vec1 = [p1[0] - p2[0], p1[1] - p2[1]]
    vec2 = [p3[0] - p2[0], p3[1] - p2[1]]
    return math.acos((vec1[0]*vec2[0] + vec1[1]*vec2[1]) / (calc_len([0, 0], vec1) * calc_len([0, 0], vec2)))

# Calculate position of line segment of length r at angle a
def ang_to_pos(r, a, init_pos, ang_comp):
    return [(r + ang_comp) * math.acos(a) + init_pos[0], (r + ang_comp) * math.asin(a) + init_pos[1]]

def calc_arm_pos(x, y):
    new_arm_pos = [[arm1_pos[0], arm1_pos[1]], [arm2_pos[0], arm2_pos[1]], [arm3_pos[0], arm3_pos[1]]]
    new_arm_ang = [arm1_ang, arm2_ang, arm3_ang]
    target_ang = pos_to_ang([0, 1], [0, 0], [x, y])

    # Calc arm1 position
    while calc_len([x, y], new_arm_pos[0]) > (arm2_len + arm3_len):
        new_arm_ang[0] = (target_ang + new_arm_ang[0]) / 2
        new_arm_pos[0] = ang_to_pos(arm3_len, new_arm_ang[0], [0, 0], 0)

    # TODO: Add logic to move arm2 and arm3
