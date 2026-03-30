class TimeMap:

    def __init__(self):
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.m:
            self.m[key].append([timestamp, value])
        else:
            self.m[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""

        arr = self.m[key]
        l, r = 0, len(arr) - 1

        while l <= r:
            m = (r + l) // 2
            if arr[m][0] == timestamp:
                return arr[m][1]

            if arr[m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1

        return arr[r][1] if r >= 0 else ""
