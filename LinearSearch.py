def linearsearch(alist,key):
    for i in range(len(alist)):
        if (alist[i] == key):
            return i
    return -1

alist = input("Enter the list of numbers: ")
alist = alist.split()
alist = [int(x) for x in alist]
key = int(input("Enter the number to search: "))

index = linearsearch(alist,key)
if index < 0:
    print ("{} key value is not found".format(key))

else:
    print("{} key value is in index{}".format(key,index))