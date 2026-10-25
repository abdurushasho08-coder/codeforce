n=int(input())
y=0
for i in range(n):
   x = list(map(int, input().split()))
   if x.count(1)>=2:
      y+=1

print(y)