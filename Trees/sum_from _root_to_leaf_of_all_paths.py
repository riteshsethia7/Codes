# example :4 5 15 2 1 7 17
# output:497095 Total Sum = 421 + 45157 + 451517 = 497095

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

def Getpaths(arr,node,patharr): 
    if node == None: 
        return
    arr.append(node.d) 
    if(node.l == None and node.r == None):
        ans = ""
        for i in arr:
            ans+= str(i)
        patharr.append(ans)
    Getpaths(arr,node.l,patharr) 
    Getpaths(arr,node.r,patharr) 
    arr.pop() 
      
for _ in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))
    node = Node(arr[0])
    for i in range(1,N):
        node = Insert(node,arr[i])
    patharr=[]
    Getpaths([],node,patharr)
    sum=0
    for i in patharr:
        sum=(sum+int(i))%1000000007
    print(sum)
