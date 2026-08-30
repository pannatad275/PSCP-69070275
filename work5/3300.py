'''life'''
def main():
    '''life'''
    n = int(input())
    works = []
    hard = 0
    easy = 0
    for _ in range(n):
        work = int(input())
        works.append(work)
    for i in works:
        if i > 18:
            hard += 1
        else:
            easy += 1
    if easy >= hard:
        print(n)
    else:
        print(2 * hard -1)
main()
