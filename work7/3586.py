'''kabata'''
def main():
    '''kabata'''
    n = int(input())
    for _ in range(n):
        text = input()
        if 'baka' in text:
            print('no')
            continue
        count = 0
        while count < len(text):
            if text.startswith("bakka", count):
                count += 5
            elif text.startswith("ka", count):
                count += 2
            elif text.startswith("ba", count):
                count += 2
            elif text.startswith("ta", count):
                count += 2
            else:
                break
        if count == len(text):
            print("yes")
        else:
            print('no')
main()
