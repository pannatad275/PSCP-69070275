'''fourdirections'''
def main():
    '''fourdirections'''
    text = input()
    arrows = {
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
    for i in range(5):
        row = [arrows[c][i] for c in text]
        print(" ".join(row))
main()
