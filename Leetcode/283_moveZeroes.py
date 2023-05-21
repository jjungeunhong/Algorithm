def moveZeroes(nums):
	for i in range(len(nums) - 1):
		for j in range(len(nums) - 1):
			if nums[j] == 0:
				nums[j], nums[j + 1] = nums[j + 1], nums[j]
			else:
				continue

#from dhanu817
def moveZeroes2(nums):
	for i in range(nums.count(0)):
		nums.remove(0)
		nums.append(0)

#from olsh
def moveZeroes3(nums):
	zero_size = 0
	for i in range(len(nums)):
		if nums[i] == 0:
			zero_size += 1
		else:
			swap_num = nums[i]
			nums[i] = 0
			nums[i - zero_size] = swap_num