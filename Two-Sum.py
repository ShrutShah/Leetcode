class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = nums[-1]-target//2
        d2 = target//2 -nums[0]
        if d1 < d2:
            for i in range(len(nums)-1,-1,-1):
                sum=0
                for j in range(len(nums)-1,-1,-1):
                    sum = 0
                    if i == j:
                        continue
                    else:
                        sum = nums[i] + nums[j]
                        if sum == target:
                            return i,j
        else:
                for i in range(len(nums)):
                    sum=0
                    for j in range(len(nums)):
                        sum = 0
                        if i == j:
                            continue
                        else:
                            sum = nums[i] + nums[j]
                            if sum == target:
                                return i,j
