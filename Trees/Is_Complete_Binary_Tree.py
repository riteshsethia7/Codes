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
    
def IscompleteBinary(node,i,N):
    if node == None:
        return True
    if i>=N:
        return False
    return (IscompleteBinary(node.l,2*i+1,N) and IscompleteBinary(node.r,2*i+2,N))
        
for _ in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))
    node = Node(arr[0])
    for i in range(1,N):
        node = Insert(node,arr[i])
    if IscompleteBinary(node,0,N):
        print('Yes')
    else:
        print('No')
