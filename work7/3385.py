"""bus1"""
def main():
    """bus1"""
    capacity = int(input())
    num_stops = int(input())
    passengers_on_bus = []
    total_delivered = 0
    for _ in range(num_stops):
        line = list(map(int, input().split()))
        current_stop = line[0]
        waiting_passengers = line[1:]
        remaining_bus = []
        for dest in passengers_on_bus:
            if dest == current_stop:
                total_delivered += 1
            else:
                remaining_bus.append(dest)
        passengers_on_bus = remaining_bus
        for dest in waiting_passengers:
            if dest > current_stop:
                if len(passengers_on_bus) < capacity:
                    passengers_on_bus.append(dest)
    print(total_delivered)
main()
