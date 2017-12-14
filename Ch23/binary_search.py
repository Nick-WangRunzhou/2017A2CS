#Nick Wang Binary Search
alist=[12,19,23,27,33,37,41,45,56,59,60,62,71,75,80,84,88,92,99]
print(alist)
def BinarySerch(alist,num):
    low=0
    high=len(alist)-1
    while low<=high:
        mid=(low+high)/2
        if alist[mid]==num:
            return mid
        elif num<alist[mid]:
            high=mid-1
        else:
            low=mid+1
            return False
        return mid
        print(mid)
num=int(input("input number"))
   
        
        
  
        
        

            
        
