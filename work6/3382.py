'''back'''
def main():
    '''ward'''
    list1 = []
    while True:
        text = input()
        if text == 'NULL':
            break
        list1.append(text)
    for i in reversed(list1):
        print(i)
main()
