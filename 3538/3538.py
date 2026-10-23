'''B-fully'''
text = input().strip()
counts = {}
first_seen = []

for char in text:
    if char in counts:
        counts[char] = counts[char] + 1
    else:
        counts[char] = 1
        first_seen.append(char)
unpaired = []
for char in first_seen:
    if counts[char] % 2:
        unpaired.append(char)
if not unpaired:
    print("fully paired")
else:
    print("".join(unpaired))
