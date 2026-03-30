class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid_triplets = []
        for i in triplets:
            if i[0] <= target[0] and i[1] <= target[1] and i[2] <= target[2]:
                valid_triplets.append(i)

        merged = [0,0,0]
        for i in valid_triplets:
            merged[0] = max(merged[0], i[0])
            merged[1] = max(merged[1], i[1])
            merged[2] = max(merged[2], i[2])

        return merged == target