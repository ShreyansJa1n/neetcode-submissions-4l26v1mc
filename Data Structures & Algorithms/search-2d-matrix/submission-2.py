class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search(row: List[int]) -> bool:
            l, r = 0, len(row) - 1
            while l <= r:
                m = (r - l) + 1 // 2
                if row[m] == target:
                    return True
                elif row[m] > target:
                    r = m - 1
                else:
                    l = m + 1            
            return False

        for i in matrix:
            if i[0] <= target <= i[-1]:
                found = binary_search(i)
                if found == True:
                    return True
                break

        return False