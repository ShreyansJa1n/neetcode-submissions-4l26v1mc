class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for i in strs:
            sorted_str = sorted(i)

            if tuple(sorted_str) in groups:
                groups[tuple(sorted_str)].append(i)
            else:
                groups[tuple(sorted_str)] = [i]
        return list(groups.values())