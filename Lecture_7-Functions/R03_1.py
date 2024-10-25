
x = float(36)
epsilon =  0.0000000001
low = min(0, x)
high = max(0, x)
guess = (low + high)/2

while ((guess**4 - x) >= epsilon):

    if guess**4 < x:
        low = guess
    else:
        high = guess

    guess = (low + high)/2
    print(guess)

print(guess)