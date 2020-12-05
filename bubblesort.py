def bubblesort(alist):
    for i in range(0,len(alist)):
        no_swap = True
        for j in range(0,len(alist)-1):
            if alist[j+1] < alist[j]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                no_swap = False

        if no_swap == True:
            return

alist = input("Enter the list of numbers: ")
alist = alist.split()
alist = [int(x) for x in alist]
bubblesort(alist)
print(alist)
