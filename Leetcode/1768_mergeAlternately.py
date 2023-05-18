def mergeAlternately(word1, word2):
	length = max(len(word1), len(word2))
	myList = []
	for i in range(length):
		if i >= len(word1):
			myList.append(word2[i])
			continue
		if i >= len(word2):
			myList.append(word1[i])
			continue
		else:
			myList.append(word1[i])
			myList.append(word2[i])
	return(''.join(myList))

word1 = "abcd"
word2 = "pq"
print(mergeAlternately(word1, word2))