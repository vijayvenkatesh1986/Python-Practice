def selectionsort(alist):
    i = 0
    for i in range(len(alist)-1):
        smallest = i
        for j in range(i+1,len(alist)):
            if (alist[j] < alist[smallest]):
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]


alist = input("Enter the list of numbers: ")
alist = alist.split()
alist = [int(x) for x in alist]
selectionsort(alist)
print(alist)
