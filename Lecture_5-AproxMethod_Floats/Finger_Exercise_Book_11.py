# the maximum floor that egg will not break
x = 30

num_guesses = 1
epsilon = 0
low = min(0, 120)
high = max(0, 120)
ans = (low + high)/2

while abs(ans - x) > epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans < x:
        low = ans
    else:
        high = ans
    ans = round((high + low)/2)


print('low =', low, 'high =', high, 'ans =', ans)
print('number of guesses =', num_guesses)
print(f"The maximum floor that egg wil not break =", ans)