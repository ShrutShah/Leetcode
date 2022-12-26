s = "[(])"

def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        for i in range(len(s)):
          if s[i] == ')':
              if len(l) == 0:
                return False 
              see = l.pop()
              if see == '(':
                pass
              else:
                return False
          elif s[i] == ']':
              if len(l) == 0:
                return False
              see = l.pop()
              if see == '[':
                pass
              else:
                return False
          
          elif s[i] == '}':
              if len(l)==0:
                return False
              see = l.pop()
              if see == '{':
                pass
              else:
                return False
          else:
            l.append(s[i])

        if len(l):
          return False
        else:
          return True



