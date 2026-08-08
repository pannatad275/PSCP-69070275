'''fizz'''
def main():
    '''fiz'''
    n = int(input())
    for i in range(1,n+1):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 3:
            print("Fizz")
        elif not i % 5:
            print("Buzz")
        else:
            print(i)
main()
