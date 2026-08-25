'''code'''
def main():
    '''code'''
    text = input()
    letters = 0
    digits = 0
    code = ''
    in_dash = False
    for i in text:
        if i.isalpha():
            letters += 1
            code += i.upper()
            in_dash = False
        elif i.isdigit():
            digits += 1
            code += i
            in_dash = False
        else:
            if not in_dash:
                code += '-'
                in_dash = True
    code = code.strip('-')
    if not code:
        code = 'NONE'
    print("CODE =", code)
    print("LETTERS =", letters)
    print("DIGITS =", digits)
main()
