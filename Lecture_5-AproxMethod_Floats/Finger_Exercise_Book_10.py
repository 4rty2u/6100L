# figure 3-5

x = -25

epsilon = 0.01
num_guesses = 0
low = min(0, x)
high = max(0, x)
print(low)
print(high)
ans = (high + low)/2
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('number of guesses =', num_guesses)
print(ans, 'is close to square root of', x)