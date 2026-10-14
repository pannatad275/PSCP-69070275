'''bus seat'''
def main():
    '''bus seat'''
    seat_row = int(input())
    num = int(input())
    kor = int(input())
    for pair_start in range(seat_row, 0, -2):
        for seat_pos in range(pair_start, pair_start - 2, -1):
            row_list = []
            for col in range(num):
                seat_num = col * seat_row + seat_pos
                if seat_num == kor:
                    row_list.append("XX")
                else:
                    row_list.append(f"{seat_num:02d}")
            print(" ".join(row_list))
        if pair_start - 2 > 0:
            print()
main()
