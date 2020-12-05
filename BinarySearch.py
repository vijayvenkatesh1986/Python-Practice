def binarysearch(alist, key):

    start = 0
    end = len(alist)

    while (start < end):
        mid = (start + end)//2
        if (alist[mid] > key):
            end = mid
        elif (alist[mid] < key):
            start = end + 1
        else:
            return mid
    return -1

alist = input("Enter the list of numbers: ")
alist = alist.split()
alist = [int(x) for x in alist]
key = int(input("Enter the number to search"))

index = binarysearch(alist,key)
if index < 0:
    print ("{} key value is not found".format(key))

else:
    print("{} key value is in index{}".format(key,index))
