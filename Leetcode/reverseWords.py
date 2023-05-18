def reverseWords(s):
	i = 0
	res = []
	while i < len(s):
		myList = []
		if s[i] != " ":
			while s[i] != " " and i <= len(s) - 1 :
				myList.append(s[i])
				i += 1
			res.append(''.join(myList))
		else:
			i += 1
	res.reverse()
	print(' '.join(res))

s = " asdasd df f"
reverseWords(s)