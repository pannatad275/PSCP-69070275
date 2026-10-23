'''align'''
size = int(input())
align = input().strip()
text = input()
padding = size - len(text)
result = text
if align == "left":
    result = text + (" " * padding)
elif align == "right":
    result = (" " * padding) + text
elif align == "center":
    left_spaces = (padding + 1) // 2
    right_spaces = padding // 2
    result = (" " * left_spaces) + text + (" " * right_spaces)
print(result)
