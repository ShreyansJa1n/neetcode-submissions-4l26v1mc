class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_koko_eat(n):
            hours = 0
            i = 0
            while i < len(piles):
                hours += math.ceil(piles[i]/n)
                i+=1
            return hours

        
        k = 1000000000
        l, r = 1, k
        min_k = float('inf')
        while l <= r:
            mid = (l + r) // 2
            if can_koko_eat(mid) <= h:
                r = mid - 1
                min_k = min(min_k, mid)
            else:
                l = mid + 1

        return min_k
