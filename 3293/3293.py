'''bigframe'''
def main():
    '''bigframe'''
    texts = []
    for _ in range(5):
        text = input()
        texts.append(text)
    max_len = 0
    for text in texts:
        if len(text) > max_len:
            max_len = len(text)
    inner_width = max(max_len + 2,2)
    print('*' * (inner_width + 2))
    for text in texts:
        space = inner_width - 1 - len(text)
        print('* '+text+(' '*space) +'*')
    print('*' * (inner_width + 2))
main()
