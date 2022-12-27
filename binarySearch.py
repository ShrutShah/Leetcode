def modified_binarySearch(nums, target):
  l = 0
  r = len(nums) -1 

  while l <= r:
    mid = l + (r-l)//2

    if nums[mid] < target:
      l = mid + 1
    elif nums[mid] > target:
      r = mid -1
    else:
      return mid

  if nums[mid] < target:
    return mid +1
  else:
    return mid  
