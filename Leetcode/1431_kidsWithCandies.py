def kidsWithCandies(candies, extraCandies):
	res = []
	for i in range(len(candies)):
		n = candies[i] + extraCandies
		for j in range(len(candies)):
			if n >= candies[j]:
				if j == len(candies) - 1:
					res.append(True)
					break
				continue
			else:
				res.append(False)
				break
	print(res)


candies = [2, 3, 5, 1, 3]
extraCandies = 3
kidsWithCandies(candies, extraCandies)