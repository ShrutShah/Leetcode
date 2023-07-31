class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}

        for current_index, current_value in enumerate(nums):
            search_value = target - current_value
            if search_value in hash_map:
                return [hash_map[search_value], current_index]

            else:
                hash_map[current_value]=current_index
        
        return
