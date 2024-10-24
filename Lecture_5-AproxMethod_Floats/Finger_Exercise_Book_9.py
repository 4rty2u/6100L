# Figure 3-5

x = 25

epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, x)
ans = (high + low)/2
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', 'ans =', ans)
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('number of guesses =', num_guesses)
print(ans, 'is close to square root of', x)

# The while loop will not be terminated because -(-x) will sum with ans to infinite and never lower than epsilon (0.01)