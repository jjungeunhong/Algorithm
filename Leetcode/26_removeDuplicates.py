def removeDuplicates(nums):
	res = []
	i = 0
	while i < len(nums):
		if nums[i] in res:
			nums.remove(nums[i])
		else:
			res.append(nums[i])
			i += 1
	print(nums)

nums = [1, 1, 2]
removeDuplicates(nums)