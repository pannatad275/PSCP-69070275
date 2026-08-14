'''sdw'''
G = int(input())
R = int(input())
if G < 1 or G > 6 or R < 1 or R > 6:
    ANS = 'Invalid'
elif G == R:
    ANS = 'Correct!'
else:
    ANS = 'Wrong!'
print(ANS)
