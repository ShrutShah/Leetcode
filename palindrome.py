x = -121

def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        s ='*'+ str(x) 
        rs = ''
        for i in range(len(s)-1,0,-1):
          rs += s[i]
        
        print(rs)
        if rs == str(x):
          return True
        else:
          return False
