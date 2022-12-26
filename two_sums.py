nums = [2,7,11,15]
target = 9

def sum2():
  for i in range(len(nums)):
    sum = 0
    for j in range(len(nums)):
      sum = nums[i]
      if j!=i:
        sum += nums[j]
        print(sum)
        if target == sum:
          print([i,j])
