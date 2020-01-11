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
def Inorder(node):
    if node == None:
        return
    Inorder(node.l)
    print(node.d,end=" ")
    Inorder(node.r)
def Preorder(node):
    if node == None:
        return
    print(node.d,end=" ")
    Preorder(node.l)
    Preorder(node.r)       
def Postorder(node):
    if node == None:
        return
    Postorder(node.l)
    Postorder(node.r)
    print(node.d,end=" ")
for _ in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))
    node = Node(arr[0])
    for i in range(1,N):
        node = Insert(node,arr[i])
    Preorder(node)
    print()
    Inorder(node)
    print()
    Postorder(node)
    print()
    print()
