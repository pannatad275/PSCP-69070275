'''rabbit'''
word = input().strip().upper()
n = len(word)

if all(ch in ('I', 'T') for ch in word):
    print(f"unknown {n}")
else:
    is_valid = True
    first_error_index = -1
    i = 0
    while i < n:
        ch = word[i]
        if ch not in ('R', 'A', 'B', 'I', 'T'):
            is_valid = False
            first_error_index = i
            break
        if ch == 'R':
            if i + 1 < n and word[i + 1] == 'A':
                pass
            else:
                is_valid = False
                first_error_index = i + 1 if i + 1 < n else i
                break
        elif ch == 'A':
            if not i or word[i - 1] not in ('R', 'A'):
                is_valid = False
                first_error_index = i
                break
        elif ch == 'B':
            if i + 1 < n and word[i + 1] in ('I', 'T'):
                pass
            else:
                is_valid = False
                first_error_index = i + 1 if i + 1 < n else i
                break
        i += 1

    if is_valid:
        max_a = 0
        current_a = 0
        for ch in word:
            if ch == 'A':
                current_a += 1
                if current_a > max_a:
                    max_a = current_a
            else:
                current_a = 0
        print(f"yes {max_a}")
    else:
        print(f"no {first_error_index}")
