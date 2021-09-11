#트리.py
class Node:
    def __init__(self,data):
        self.data=data
        
class Tree:
    def __init__(self):
        self.blist = ['']

    def insertNode(self,data):
        newNode = Node(data)
        self.blist.append(newNode)

    def printNode(self):
        num = 1
        for i in range(1,len(self.blist)):
            if i==2**num:
                print()
                num+=1
            print(self.blist[i].data,end=" ")

    def deleteNode(self,data):
        for i in range(1,len(self.blist)):
            if self.blist[i].data == data:
                node=self.blist[i]
                del self.blist[i]
                return node
        print("삭제할 값이 없습니다")

    def searchParentNode(self,data):
        for i in range(1,len(self.blist)):
            if self.blist[i].data == data:
                if i==1:
                    print("Root Node")
                else:
                    print("Parent Node :", self.blist[i//2].data)
                return True
        print("찾는 값이 없습니다.")
        return False

    def searchChildNode(self,data):
        cl = list()
        for i in range(1,len(self.blist)):
            if self.blist[i].data == data:
                if i*2<len(self.blist):
                    print("Left Child Node :",self.blist[i*2].data)
                    cl.append(self.blist[i*2])
                    if i*2+1<len(self.blist):
                        print("Right Child Node :",self.blist[i*2+1].data)
                        cl.append(self.blist[i*2+1])
                    else:
                        #오른쪽 자식노드 없음
                        print("Right Child Node : XXXXX")
                    return cl
                else:
                    print("Leaf Node")
                    return True
        print("찾는 값이 없습니다.")
        return False

t = Tree()
for i in range(65,91):
    t.insertNode(chr(i))

t.printNode()











