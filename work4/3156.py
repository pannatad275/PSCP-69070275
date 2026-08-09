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
            new_p = (p + n) % 26
            al.append(abc[new_p])
    print("".join(al))
main()
