def mod(num1,num2):
    q = num1//num2

    if q<0:
        q = q + 1

    mod = num1 - num2 * q
    return mod

p = mod(5,2)
print(p)