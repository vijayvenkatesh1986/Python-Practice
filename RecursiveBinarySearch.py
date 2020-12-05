def recursivesearch(alist,start,end,key):
    if not start<end:
        return -1

    while (start < end):
        mid = (start+end)//2
        if (alist[mid] < key):
            return binarysearch(alist,mid+1,end,key)
        elif (alist[mid]>key):
            return binarysearch(alist,start,mid,key)
        else:
            return mid

alist = input("Enter the list of numbers: ")
alist = alist.split()
alist = [int(x) for x in alist]
key = int(input("Enter the number to search: "))

index = recursivesearch(alist,0,len(alist),key)
if index < 0:
    print ("{} key value is not found".format(key))

else:
    print("{} key value is in index{}".format(key,index))
