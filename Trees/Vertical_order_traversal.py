class Node :
    def __init__(self,x):
        self.l = None
        self.r = None
        self.d = x

def Insert(node,x) :
    if node == None :
        return Node(x)
    if x< node.d :
        node.l = Insert(node.l,x)
    else :
        node.r = Insert(node.r,x)    
    return node

def VOT(node,v):
    if node == None :
        return
    if v not in vertical:
        vertical[v] = [node.d]
    else :
        vertical[v].append(node.d)
    VOT(node.l,v-1)
    VOT(node.r,v+1)
    
if __name__ == "__main__" :
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        root = Node(arr[0])
        vertical = dict()
        for i in range(1,n):
            root = Insert(root,arr[i])
        VOT(root,0)
        for k in sorted(vertical.keys()):
            for j in sorted(vertical[k]) :
                print(j,end=" ")
            print()
        print()
            
        
