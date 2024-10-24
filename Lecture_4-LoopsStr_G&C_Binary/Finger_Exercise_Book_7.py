n = int(input("Type an interger: "))
x = 0

for root in range(1, n):
    for pwr in range(2, 6):
        if n == root ** pwr:
            x += 1

if x >= 1:
    print("Nice")

else:
    print("Not nice")