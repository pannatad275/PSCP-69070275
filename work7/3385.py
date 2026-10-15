"""bus1"""
p = int(input())
n = int(input())

bus = []
total_dropped = 0

for _ in range(n):
    line = input()
    while line.strip() == "":
        line = input()
        
    data = list(map(int, line.split()))
    current_stop = data[0]
    passengers = data[1:]
    remaining_bus = []
    for dest in bus:
        if dest == current_stop:
            total_dropped += 1
        else:
            remaining_bus.append(dest)
    bus = remaining_bus
    for dest in passengers:
        if dest > current_stop and len(bus) < p:
            bus.append(dest)

print(total_dropped)
