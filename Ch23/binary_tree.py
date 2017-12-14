# Nick Wang S3C2
# Binary Tree
class BTree:
    NP = -1
    RP = None
    FP = None
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None
    def initialise(self):
        RP = NP
        FP = 1
        Tree = []
        for i in Tree(1,7):
            Tree[i].left = i+1
        Tree[7].left=NP
    def insertLeft(self,value):  
        self.left = BTree(value)  
        return self.left  
    def insertRight(self,value):  
        self.right = BTree(value)  
        return self.right  
    def show(self):  
        print(self.data)
def insert(node,value):  
    if value > node.data:  
        if node.right:  
            insert(node.right,value)  
        else:  
            node.insertright(value)  
    elif value == node.data:  
        print (str(value))+" already in BTree"  
    else:  
        if node.left:  
            insert(node.left,value)  
        else:  
            node.insertleft(value)
def insert(NEP,value):
    if FP!= NP:
        NEP = FP
        FP = Tree[FP].left

            
            
