# Test if an int > 2 is prime. If not, not print smallest divisor
x = int(input('Enter a integer greater than 2: '))
smallest_divisor=None
greatest_divisor=None
for guess in range(2, x):
    if x % guess == 0 and guess < x:
        greatest_divisor = guess

if greatest_divisor != None:
    print("Greatest divisor of", x, "is", greatest_divisor)
else:
    print(x, 'is a prime number')