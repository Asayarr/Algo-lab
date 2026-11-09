import sys
input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    a = list(map(int, input().split()))
    res = 0

    for i in range(n):
        res += a[i]

    print(res)

main()