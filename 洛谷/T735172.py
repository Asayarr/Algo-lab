import sys
input = lambda: sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())
    Misserina = list(map(int, input().split()))
    Melo = list(map(int, input().split()))
    Misserina.sort()
    Melo.sort()
    
    if Misserina[0] > Melo[0]:
        print("Melo")
        print(Misserina[0] - Melo[0])
    else:
        print("Misserina")
        print(Melo[0] - Misserina[0])

main()