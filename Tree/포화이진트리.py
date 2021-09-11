#포화이진트리.py
class Node:
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None

    def __repr__(self):
        return self.data

class PBT:
    def __init__(self):
        self.root=None
        self.count = 1
        self.queue = [Node('none')]

    def insertNode(self,data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:
            if self.root.left is None:
                self.root.left = newNode
            elif self.root.right is None:
                self.root.right = newNode
            else:
                if self.queue[self.count//2].left is None:
                    self.queue[self.count//2].left = newNode
                elif self.queue[self.count//2].right is None:
                    self.queue[self.count//2].right = newNode
        self.count+=1
        self.queue.append(newNode)

t = PBT()
t.insertNode('A')
t.insertNode('B')
t.insertNode('C')
t.insertNode('D')
t.insertNode('E')
t.insertNode('F')
t.insertNode('G')

root = t.root
print(root)
print(root.left)
print(root.right)










