n = int(input())

for i in range(1,n):
    value=0
    value += i
    k=value
    for j in str(k):
        value+=int(j)
    if value == n:
        print(k)
