'''cutecat'''
cats = {"Garfield": "Cat01"}
foxes = {"Fubuki": "Fox01"}

n = int(input())

for _ in range(n):
    line = input().strip()
    data = eval(line)
    for name, code in data.items():
        if "Cat" in code:
            cats.update({name: code})
        elif "Fox" in code:
            foxes.update({name: code})

print("Cat :", str(len(cats)))
print("Fox :", str(len(foxes)))

sorted_cats = sorted(cats.items(), key=lambda x: x[1])
for name, code in sorted_cats:
    print(name + " : " + code)

sorted_foxes = sorted(foxes.items(), key=lambda x: x[1])
for name, code in sorted_foxes:
    print(name + " : " + code)
