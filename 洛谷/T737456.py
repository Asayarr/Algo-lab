import sys
input = lambda: sys.stdin.readline().strip()

def main():
    q, w = map(int, input().split())
    a = list(map(int, input().split()))
    n = [int(input()) for _ in range(q)]

    if len(set(a)) == 1:
        out = [str(a[0] * x) for x in n]
        sys.stdout.write("\n".join(out) + "\n")
        return

    maxn = max(n)

    pref = [0] * (maxn + 1)
    
    for x in range(1, maxn + 1):
        cnt = 0
        temp = x
        while temp % 2 == 0:
            temp //= 2
            cnt +=1
            if cnt == w:
                break
        pref[x] = pref[x - 1] + a[cnt]

    out = []
    for i in n:
       out.append(str(pref[i]))
    sys.stdout.write("\n".join(out) + "\n")
        
main()            
