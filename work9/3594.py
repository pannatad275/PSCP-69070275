'''1132'''
data = input().split(", ")
numbers = [float(x) for x in data]
numbers.sort()
n = len(numbers)
if n % 2 == 1:
    median = numbers[n // 2]
else:
    mid1 = numbers[(n // 2) - 1]
    mid2 = numbers[n // 2]
    median = (mid1 + mid2) / 2
print(f"{median:.2f}")
