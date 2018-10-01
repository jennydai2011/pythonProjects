def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target int
    :rtype List[int]
    """

    for i in range(len(nums)):
        a = target - nums[i]
        if a in nums and i!=nums.index(a):
            return ([i, nums.index(a)])
    

def main():
    a = [2, 7, 11, 15]
    print(twoSum(a, 9))

if __name__ == "__main__":
    main()
