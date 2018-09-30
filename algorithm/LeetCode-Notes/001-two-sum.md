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
a = [2, 7, 11, 15]
d = {str(i) : a[i] for i in range(len(a))}

print(d)

target = 9

i1="0"
i2="0"

found=False
for k, v in d.items():
    print("k is "+ str(k) + ", v is "+ str(v))
    i1=k
    f = target - d[k]
    for fk2 in d.keys():
        if d[fk2] == f:
            print("found 2nd item:" + str(f) + ", index is "+ fk2)
            i2=fk2
            found=True
            break
    if found:
        break

print("found matching index: "+ str(i1) +" and "+ str(i2))
```