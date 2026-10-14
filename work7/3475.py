'''menu'''
menu = []
while True:
    line = input().strip()

    if line == "DONE":
        break

    if line == "CLOSED":
        menu.clear()
        break

    if line == "SOMETHING'S WRONG":
        menu.clear()

    elif line.startswith("Can't do: "):
        dish_to_remove = line.replace("Can't do: ", "").strip()
        if dish_to_remove in menu:
            menu.remove(dish_to_remove)

    elif " #" in line:
        dish, pos = line.split(" #")
        if pos == "N":
            menu.append(dish)
        else:
            index = int(pos) - 1
            menu.insert(index, dish)
print(f"Full Course: {menu} Reversed: {menu[::-1]}")
