def is_in_range (num, renge):
    z = 0

    for i in range(renge):
        if i == num:
            z += 1

    if z != 0:
        return "Is it in range"
    
    else:
        return "Is not in range"
    
print(is_in_range(11, 10))