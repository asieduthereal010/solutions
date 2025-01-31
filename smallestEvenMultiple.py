class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if(n%2 == 0): return n #catch the case where two can divide the number.
        else: return n * 2
