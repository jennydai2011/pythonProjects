# Python桶排序
def bucket(lst):
    buckets = [0] * ((max(lst) - min(lst)) + 1)
    for i in range(len(lst)):
        buckets[lst[i] - min(lst)] += 1
    res = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i + min(lst)] * buckets[i]
    return res


a = [12, 4, 2, 4, 56, 1, 4, 0]
b = bucket(a)
print(b)