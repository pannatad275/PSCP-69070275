'''ticket'''
def main():
    '''ticket'''
    age = int(input())
    role = input()
    if age < 18 or role in ["s", "S"]:
        print(20)
    else:
        print(50)
main()
