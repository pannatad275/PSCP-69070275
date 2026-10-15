'''hint'''
def check_condition(digit, op, target):
    '''hint'''
    if op == '==':
        return digit == target
    if op == '!=':
        return digit != target
    if op == '>':
        return digit > target
    if op == '>=':
        return digit >= target
    if op == '<':
        return digit < target
    if op == '<=':
        return digit <= target
    return False
op_u, num_u = input().split()
target_u = int(num_u)

op_s, num_s = input().split()
target_s = int(num_s)

op_r, num_r = input().split()
target_r = int(num_r)

for r in range(10):
    if check_condition(r, op_r, target_r):
        for s in range(10):
            if check_condition(s, op_s, target_s):
                for u in range(10):
                    if check_condition(u, op_u, target_u):
                        print(f"{r}{s}{u}")
