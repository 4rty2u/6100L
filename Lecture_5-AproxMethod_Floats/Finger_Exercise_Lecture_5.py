my_str = "abcdefg"
my_str_g = ""

for i in range(0, len(my_str), 2):
    if i % 2 == 0:
        my_str_g += my_str[i]

print(my_str_g)