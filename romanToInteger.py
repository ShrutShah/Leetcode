s = "IX"

def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        c = 0
        for i in range(len(s)):
          print(i,s[i])
          if s[i] == 'I':
            if i<len(s)-1:
              if s[i+1]=='V':  
                c+=4
              
              elif s[i+1]=='X':
                c+= 9
              
              else:
                c+=1 
                print(c) 

            else:
              c+=1

          elif s[i] == 'X': 
            if s[i-1] == 'I':
              pass
            elif i<len(s)-1:
              if s[i+1] == 'L':
                c+=40
              
              elif s[i+1] == 'C':
                c+=90
              else: 
                c+=10
            else:
              c+=10

          elif s[i] == 'C':
            if s[i-1] == 'X':
                pass
            elif i<len(s)-1 :
              if s[i+1] == 'D':
                c+=400 
              
              elif s[i+1] == 'M':
                c+=900
              else: 
                c+=100
            else: 
              c+=100
              
          elif s[i] == 'V':
            if s[i-1]=='I':
              pass
            else: 
              c+= 5

          elif s[i] == 'L':
            if s[i-1]=='X':
              pass
            else:
              c+= 50
            

          elif s[i] == 'D':
            if s[i-1]=='C':
              pass
            else: c+=500
          
          elif s[i] == 'M':
            if s[i-1]=='C':
              pass
            else: c+=1000
            
        
        return c


