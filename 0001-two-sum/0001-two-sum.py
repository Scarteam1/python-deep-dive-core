class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lookup_table = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in lookup_table:
                return [lookup_table[complement], index]
            lookup_table[num] = index
        return []
