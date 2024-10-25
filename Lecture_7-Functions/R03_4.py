epsilon = 0.01
ans = 0.0
increment = 0.001
num_guesses = 0
num = 0.01

while abs(ans - num) >= epsilon:
    ans += increment
    num_guesses += 1

print("The number is", num)
print("The number of guesses is", num_guesses)