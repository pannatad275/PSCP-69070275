'''classify'''
counts = {}
while True:
    line = input().strip()
    if line == "END":
        break
    year = line[:2]
    faculty = int(line[2:4])

    key = (year, faculty)
    counts[key] = counts.get(key, 0) + 1

all_years = sorted(list(set(y for y, f in counts)))

for year in all_years:
    faculties = sorted([f for y, f in counts if y == year])
    for i, fac in enumerate(faculties):
        cnt = counts[(year, fac)]
        if not i:
            print(f"{year} {fac} {cnt}")
        else:
            print(f"-- {fac} {cnt}")
