'''hint'''
def main():
    '''hint'''
    sign1,num1 = input().split()
    sign2,num2 = input().split()
    sign3,num3 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    for i in range(10):
        for j in range(10):
            for h in range(10):
                if eval(f'{i} {sign1} {num1}') and eval(f'{j} {sign2} {num2}') and eval(f'{h} {sign3} {num3}'):
                    print(f'{h}{j}{i}')
main()
