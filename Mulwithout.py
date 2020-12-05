def mulwithout(num1,num2):
    mul=0
    if (num2<0):
        num2=-num2
        num1=-num1

    for i in range(1,num2+1):
            mul=mul+num1
    return mul


p = mulwithout(5,2)
print(p)


