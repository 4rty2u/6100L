low = 0
high = 100
episolon = 0
num = 13
count = 0

guess = (high + low) / 2
count += 1

while abs(guess - num) > episolon:

    if guess < num:
        low = guess
    else:
        high = guess
    
    guess = round(high + low)/2

    count += 1

print(count)
print(guess)