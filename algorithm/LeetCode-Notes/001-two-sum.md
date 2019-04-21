#1. Two Sum
##描述
给定一个整数数组，返回两个数字的索引，使得它们加起来等于一个特定的目标值。

您可以假设每个输入都有一且只有一个答案，数组中每个元素只能使用一次。

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
##解析
用哈希表按照“数值-下标”的关系存储给定数组中的数值，单次查找的时间复杂度为O(1)。

时间复杂度：O(n)
空间复杂度：O(n)
语言：Python

```
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target int
    :rtype List[int]
    """

     # solution#1 - time O(n), space O(n)
        temp = {nums[0]: 0}
        # temp ={}
        #for i, v in enumerate(nums, 0):
        for i in range(1, len(nums)):
            v = nums[i]
            #if target - v in temp.keys():
            if target - nums[i] in temp.keys():
                return [temp[target - v], i]
            else:
                temp[v] = i

        # solution#2 - time o(n), space o(1)
        # for i in range(len(nums)):
        #     a = target - nums[i]
        #     if a in nums and i!=nums.index(a):
        #         return ([i, nums.index(a)])
```
