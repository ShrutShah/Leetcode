def addBinary(a,b):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(a) == 0 and len(b) == 0:
          return ''
        if len(a) == 0:
          return b
        if len(b) == 0:
          return a
        a = '*' + a
        c = len(a)
        sum1 = 0
        for i in range(c-1,0,-1):
          j =c -i -1
          sum1 += int(a[i])* (2 ** j)  
        print(sum1)
        b = '*' + b
        c = len(b)
        sum2 = 0
        for i in range(c-1,0,-1):
          j =c -i -1
          sum2 += int(b[i])* (2 ** j)  
        print(sum2)
        res = sum1 + sum2
        print(res)
        if res == 0:
          return "0"
        s=""
        while res >= 1:
          s= str(res%2) + s
          res = res//2

        return s