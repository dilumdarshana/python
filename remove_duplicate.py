def remove_duplicates(nums):
  count = 1
  i = 1

  while i < len(nums):
    if (nums[i] == nums[i-1]):
      count += 1
    else:
      count = 1

    if (count >= 3):
      nums.pop(i)
    else:
      i += 1

  return nums


print (remove_duplicates([1,1,1,2,2,3]))
