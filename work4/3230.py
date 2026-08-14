'''pas'''
pw = input()
if int(pw[0]) > 5:
    PAS = 9
elif int(pw[1]) > 5:
    PAS = 10
elif int(pw[2]) > 5:
    PAS = 11
elif int(pw[3]) > 5:
    PAS = 12
elif int(pw[4]) > 5:
    PAS = 14
else:
    PAS = 13

if pw == pw[::-1]:
    if int(pw[0]) + int(pw[4]) > 5:
        PAS2 = 1
    elif int(pw[1]) * int(pw[3]) > 5:
        PAS2 = 2
    else:
        PAS2 = 0
else:
    if int(pw[4]) and int(pw[0]) // int(pw[4]) > 5:
        PAS2 = 1
    elif int(pw[1]) - int(pw[4]) > 5:
        PAS2 = 2
    else:
        PAS2 = 0
if int(pw[0]) + int(pw[1]) + int(pw[2]) + int(pw[3]) + int(pw[4]) > 25:
    PAS3 = 1
elif int(pw[0]) * int(pw[1]) * int(pw[2]) * int(pw[3]) * int(pw[4]) > 55:
    PAS3 = 2
else:
    PAS3 = 0
print(str(PAS)+str(PAS2)+str(PAS3))
