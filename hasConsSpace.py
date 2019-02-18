def isThisASpace(str, index):
	if (str[index] == " "):
		return true
	else:
		return false

def hasConsSpaces(str, index):
	if (isThisASpace(str, index) and isThisASpace(str, index+1)):
		return true
	else:
		false

def howManySpaces(str, index):
	n = 2
	if (isThisASpace(str, index+n)):
		while(isThisASpace(str,index+n)):
			n = n + 1
	return n

testString = "     " #5 spaces
n = len(testString)

for i in range(0,n):
	if (hasConsSpaces(testString, i)):
		print(howManySpaces(testString,i))

#comment