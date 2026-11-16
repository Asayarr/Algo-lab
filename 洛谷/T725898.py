import sys
input = lambda: sys.stdin.readline().strip()
MOD = 998244353

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        up = 1 << n
        cnt = 0
        for a in range(0, up):
            for b in range(0, up):
                if (a ^ b).bit_count() == (a + b).bit_count():
                    cnt +=1
        print(cnt % MOD)

main()