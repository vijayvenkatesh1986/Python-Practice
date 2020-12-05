def sub(num1,num2):
    num1 = int(input("Enter number 1"))
    num2 = int(input("Enter number 2"))
    result = num1 + (~num2+1)
    return result

res = sub(5,6)
print(res)