'''aeiou'''
def main():
    '''aeiou'''
    name = input().lower()
    aeiou = [0,0,0,0,0]
    for i in name:
        if i == "a":
            aeiou[0] += 1
        elif i == "e":
            aeiou[1] += 1
        elif i == "i":
            aeiou[2] += 1
        elif i == "o":
            aeiou[3] += 1
        elif i == "u":
            aeiou[4] += 1

    if aeiou[0] > 0:
        print(f"a : {aeiou[0]}")
    if aeiou[1] > 0:
        print(f"e : {aeiou[1]}")
    if aeiou[2] > 0:
        print(f"i : {aeiou[2]}")
    if aeiou[3] > 0:
        print(f"o : {aeiou[3]}")
    if aeiou[4] > 0:
        print(f"u : {aeiou[4]}")
main()
