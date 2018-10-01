class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b 
    """
    def aplusb(self, a, b):
        # write your code here, try to do it without arithmetic operators.
        from ctypes import c_int32
        a = c_int32(a).value
        b = c_int32(b).value
        if b == 0:
            return a
        if a == 0:
            return b
        while b!=0:
            carry = c_int32(a&b).value
            a = c_int32(a ^ b).value
            b = c_int32(carry << 1).value
        return a 

s = Solution()
t = s.aplusb(10, -10)
print(t)