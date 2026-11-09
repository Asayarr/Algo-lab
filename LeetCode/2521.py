class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        res = set()
        for x in nums:
            d = 2
            while d * d <= x:
                if x % d == 0:
                    while x % d ==0:
                        x //= d
                    res.add(d)  
                d += 1
            if x > 1:
                res.add(x)

        return len(res)          
             


