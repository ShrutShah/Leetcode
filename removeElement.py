nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p=0
        for i in range(len(nums)):
          if nums[i] != val:
            nums.append(nums[i])
            p+=1
        print(nums)
        for i in range(p):
          nums.insert(0,'*')
        print(nums)
        print(len(nums) -p ,len(nums)-1)
        for i in range(len(nums) -p -1 ,len(nums)-1):
          nums.remove('*')
          nums.insert(0,nums[i])

        return p
            