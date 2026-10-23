'''calv2'''
n = int(input())
if n == 1:
    print(1)
else:
    digits_count = 0
    length = 1
    start = 1
    while start <= n:
        end = min(n, start * 10 - 1)
        count_in_range = end - start + 1
        digits_count += count_in_range * length
        start *= 10
        length += 1
    total_presses = digits_count + (n - 1) + 1
    print(total_presses)
