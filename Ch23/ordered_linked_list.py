#Free list
#Wang Runzhou Opt 3
NP = -1

class Myclass:
    def __init__(self):
        self.Value = ""
        self.Next = NP

def InitializeList():
    List = [Myclass() for i in range(10)]
    SP = NP
    FP = 0
    for i in range(9):
        List[i].Next = i + 1
    List[9].Next = NP
    print(List)
    print(SP,FP)
            
InitializeList()


