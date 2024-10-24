N = 4
Perfect_Cube = False

for i in range(1, 16):
    if i**2 == N:
        Perfect_Cube = True
        break

if Perfect_Cube == True:
    print("It's a perfect cube!")
else:
    print("Is not a perfect cube!")