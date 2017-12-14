#S3C2 Nick Wang
#This is the python code for some recursion problems
def factorial(x):
    if x == 1:
        return 1
    return x*factorial(x-1)

def bunnyEars(bunnies):
    if bunnies == 0:
        return 0
    return bunnyEars(bunnies-1)+2

def fibonacci(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fibonacci(x-2)+fibonacci(x-1)

def bunnyEars2(bunnies):
    if bunnies == 0:
        return 0
    if bunnies%2 ==0:
        return bunnyEars2(bunnies-1)+3
    if bunnies%2 ==1:
        return bunnyEars2(bunnies-1)+2

def triangle(x):
    if x == 0:
        return 0
    return triangle(x-1)+x

def sumDigits(x):
    if x == 0:
        return 0
    return sumDigits(int(x/10))+x%10

def count7(x):
    if x == 0:
        return 0
    if x%10==7:
        return count7(int(x/10))+1
    if x%10!=7:
        return count7(int(x/10))

def count8(x):
    if x == 0:
        return 0
    if x%10 ==8 and (int(x/10))%10 !=8:
        return count8(int(x/10))+1
    if x%10 ==8 and (int(x/10))%10 ==8:
        return count8(int(x/10))+2
    if x%10 !=8:
        return count8(int(x/10))

def powerN(x1,x2):
    if x2 == 1:
        return x1
    return x1*powerN(x1,x2-1)

def countX(x):
    if x == '':
        return 0
    if x[-1:] == 'x':
        return countX(x[:-1])+1
    if x[-1:] != 'x':
        return countX(x[:-1])

def countHi(x):
    if x == '':
        return 0
    if x[-2:] == 'hi':
        return countHi(x[:-2])+1
    else:
        return countHi(x[:-1])

def changeXY(x):
    if x == '':
        return ''
    if x[-1:] == 'x':
        return changeXY(x[:-1])+'y'
    else:
        return changeXY(x[:-1])+x[-1:]

def changePi(x):
    if x == '':
        return ''
    if x[-2:] == 'pi':
        return changePi(x[:-2])+'3.14'
    else:
        return changePi(x[:-1])+x[-1:]

def noX(x):
    if x == '':
        return ''
    if x[-1:] == 'x':
        return noX(x[:-1])
    else:
        return noX(x[:-1])+x[-1:]

def array6(x,index):
    if index == len(x):
        return False
    if x[index] == 6:
        return True
    return array6(x, index+1)

def array11(x,index):
    if index == len(x):
        return 0
    if x[index] == 11:
        return array11(x,index+1)+1
    return array11(x,index+1)

def array220(x,index):
    if index == len(x)-1:
        return False
    if x[index]*10 == x[index+1]:
        return True
    return array220(x,index+1)

def allStar(x):
    if x[:-1] == '':
        return x[-1:]
    else:
        return allStar(x[:-1])+'*'+x[-1:]

def pairStar(x):
    if x == '':
        return ''
    if x[-1:] == x[-2:-1]:
        return pairStar(x[:-1])+'*'+x[-1:]
    else:
        return pairStar(x[:-1])+x[-1:]

def endX(x):
    if x == '':
        return ''
    if x[0] == 'x':
        return endX(x[1:]+'x')
    else:
        return x

def countPairs(x):
    if x == '':
        return 0
    if x[-1:] == x[-3:-2]:
        return countPairs(x[:-1])+1
    else:
        return countPairs(x[:-1])

def countAbc(x):
    if x == '':
        return 0
    if x[0] == 'a' and x[1] == 'b' and x[2] == 'a':
        return countAbc(x[1:])+1
    if x[0] == 'a' and x[1] == 'b' and x[2] == 'c':
        return countAbc(x[1:])+1
    else:
        return countAbc(x[1:])

def count11(x):
    if x == '':
        return 0
    if x[0] == '1' and x[1] == '1':
        return count11(x[2:])+1
    else:
        return count11(x[1:])

def stringClean(x):
    if x == '':
        return ''
    if x[-1] == x[-2:-1]:
        return stringClean(x[:-1])
    else:
        return stringClean(x[:-1])+x[-1:]

def countHi2(x):
    if len(x) < 2:
        return 0
    if x == '':
        return 0
    if x[0] != 'x' and x[1] == 'h' and x[2] == 'i':
        return 1 + countHi2(x[1:])
    else:
        return countHi2(x[1:])

def parenBit(x):
    if x[0] != '(':
        if x[len(x)-1] != ')':
            return parenBit(x[1:-1])
        return parenBit(x[1:])
    if x[len(x)-1] != ')':
        return parenBit(x[:len(x)-1])
    else:
        return x

def nestParen(x):
    if x == '':
        return True
    if (x[0] == '(') and (x[len(x)-1] == ')'):
        return nestParen(x[1:len(x)-1])
    else:
        return False

def strCount(x1,x2):
    if x1 == '':
        return 0
    if x1[0:len(x2)] == x2:
        return strCount(x1[len(x2):],x2)+1
    else:
        return strCount(x1[1:],x2)

def strCopies(x1,x2,n):
    if x1 == '':
        return False
    if x1[0:len(x2)] == x2:
        return strCopies(x1[1:],x2,n-1)
    if n<= 0:
        return True
    return strCopies(x1[1:],x2,n)

def strDist(x1,x2):
    if x1 == 0:
        return 0
    if x1[0:len(x2)] != x2:
        return strDist(x1[1:],x2)
    if x1[-len(x2):] != x2:
        return strDist(x1[:-1],x2)
    return len(x1)
    
print(strDist("catcowcat","cat"))




