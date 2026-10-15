'''fourdirections'''
word = input()

for row in range(5):
    line = ""
    for i in range(len(word)):
        ch = word[i]

        if i > 0:
            line += " "

        if ch == 'U':
            if row == 0: line += "  *  "
            elif row == 1: line += " *** "
            elif row == 2: line += "* * *"
            elif row == 3: line += "  *  "
            elif row == 4: line += "  *  "
        elif ch == 'D':
            if row == 0: line += "  *  "
            elif row == 1: line += "  *  "
            elif row == 2: line += "* * *"
            elif row == 3: line += " *** "
            elif row == 4: line += "  *  "
        elif ch == 'L':
            if row == 0: line += "  *  "
            elif row == 1: line += " *   "
            elif row == 2: line += "*****"
            elif row == 3: line += " *   "
            elif row == 4: line += "  *  "
        elif ch == 'R':
            if row == 0: line += "  *  "
            elif row == 1: line += "   * "
            elif row == 2: line += "*****"
            elif row == 3: line += "   * "
            elif row == 4: line += "  *  "
            
    print(line)
