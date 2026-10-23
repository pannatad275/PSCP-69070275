'''store'''
stock = {}

while True:
    line = input().strip()
    if line == "END":
        break

    parts = line.split()
    cmd = parts[0]

    if cmd == "ADD":
        name = parts[1]
        qty = int(parts[2])
        stock[name] = stock.get(name, 0) + qty

    elif cmd == "REMOVE":
        name = parts[1]
        qty = int(parts[2])
        current_qty = stock.get(name, 0)

        if current_qty >= qty:
            stock[name] -= qty
        else:
            stock[name] = 0
            print(f"Not enough stock for {name}")

    elif cmd == "CHECK":
        low_stock = [name for name, qty in stock.items() if qty < 5]
        if low_stock:
            for name in sorted(low_stock):
                print(name)
        else:
            print("All stocks are sufficient")
    elif cmd == "REPORT":
        for name in sorted(stock.keys()):
            print(f"{name}: {stock[name]}")
