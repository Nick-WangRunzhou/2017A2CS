#Nick Wang
#Queue
class QueueNode():  
    def __init__(self, value):  
        self.value = value  
        self.next = None  
    
class Queue():  
    def __init__(self):  
        self.front = None  
        self.rear = None  
  
    def isEmpty(self):  
        return self.front is None and self.rear is None
        return self.items == []
  
    def enqueue(self,num):  
        node = QueueNode(num)  
        if self.isEmpty():  
            self.front = node  
            self.rear = node  
        else:  
            self.rear.next = node  
            self.rear = node
        return self.items.insert(0,item)
  
    def dequeue(self):  
        if self.front is self.rear:  
            node = self.front  
            self.front = None  
            self.rear = None  
            return node.value  
        else:  
            node = self.front  
            self.front = node.next  
            return node.value
        return self.items.pop()

l =list()
l = Queue.enqueue(l,1)

