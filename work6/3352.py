'''laststand'''
def main():
    '''laststand'''
    n = input()
    num = n[1:-1].split(',')
    #print(num)
    for i in num:
        ste = i.strip()
        print(ste[-1])
main()
