import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

    def same(self, a, b):
        return self.find(a) == self.find(b)

def main():
    data = sys.stdin.read().split()
    i = 0
    out = []

    while True:
        n = int(data[i]); i += 1
        if n == 0:
            break
        dsu = DSU(n + 1)
        m = int(data[i]); i += 1
        for _ in range(m):
            a = int(data[i]); b = int(data[i + 1]); i += 2
            dsu.union(a, b)
        cnt = 0
        for j in range(1, n + 1):
            if dsu.parent[j] == j:
                cnt += 1
        out.append(str(cnt - 1))

    print("\n".join(out))

main()  