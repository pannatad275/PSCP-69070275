'''colour'''
c1 = input()
c2 = input()

if c1 == c2:
    print(c1)
elif (c1 == "Red" and c2 == "Yellow") or (c1 == "Yellow" and c2 == "Red"):
    print("Orange")
elif (c1 == "Red" and c2 == "Blue") or (c1 == "Blue" and c2 == "Red"):
    print("Violet")
elif (c1 == "Blue" and c2 == "Yellow") or (c1 == "Yellow" and c2 == "Blue"):
    print("Green")
else:
    print("Error")
    