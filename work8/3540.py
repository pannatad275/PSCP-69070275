'''num'''
text = input().strip()
words = text.split()

word_to_num = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
}

total_sum = 0
current_num = 0

for w in words:
    if w in word_to_num:
        current_num = current_num + word_to_num[w]
    elif w == "hundred":
        current_num = current_num * 100
    elif w == "thousand":
        current_num = current_num * 1000
        total_sum = total_sum + current_num
        current_num = 0
total_sum = total_sum + current_num
print(total_sum)
