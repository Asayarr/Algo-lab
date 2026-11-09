from math import isqrt

class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        ans = 0
        for x in nums:
            cnt = 0
            s = 0
            for d in range(1, isqrt(x) + 1):
                if x % d == 0:
                    cnt += 1
                    s += d
                    q = x // d
                    if d != q:
                        cnt += 1
                        s += q
                    if cnt > 4:
                        break    
            if cnt == 4:
                ans += s

        return ans                    
                
