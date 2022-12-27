def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.insert(0,'*')
        c = len(digits)
        sum = 0
        for i in range(c-1,0,-1):
          j =c -i -1
          sum += digits[i]* (10 ** j)  
        sum += 1
        sum = str(sum)
        res = []
        for k in range(len(sum)):
          res.append(int(sum[k]))
        
        return res