y = 0

for i in range(10):
        x = int(input("Type a number: "))
        if x % 2 != 0 and x > y:
              y = x

if y == 0:
    print("You only typed even numbers!")
else:
     print(y)