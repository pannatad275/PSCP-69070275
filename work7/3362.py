'''buppe'''
name1 = input()
name2 = input()
len1 = len(name1)
len2 = len(name2)
if len1 < len2:
    diff = len2 - len1
    name1 += (name1 * (diff // len1 + 1))[:diff]
elif len2 < len1:
    diff = len1 - len2
    name2 += (name2 * (diff // len2 + 1))[:diff]
charm = []
love_chars = {'l', 'o', 'v', 'e'}
for i, char1 in enumerate(name1):
    c1 = char1.lower()
    c2 = name2[i].lower()
    if c1 in love_chars or c2 in love_chars:
        charm.append('w')
    else:
        charm.append('$')

charm_str = "".join(charm)
W = charm_str.count('w')
if W % 2:
    max_consecutive_w = 0
    current_w = 0
    for char in charm_str:
        if char == 'w':
            current_w += 1
            if current_w > max_consecutive_w:
                max_consecutive_w = current_w
        else:
            current_w = 0
    charm_str += str(max_consecutive_w)
else:
    if 'ww' not in charm_str:
        charm_str += '#'
print(charm_str)
