'''regtangle'''
Xa, Ya, Wa, Ha = map(int, input().split())
Xb, Yb, Wb, Hb = map(int, input().split())

Xa1 = Xa
Xa2 = Xa + Wa
Ya1 = Ya
Ya2 = Ya + Ha

Xb1 = Xb
Xb2 = Xb + Wb
Yb1 = Yb
Yb2 = Yb + Hb

overlapping1 = min(Xa2, Xb2)
overlapping2 = max(Xa1, Xb1)

overlapping3 = min(Ya2, Yb2)
overlapping4 = max(Ya1, Yb1)

overlap1 = overlapping1 - overlapping2
overlap2 = overlapping3 - overlapping4

if overlap1 > 0 and overlap2 > 0:
    area = overlap1 * overlap2
    print(area)
else:
    print("no overlapping")
