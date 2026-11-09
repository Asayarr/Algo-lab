class Solution:
    def smallestValue(self, n: int) -> int:
        def factorize(n):
            x = n
            res = []
            d = 2
            while d * d <= x:
                if x % d == 0:
                    cnt = 0
                    while x % d == 0:
                        x //= d
                        cnt += 1    
                    res.append((d, cnt))
                d += 1
            if x > 1:
                res.append((x, 1))

            newN = 0
            for q, v in res:
                newN += q * v

            if n == newN:
                return newN
            else:
                return factorize(newN)

        return factorize(n)         

                

                           
                        