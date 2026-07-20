'''calculator'''
n = int(input())
if n == 1:
    print("1")
else:
    click = 0
    for i in range(1,n + 1):
        click += len(str(i)) #len นับตัวหนังสือของ i ที่เปลี่ยนเป็น str แล้ว
                                    # str เปลี่ยนตัวเลขจาก i เป็นข้อความให้ len นับได้
    total = click + n
    print(total)
    print(len(str(i)))
    