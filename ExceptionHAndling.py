try:
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter 2nd number:"))
    p = num1//num2
    if num2 == 0:
        raise ZeroDivisionError
    print(p)
except ZeroDivisionError:
    print("The denominator should not be zero")
