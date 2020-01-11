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
def IsfullBinary(node):
    if node == None:
        return True
    if (node.l == None) and (node.r == None) :
        return True
    if (node.l != None) and (node.r != None) :
        return(IsfullBinary(node.l) and IsfullBinary(node.r))
    return False
    
for _ in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))
    node = Node(arr[0])
    for i in range(1,N):
        node = Insert(node,arr[i])
    if IsfullBinary(node):
        print('True')
    else:
        print('False')
