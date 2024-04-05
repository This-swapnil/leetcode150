class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevmap:
                return [prevmap[diff], i]
            prevmap[n] = i
        return


# time complexity O(n**2) solution
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoSum(nums=nums, target=target))
