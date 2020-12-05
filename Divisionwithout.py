def division(numerator,denominator):
    neg=0
    quotient=0

    if numerator<0:
        numerator=-numerator
        neg=1
        if denominator<0:
            denominator=-denominator
            neg=0

    if denominator<0:
        denominator=-denominator
        neg=1
        if numerator<0:
            numerator=-numerator
            neg=0

    while numerator>=denominator:
        numerator-=denominator
        quotient+=1

    if neg==1:
        quotient=-quotient
    return quotient

p = division(10,2)
print(p)

