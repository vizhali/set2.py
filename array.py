put=int(input())
mw=list(map(int,input().split()[:put]))
mw.sort()
for z in mw:
        print(z,end=" ")
