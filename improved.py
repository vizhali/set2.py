pop=int(input())
zip=list(map(int,input().split()[:pop]))
zip.sort()
for k in zip:
  print(k,end=" ")
