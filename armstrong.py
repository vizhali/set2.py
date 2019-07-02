p=int(input())
q=0
r=p
while r>0:
 digit = r%10
 q +=digit ** 3
 r //=10
if p==q:
 print("yes")
else:
 print("no")
