#print depth of each node of BST in order of the given array elements
class Node:
    def __init__(self,x):
        self.l = None
        self.r = None
        self.d = x
        self.dep = None
        
def Insert(node,x):
    if node == None:
        return Node(x)
    if x<node.d:
        node.l = Insert(node.l,x)
    else:
        node.r = Insert(node.r,x)
    return node
#Fills each node with its depth (.dep)

def Filldepth(node,de):
    if node == None:
        return
    node.dep = de
    depth[node.d]=de
    de+=1
    Filldepth(node.l,de)
    Filldepth(node.r,de)
    
for _ in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))
    node = Node(arr[0])
    for i in range(1,N):
        node = Insert(node,arr[i])
    depth ={}
    Filldepth(node,0)
    for i in arr:
        print(depth[i],end=" ")
    print()
  
    
    
