import sys
input = lambda: sys.stdin.readline().strip()

def g(x):
    d = 2
    ans = 1
    while d * d <= x:
        if x % d == 0:
            cnt = 1
            while x % d == 0:
                x //= d
                cnt += 1
            ans *= cnt
        d += 1
    if x > 1:
        ans *= 2

    return ans

def main():
    n = int(input())
    for i in range(n, 0, -1):
        flag = True
        for j in range(i - 1, 0, -1):
            if not(g(i) > g(j)):
                flag = False
                break
        if flag:
            print(i)
            return    

main()
