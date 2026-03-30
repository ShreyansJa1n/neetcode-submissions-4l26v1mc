class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for i in strs:
            encoded = f"{len(i)}#{i}"
            final += encoded

        return final

    def decode(self, s: str) -> List[str]:
        strs = []
        counter = 0
        while counter < len(s):
            j = counter
            while s[j] != "#":
                j += 1
            length = int(s[counter: j])
            strs.append(s[j + 1 : j + length + 1])
            counter = j + 1 + length
        return strs
