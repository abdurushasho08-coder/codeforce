n=int(input())
z=0
for i in range(n):
    y=input()

    if y=="++X" or y == "X++":
        z+=1
    elif y=="--X" or y == "X--":
        z-=1
print(z)
