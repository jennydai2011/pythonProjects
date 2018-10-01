# Description
Write an algorithm which computes the number of trailing zeros in n factorial.

```
class Solution:
    """
    @param n: An integer
    @return: The number of zero in factorial
    """
    def trailingZero(self, n):
        if n <5:
            return 0
        elif n < 10:
            return 1
        else:
            return n//5 + self.trailingZero(n//5)
```