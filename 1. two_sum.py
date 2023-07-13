class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # num_list = sorted(nums)

        # numbers_that_can_fit = []

        #for i_elem in num_list:
        #    if i_elem <= target:
        #        numbers_that_can_fit.append(i_elem)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return (i, j)

nums = [2, 7, 11, 15]
target = 9

s = Solution()

print(s.twoSum(nums, target))
