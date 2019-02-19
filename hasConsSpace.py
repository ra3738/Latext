#Checks if current index is a space, returns boolean
def isThisASpace(str, index):
	if (str[index] == " "):
		return True
	else:
		return False

#Checks if current index and next index are spaces, returns boolean
#If at second last index, returns false

def hasConsSpaces(str, index):
	if (index + 1 < len(str)):
		if (isThisASpace(str, index) and isThisASpace(str, index+1)):
			return True
		else:
			return False
	else:
		return False

#Counts no. of consecutive spaces, returns int
def howManySpaces(str, index):
	length = len(str)
	index = index
	n = 0
	while (index < length):
		if (isThisASpace(str,index)):
			n = n + 1
			index = index + 1
		else:
			return n
	return n 

#replaces spaces number of indices after and including index with strToReplaceWith
#Returns string
def replaceSpaces(strToReplace, index, strToReplaceWith, spaces):
	strList = list(strToReplace)
	while (not(spaces== 0)):
		strList[index] = strToReplaceWith
		index = index + 1
		spaces = spaces - 1
	return "".join(strList)

testString = "  m  m " 

i = 0
while (i < len(testString)):
	if (hasConsSpaces(testString, i)):
		j = howManySpaces(testString, i)
		print(j)
		testString = replaceSpaces(testString, i, "", j)
		i = i + j - 1
	else:
		i = i + 1

print(testString)
#comment