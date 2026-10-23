'''horizon'''
text = input()
A = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char in A:
    count = text.count(char)

    if count > 0:
        graph = ""
        for i in range(1, count + 1):
            graph += "-"
            if not i % 5 and i != count:
                graph += "|"
        print(char + " : " + graph)
