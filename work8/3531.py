'''MissingNumber'''
n = int(input())

given_numbers = []

while True:
    num = int(input())
    if not num:
        break
    given_numbers.append(num)

for i in range(1, n + 1):
    if i not in given_numbers:
        print(i)
