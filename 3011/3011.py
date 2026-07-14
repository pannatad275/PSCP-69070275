'''colour'''
c1 = input()
c2 = input()

if (c1 == "Red") and (c2 == "Yellow"):
    print("Orange")
elif (c1 == "Yellow") and (c2 == "Red"):
    print("Orange")
elif (c1 == "Red") and (c2 == "Blue"):
    print("Violet")
elif (c1 == "Blue") and (c2 == "Red"):
    print("Violet")
elif (c1 == "Yellow") and (c2 == "Blue"):
    print("Green")
elif (c1 == "Blue") and (c2 == "Yellow"):
    print("Green")
else:
    print("Error")
