from dataclasses import dataclass 

@dataclass #구조체 선언부
class nodetype:
    parent:int=None
    depth:int=None
@dataclass
class edge:
    a:int=None
    b:int=None
    weight:int=None
    
def find(U:nodetype, i:int): #find 함수 구현부
    k=i
    while(U[k].parent!=k):
        k = U[k].parent
    return k

def merge(U:nodetype,p:int,q:int):#merge 함수 구현부
    if(U[p].depth == U[q].depth):
        U[p].depth += 1
        U[q].parent = p
    elif(U[p].depth < U[q].depth):
        U[p].parent = q
    else:
        U[q].parent = p

# graph=[edge(1,2,1),edge(1,3,3),edge(2,3,3),edge(2,4,6),edge(3,4,4),edge(3,5,2),edge(4,5,5)] #교재
graph=[edge(1,3,3),edge(1,5,1),edge(1,4,6),edge(2,3,3),edge(2,4,7),edge(3,4,6),edge(4,5,2)] #자작 데이터

graph.sort(key = lambda x: x.weight) 
F=[]
n=5 

tree_edges = 1
U=[nodetype(i,0) for i in range(n+1)]
index=0

while (tree_edges<=n-1):
    i, j, wt =graph[index].a,graph[index].b,graph[index].weight
    p=find(U,i) 
    q=find(U,j)
    if (p!=q):
        merge(U,p,q)
        F.append(graph[index])
        tree_edges += 1
    index+=1
print('최소신장트리: ',F)
print("\nU배열 출력")
for i in U:
    print(" parent: {0}, depth:{1}".format(i.parent,i.depth))

