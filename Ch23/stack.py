#Stack
#Wang Runzhou Opt 3

class Stack:
  def __init__(self):
    self.items = []
   
  def push(self, item):
    self.items.append(item)
   
  def pop(self):
    return self.items.pop()

s=Stack()
s.push(3)
s.push(4)
s.push(5)
s.push(6)
print(s.pop())
print(s.pop())
print(s.pop())


        


