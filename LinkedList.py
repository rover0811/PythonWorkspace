
class Node:
    def __init__(self,input):
        self.right=None
        self.left=None
        self.data=input

class Chain:
    lastLeft=None
    lastRight=None
    head=None
    def __init__(self,input):
        self.lastLeft=self.lastRight=self.head=Node(input)            

    def append(self,input):
        self.lastRight.right=Node(input)
        self.lastRight.right.left=self.lastRight
        self.lastRight=self.lastRight.right
    def appendLeft(self,input):
        self.lastLeft.left=Node(input)
        self.lastLeft.left.right=self.lastLeft
        self.lastLeft=self.lastLeft.left
        
    def showRight(self):
        while (self.head!=self.lastRight.right):
            print(self.head.data)
            self.head=self.head.right

    def showLeft(self):
        while(self.head!=self.lastRight.right):
            print(self.head.data)
            self.head=self.head.left

a=Chain(0)

for k in range(1,10):
    a.append(k)

# a.showRight()
a.showLeft()


    

    
        
        
        