a=list(map(int,input().split()))
def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans
print(solve(a))