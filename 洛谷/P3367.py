import sys
input = lambda: sys.stdin.readline().strip()

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
       n, m = map(int, input().split())
       dsu = DSU(n + 1)
       out = []
       for _ in range(m):
           z, x, y = map(int, input().split())
           if z == 1:
               dsu.union(x, y)
           else:
               out.append("Y" if dsu.same(x, y) else "N")
       print("\n".join(out))


main()     