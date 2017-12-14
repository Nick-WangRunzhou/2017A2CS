def bubbleSort(alist):
    for thenum in range(len(alist)-1,0,-1):
        for i in range(thenum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
alist=[]
num=int(input("how many numbers in the array"))
count=0
while count<num:
    a=int(input("please input"))
    alist.append(a)
    count=count+1
print(alist)
bubbleSort(alist)
print(alist)
