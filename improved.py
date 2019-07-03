pop=int(input())
zip=list(map(int,input().split()[:pop]))
zip.sort()
for x in zip:
  print(x,end=" ")
