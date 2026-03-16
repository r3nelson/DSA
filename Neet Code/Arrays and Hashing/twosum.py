from typing import List
class Solution:
    def twoSum(self, nums: List[int],target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            if nums[i] in diffs:
                return [diffs[nums[i]], i]
            diff = target - nums[i]
            diffs[diff] = i

print(Solution().twoSum(nums=[3,4,5,6],target=7))
print(Solution().twoSum(nums=[4,5,6],target=10))
print(Solution().twoSum(nums=[5,5],target=10))