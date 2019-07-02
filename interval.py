AA,vad=map(int,input().split())
for v in range(AA+1,vad,1):
    if(v>1):
        for n in range(2,v):
            if(v%n==0):
                break
        else:
            print(v,end=" ")
