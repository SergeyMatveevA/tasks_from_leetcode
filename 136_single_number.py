class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        storage = set()
        for digit in nums:
            if digit in storage:
                storage.remove(digit)
            else:
                storage.add(digit)
        return list(storage)[0]
