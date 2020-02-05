#check if the given tree is binary search tree or not
class Node :
    def __init__(self,x):
        self.l = self.r = None
        self.d = x
def createTree(arr,node,i,n):
    if i < n:
        temp = Node(arr[i])
        node = temp
        node.l = createTree(arr,node.l,2*i+1,n)
        node.r = createTree(arr,node.r,2*i+2,n)
    return node

def isBST(node,a,b):
    if node == None :
        return True
    if node.d>a and node.d<b :
        return isBST(node.l,a,node.d) and isBST(node.r,node.d,b)
    else :
        return False
    
if __name__ == '__main__' :
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        root = None
        root = createTree(arr,root,0,n)
        a = float('-inf')
        b = float('inf')
        if isBST(root,a,b) :
            print('True')
        else :
            print('False')
