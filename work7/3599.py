'''sum'''
def main():
    '''sum'''
    tar_num = int(input())
    sum_num = 0
    while True:
        num = int(input())
        if num == -1:
            break
        sum_num += num
        if sum_num == tar_num:
            break
    print(sum_num)
main()
