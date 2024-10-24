k = 30
num = 0

epsilon = 0.001
guess = k/2
num += 1

while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k) / (2*guess))
    num += 1
print('Square root of', k, 'is about', guess)
print('The number off guesses:', num)

low = 0
high = k

num = 0
guess = (high + low)/2
num += 1

while abs(guess**2 - k) >= epsilon:
    if guess**2 < k:
        low = guess
    else:
        high = guess
    num += 1

    guess = (high + low)/2

print('')
print('Square root of', k, 'is about', guess)
print('The number off guesses:', num)


# The Newton algorithm is better than divide and conquer to found root of an equation!