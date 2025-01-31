class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False #catch when the number is negative.
        if x == 0: return True
        ans = 0
        temp = x
        while(x):
            ans = (ans*10) + (x%10)
            x = (x*0.1)//1
            
        if(ans == temp): 
            return True
        else: 
            return False
        
