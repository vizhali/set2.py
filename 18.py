v,s=map(int,input().split())

for j in range(v+1,s):
  fin=j
  df=0
  while (j>0):
    dt=j%10
    df=df+(dt**3)
    j=j//10
    if(df==fin):
      print(df,end=" ")
