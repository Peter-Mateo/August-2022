class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for a in range(len(nums)):
                if i == a:
                    continue
                check = nums[i] + nums[a]
                if check == target:
                    break
        print(i, a)
        return (i, a)
ten = []
for i in range(10_000):
    ten.append(i)

two = Solution()
two.twoSum([1,2,3,4,5,6,7,8,9,10], 19)
