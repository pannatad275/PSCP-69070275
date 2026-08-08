'''conan'''
def main():
    '''conan'''
    word = input()
    n = int(input())
    al = []
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in word:
        if 'a' <= i <= 'z':
            p = abc.find(i)
    print(p)
            
main()