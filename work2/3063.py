'''BANK'''
Password = input()
Passwordnumber = input()

if Password == "H" and Passwordnumber == "4567":
    print("safe unlocked")
elif Password == "H" and Passwordnumber != "4567":
    print("safe locked - change digit")
elif Password != "H" and Passwordnumber == "4567":
    print("safe locked - change char")
else:
    print("safe locked")
