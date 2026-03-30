class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s
        counter = 0
        direction = True
        partitions = [""] * numRows
        partition_counter = 0
        while counter < len(s):
            partitions[partition_counter] += s[counter]

            if partition_counter == numRows - 1:
                direction = False
            elif partition_counter == 0:
                direction = True

            if direction:
                partition_counter += 1
            else:
                partition_counter -= 1

            counter += 1

        return "".join(partitions)

