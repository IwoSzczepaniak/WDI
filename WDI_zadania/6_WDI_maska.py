def f(T,n,pos=0,iloczyn=1,mask=0):
    if iloczyn==n:
        for i in range(1,pos+1):
            if mask % 2 == 1:
                print(T[pos-i], end=" ")
            mask//=2
        print()
        return 1
    if pos==len(T):
        return 0
    return f(T,n,pos+1,iloczyn,mask*2) + f(T,n,pos+1,iloczyn*T[pos],mask*2+1)

tab = [2,3,4,5,6,7,8,9,5]
print(f(tab, 54))
