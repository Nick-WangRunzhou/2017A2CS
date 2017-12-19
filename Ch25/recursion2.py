def groupSum(start,array,target):
    if target == 0:
        return True
    if start == len(array):
        return False
    return groupSum(start+1,array,target-array[start]) or groupSum(start+1,array,target)

def groupSum6(start,array,target):
    if start == len(array):
        return target == 0
    if array[start] == 6:
        return groupSum6(start+1,array,target-array[start])
    return groupSum6(start+1,array,target-array[start]) or groupSum6(start+1,array,target)

def groupNoAdj(start,array,target):
    if start == len(array):
        return target == 0
    return groupNoAdj(start+2,array,target-array[start]) or groupNoAdj(start+1,array,target) 

def groupSum5(start,array,target):
    if start == len(array):
        return target == 0
    if array[start] % 5 == 0:
        if start < len(array)-1 and array[start+1] == 1:
            return groupSum5(start+2,array,target-array[start])
        return groupSum5(start+1,array,target-array[start])
    return groupSum5(start+1,array,target-array[start]) or groupSum5(start+1,array,target)

def groupSumClump(start,array,target):
    if start+1 > len(array):
        return target == 0
    if start < len(array)-1:
        if array[start] == array[start+1]:
            i = start
            while i < len(array)-1 and array[i] == array[i+1]:
                i += 1
            i += 1
            return groupSumClump(i,array,target) or groupSumClump(i,array,target-(i-start)*array[i-start])
    return groupSumClump(start+1,array,target) or groupSumClump(start+1,array,target-array[start])

def splitArray(array):
    return splitArrayHelper(0,array,0,0)
def splitArrayHelper(start,array,x1,x2):
    if start == len(array):
        return x1==x2
    return splitArrayHelper(start+1,array,x1+array[start],x2) or splitArrayHelper(start+1,array,x1,x2+array[start])

def splitOdd(array):
    return splitOddHelper(0,array,0,0)
def splitOddHelper(start,array,x1,x2):
    if start == len(array):
        return (x1%10 == 0 and x2 %2 == 1 )or (x1%2 == 1 and x2%10 == 0)
    return splitOddHelper(start+1,array,x1+array[start],x2) or splitOddHelper(start+1,array,x1,x2+array[start])

def split53(array):
    return split53Helper(0,array,0,0)
def split53Helper(start,array,x1,x2):
    if start == len(array):
        return x1==x2
    if array[start]%5 == 0:
        return split53Helper(start+1,array,x1+array[start],x2)
    if array[start]%3 == 0:
        return split53Helper(start+1,array,x1+array[start],x2+array[start])
    return split53Helper(start+1,array,x1+array[start],x2) or split53Helper(start+1,array,x1,x2+array[start])

    
 

