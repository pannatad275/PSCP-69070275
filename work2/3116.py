'''school'''
def main():
    '''school'''
    name = input()
    len_name = len(name)
    u_name = name.upper()
    first_l = u_name[0]
    last_l = u_name[-1]
    ascii_first = ord(first_l)
    ascii_last = ord(last_l)
    s = [0,1,2,3,4,5,6,7,8,9]
    result = []
    for i in range(1, 11):
        val = s[i - 1]
        if i % 2:
            val = val + ascii_first
        else:
            val = val - ascii_last

        val = abs(val) % len_name
        if val > 9:
            val = val % 10
        result.append(val)
    ans = " ".join(map(str,result[2:8]))
    print(ans)
main()
