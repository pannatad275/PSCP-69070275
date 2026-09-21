'''lan rab'''
def main():
    '''lan rab'''
    text = input().upper()
    n = len(text)

    for i in range(n):
        if text[i] not in 'RABIT':
            print(f'no {i}')
            return

    for i in range(n):
        if text[i] == 'R':
            if i + 1 >= n or text[i + 1] != 'A':
                print(f'no {i}')
                return
        elif text[i] == 'B':
            if i + 1 >= n or (text[i + 1] != 'I' and text[i + 1] != 'T'):
                print(f"no {i}")
                return
        elif text[i] == 'A':
            if i == 0 or (text[i - 1] != 'R' and text[i - 1] != 'A'):
                print(f"no {i}")
                return

    only_it = True
    for char in text:
        if char != 'I' and char != 'T':
            only_it = False
            break

    if only_it:
        print(f"unknown {n}")
        return

    max_a = 0
    current_a = 0
    for char in text:
        if char == 'A':
            current_a += 1
            if current_a > max_a:
                max_a = current_a
        else:
            current_a = 0

    print(f"yes {max_a}")
main()
