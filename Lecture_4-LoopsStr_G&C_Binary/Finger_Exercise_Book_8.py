q = 0
total = 0

for i in range(3, 1000, 2):

    q = 0

    for j in range(1, i+1):
        if i % j == 0:
            q += 1
    
    if q == 2:
        print(i)
        total += i

print(total)