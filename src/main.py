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



# Task 3: Compute the Partition Function
def partition_function(joint_dist):
    Z = 0
    for prob in joint_dist.values():
        Z += prob
    return Z



#  Task 4:
def print_normalized_table(joint_dist, z):
    print("A  B  C | Unnormalized | Normalized P(A,B,C)")
    print("-" * 50)
    
    normalized_dist = {}
    for (a, b, c), unnorm_val in joint_dist.items():
        prob = unnorm_val / z
        normalized_dist[(a, b, c)] = prob
        print(f"A{a} B{b} C{c} |    {unnorm_val:2} / {z}    |    {prob:.4f}")
        
    return normalized_dist
values = [0, 1]
unnorm_results = all_comp(values, values, values)
z_val = partition_function(unnorm_results)
print(f"Partition Function Z = {z_val}\n")
normalized_results = print_normalized_table(unnorm_results, z_val)


# Task 5: General Probability Query Function
def query_prob(a, b, c, normalized_dist = normalized_results):
    if (a, b, c) in normalized_dist:
        return normalized_dist[(a, b, c)]
    else:
        return 0
    
# Example query
print("\nQuery P(A=1, B=1, C=1):")
print(query_prob(1, 1, 1))

print("\nQuery P(A=0, B=1, C=0):")
print(query_prob(0, 1, 0))
