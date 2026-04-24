# Task 1: Implement the Factors 

# A-B
def phi1(a, b):

    if a == b:
        return 4
    else:
        return 2

# B-C
def phi2(b, c):

    if b == c:
        return 5
    else:
        return 1

# C-A
def phi3(c, a):

    if c == a:
        return 3
    else:
        return 1

# Task 2: Construct the Joint Distribution (Unnormalized)
def all_comp(a, b, c):
    joint_dist = {}
    for val_a in a:
        for val_b in b:
            for val_c in c:
                prob = phi1(val_a, val_b) * phi2(val_b, val_c) * phi3(val_c, val_a)
                joint_dist[(val_a, val_b, val_c)] = prob
    return joint_dist
