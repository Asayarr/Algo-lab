import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

best_d = 0
best_num = 0

def dfs(idx, max_e, cur, div):
    global best_d, best_num
    if div > best_d or (div == best_d and cur < best_num):
        best_num = cur
        best_d = div

    if idx == len(primes):
        return

    for e in range(1, max_e + 1):
        if cur * primes[idx] ** e > n:
            break
        dfs(idx + 1, e, cur * primes[idx] ** e, div * (e + 1)) 
        
dfs(0, 30, 1, 1)
print(best_num)