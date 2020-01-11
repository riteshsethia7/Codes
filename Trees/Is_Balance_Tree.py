class Node:
    def __init__(self,x):
        self.l = None
        self.r = None
        self.d = x
        
def Insert(node,x):
    if node == None:
        return Node(x)
    if x<node.d:
        node.l = Insert(node.l,x)
    else:
        node.r = Insert(node.r,x)
    return node

def Height(node):
    if node == None:
        return -1
    return max(Height(node.l),Height(node.r))+1
    
def Isbalanced(node):
    if node == None:
        return True
    hl = Height(node.l) 
    hr = Height(node.r)
    if ( abs(hl-hr)<=1 and Isbalanced(node.l) == True and Isbalanced(node.r)== True ):
        return True
    return False
    
for _ in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))
    node = Node(arr[0])
    for i in range(1,N):
        node = Insert(node,arr[i])
    if Isbalanced(node):
        print('Yes')
    else:
        print('No')
