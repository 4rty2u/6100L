a = 2
b = 5
c = 7

answer = min(a, b, c)
if a % 2 != 0 and a == answer:
    print(a)
else:
    answer = min(b, c)
    if b % 2 != 0 and b == answer:
        print(b)
    else:
        print(c)