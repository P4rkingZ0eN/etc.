pn=(2,3,5,7,11,13,17,19,23,29,31,37)
def po(n,k,mod):
    ret=1;n%=mod
    while k:
        if k%2:
            ret=ret*n%mod
        k//=2
        n=n*n%mod
    return ret
def ip(n,a):
    if a%n==0:
        return True
    k=n-1
    while True:
        t=po(a,k,n)
        if t==n-1:
            return True
        if k%2:
            return (t==1 or t==n-1)
        k//=2
def Primality_Test(n):
    if n<=1:
        return False
    for i in range(12):
        if(not ip(n,pn[i])):
            return False
    return True
