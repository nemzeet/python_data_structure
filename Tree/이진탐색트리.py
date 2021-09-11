#이진탐색트리.py
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)
    
class BST:
    def __init__(self):
        self.root = None
        self.count = 1
        self.queue=[Node('none')]

    def insertNode(self,data,node):
        
        if node is None:
            #같이 넘어온 노드가 없다면
            #새로 노드를 만들어서 node 변수에 넣어주고
            node = Node(data)
            self.queue.append(node)
            self.count+=1
            if self.root is None:
                self.root = node
        else:
            #같이 넘어온 노드가 있다면
            if node.data>data:
                #추가하려는 데이터가 넘어온 노드의 데이터보다 작다면
                #넘어온 노드의 left에다가 insertNode를 재귀호출 해서 넣어준다
                #재귀호출시 추가하려는 데이터와 왼쪽노드를 같이 넘겨준다.
                #왼쪽노드가 없다면 None이 넘어갔을 것이고 재귀호출시 위의 if문으로
                #들어가므로 새로운 노드가 만들어지게 된다.
                node.left=self.insertNode(data,node.left)

            else:
                #추가하려는 데이터가 넘어온 노드의 데이터보다 크다면
                #넘어온 노드의 right에다 재귀호출을 진행하여
                #위의 과정과 비슷하게 진행한다
                node.right=self.insertNode(data,node.right)
        #if문에 들어갔다면 새로 생성된 노드가 리턴되고
        #else문에 들어갔다면 같이 넘어온 노드를 다시 그대로 리턴한다
        return node

    def searchNode(self,data,node):
        if node is None:
            return None

        if node.data == data:
            return node

        elif node.data > data:
            return self.searchNode(data,node.left)

        else:
            return self.searchNode(data,node.right)

    def deleteNode(self,data,node):
        if node is None:
            return None

        if node.data>data:
            node.left = self.deleteNode(data,node.left)

        elif node.data<data:
            node.right = self.deleteNode(data,node.right)

        else:
            if node.right is not None:
                temp = self.findMinNode(node.right)
                node.data = temp.data
                node.right=self.deleteNode(temp.data,node.right)
            elif node.left is not None:
                temp = self.findMaxNode(node.left)
                node.data = temp.data
                node.left = self.deleteNode(temp.data,node.left)
            else:
                return None
        return node

    def findMinNode(self,node):
        curr = node
        while curr.left is not None:
            curr=curr.left
        return curr

    def findMaxNode(self,node):
        curr = node
        while curr.right is not None:
            curr = curr.right
        return curr

t = BST()
for data in [21,7,38,61,15,17,42,81,100,1]:
    t.insertNode(data,t.root)

print(t.searchNode(61,t.root).data)


















    











