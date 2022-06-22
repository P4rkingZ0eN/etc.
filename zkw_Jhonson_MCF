# Author : Seojin Park
from queue import Queue
from queue import PriorityQueue
sz=805;inf=(1<<62)
C=[[0 for i in range(sz)] for i in range(sz)]
W=[[0 for i in range(sz)] for i in range(sz)]
G=[[] for i in range(sz)]
h=[inf for i in range(sz)]
d=[inf for i in range(sz)]
s=0;sink=801
def JHONSON(): #Jhonson's Algorithm
    global h;global d;global G;global C;global W;global sz;global inf;
    global s;global sink
    inQ=[False for i in range(sz)]
    inQ[s]=True;
    q=Queue();q.put(s) #SPFA
    while not Queue.empty(q):
        cur=q.get();inQ[cur]=False
        for nxt in G[cur]:
            if C[cur][nxt]>0 and h[nxt]>h[cur]+W[cur][nxt]:
                h[nxt]=h[cur]+W[cur][nxt]
                if not inQ[nxt]:
                    inQ[nxt]=True
                    q.put(nxt)
    for u in range(sz):
        for v in G[u]:
            if C[u][v]>0:
                W[u][v]+=h[u]-h[v]
    Q=PriorityQueue();Q.put((0,s))
    d[s]=0
    while not PriorityQueue.empty(Q):
        Qt=Q.get();u=Qt[1]
        if d[u]-Qt[0]:continue
        for v in G[u]:
            if C[u][v]>0 and d[v]>d[u]+W[u][v]:
                d[v]=d[u]+W[u][v];Q.put((d[v],v))
    for i in range(sz):d[i]+=h[sink]-h[s]
visit=[False for i in range(sz)];K=[0 for i in range(sz)]
def g(): #update DAG
    global h;global d;global G;global C;global W;global sz;global inf
    global s;global sink;global visit;global K
    mn=inf
    for i in range(sz):
        if not visit[i]:continue
        for u in G[i]:
            if C[i][u]>0 and (not visit[u]):mn=min(mn,d[i]+W[i][u]-d[u])
    if mn>=inf:return False
    for i in range(sz):
        if not visit[i]:d[i]+=mn
    return True
def dfs(p,flow):
    global h;global D;global d;global G;global C;global W;global sz;global inf
    global s;global sink;global K;global visit
    visit[p]=True
    if p==sink:return flow
    while K[p]<len(G[p]):
        j=G[p][K[p]]
        if (not visit[j]) and (d[j]==d[p]+W[p][j]) and C[p][j]>0:
            ret=dfs(j,min(flow,C[p][j]))
            if ret:
                C[p][j]-=ret;C[j][p]+=ret
                return ret
        K[p]+=1
    return 0
def MCF():
    JHONSON()
    global h;global d;global G;global C;global W;global sz;global inf
    global s;global sink;global K;global visit
    res=0;cnt=0
    while True:
        visit=[False for i in range(sz)]
        K=[0 for i in range(sz)]
        now=0
        while True:
            now=dfs(s,inf)
            if now==0:break
            res+=d[sink]*now
            cnt+=now
            visit=[False for i in range(sz)]
        if not g():break
    return(cnt,res)
N,M=map(int,input().split()) #input & make graph
for i in range(1,N+1):
    k=list(map(int,input().split()))
    n=k[0]
    for j in range(1,len(k),2):
        u=k[j];w=k[j+1]
        G[i].append(u+400)
        G[u+400].append(i)
        W[i][u+400]=-w;W[u+400][i]=w
        C[i][u+400]=1
for i in range(1,N+1):
    C[s][i]=1
    G[s].append(i)
    G[i].append(s)
for i in range(1,M+1):
    C[i+400][sink]=1
    G[i+400].append(sink)
    G[sink].append(i+400)
ans=MCF()
print(str(ans[0])+"\n"+str(-ans[1]))
# Baekjoon 11409
