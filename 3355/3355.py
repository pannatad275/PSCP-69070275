'''shorten'''
nums = []

while True:
    n = int(input())
    if n == -1:
        break
    nums.append(n)

if len(nums) > 0:
    ans = ""
    start = nums[0]
    prev = nums[0]

    for i in range(1, len(nums)):
        curr = nums[i]
        if curr == prev + 1:
            prev = curr
        else:
            if len(ans) > 0:
                ans += ", "
            if start == prev:
                ans += str(start)
            else:
                ans += str(start) + "-" + str(prev)
            start = curr
            prev = curr
    if len(ans) > 0:
        ans += ", "
    if start == prev:
        ans += str(start)
    else:
        ans += str(start) + "-" + str(prev)

    print(ans)
