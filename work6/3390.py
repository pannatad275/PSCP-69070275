'''2D'''
def main():
    '''2D'''
    matrix = []
    for _ in range(5):
        row = list(map(int, input().split()))
        matrix.append(row)
    wrong_row = -1
    wrong_col = -1
    for r in range(5):
        if sum(matrix[r]) % 2:
            wrong_row = r
    for c in range(5):
        col_sum = sum(matrix[r][c] for r in range(5))
        if col_sum % 2:
            wrong_col = c
    print(f"{wrong_row} {wrong_col}")
main()
