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

def Filldepth(node,de):
    if node == None:
        return
    node.dep = de
    depth[node.d]=de
    de+=1
    Filldepth(node.l,de)
    Filldepth(node.r,de)

def Height(node):
    if node == None:
        return -1
    return max(Height(node.l),Height(node.r))+1
    
for _ in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))
    node = Node(arr[0])
    for i in range(1,N):
        node = Insert(node,arr[i])
    depth ={}
    h = Height(node)
    Filldepth(node,0)
    for i in range(h,-1,-1):
        arr = [k for k,v in depth.items() if v==i  ]
        for z in arr:
            print(z , end=" ")
        print()
    print()
