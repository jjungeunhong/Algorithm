def reverseWords(s):
	i = 0
	res = []
	while i < len(s):
		myList = []
		if s[i] != " ":
			while s[i] != " ":
				myList.append(s[i])
				i += 1
				if i == len(s):
					break
			res.append(''.join(myList))
		else:
			i += 1
	res.reverse()
	print(' '.join(res))

s = " hello   world "
reverseWords(s)