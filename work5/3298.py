'''BUU'''
def main():
    '''BUU'''
    text = input()
    if 'BUU' in text.upper():
        count = 0
        count_max = 0
        for i in text:
            if i in{'U','u'}:
                count += 1
            else:
                count = 0
            count_max = max(count_max,count)
        print(f'Yes {count_max}')
    elif 'B' in text.upper():
        idx = text.upper().find('B')
        new = text[:idx +1] + ('U'*(len(text)-idx-1))
        print(new)
    else:
        new =''
        for i in range(len(text)):
            if not i % 3:
                new += 'B'
            else:
                new += 'U'
        print(new)
main()
