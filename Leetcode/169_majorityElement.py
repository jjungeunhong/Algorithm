def majorityElement(nums):
	res = {}
	for key in nums:
		if key in res:
			res[key] += 1
		else:
			res[key] = 1
	print(max(res, key = res.get))

nums = [1, 1, 3, 3, 3, 3, 4, 4]
majorityElement(nums)