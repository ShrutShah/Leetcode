strs = ["flower","flow","flight"]

def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        c = len(strs)
        if c > 1:
          res=""
          l=201
          for k in range(c):
            l = min(l,len(strs[k]))
            
          for i in range(l):
            t=[]
            for j in range(c):
              t.append(strs[j][i]) 
            if len(set(t)) != 1:
              break
            res+= strs[0][i]
          return res 
        elif c==1 and len(strs[0]):
          return strs[0]
        else:  
          return ""