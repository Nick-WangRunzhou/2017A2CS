def myHash(data,hashLength,):
    return data % hashLength

def insertHash(hash,hashLength,data):
    hashAddress=myHash(data,hashLength)
    while(hash.get(hashAddress)):
        hashAddress+=1
        hashAddress=myHash(data,hashLength)
    hash[hashAddress]=data

def findHash(hash,hashLength,data):
    hashAddress=myHash(data,hashLength)
    while hash.get(hashAddress) and hash[hashAddress]!=data:
        hashAddress+=1
        hashAddress=hashAddress%hashLength
    if hash.get(hashAddress)==None:
        return None
    return hashAddress

if __name__ == '__main__':
    hashLength=10
    L=[16,17,18]
    hash={}
    for i in L:
        insertHash(hash,hashLength,i)
    result=findHash(hash,hashLength,17)
    if result:
        print("data is found at",result)
        print("value =",hash[result])
    else:
        print("value not found")
    print(hash)

