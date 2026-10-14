'''dict'''
def main():
    '''dict'''
    text = input()
    order = []
    for i in range(26):
        order.append(chr(ord("a") + i))
        order.append(chr(ord("A") + i))


    for char in order:
        count = text.count(char)
        if count > 0:
            print(f"{char} = {count}")
main()
