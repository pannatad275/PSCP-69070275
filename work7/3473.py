'''fourdirections'''
patterns = {
    'U': [
        "  *  ",
        " *** ",
        "* * *",
        "  *  ",
        "  *  "
    ],
    'D': [
        "  *  ",
        "  *  ",
        "* * *",
        " *** ",
        "  *  "
    ],
    'L': [
        "  *  ",
        " *   ",
        "*****",
        " *   ",
        "  *  "
    ],
    'R': [
        "  *  ",
        "   * ",
        "*****",
        "   * ",
        "  *  "
    ]
}
commands = input().strip()

for row in range(5):
    line_parts = []
    for cmd in commands:
        if cmd in patterns:
            line_parts.append(patterns[cmd][row])
    print(" ".join(line_parts))
