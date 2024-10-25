def is_perfect (num):

    k = 0

    for i in range(1, num):
        if num % i == 0:
            k += i

    if num == k:
        return "This is a perfect number"
    
    else:
        return "This is not a perfect number"
    
print(is_perfect(5))
print(is_perfect(6))
print(is_perfect(28))