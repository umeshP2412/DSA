# Python3 program for the above approach

# Function to check if the
# character c is in lowercase or not
def isLower(c):
	return ord(c) >= ord('a') and ord(c) <= ord('z')

# Function to check if the
# character c is in uppercase or not
def isUpper(c):
	return ord(c) >= ord('A') and ord(c) <= ord('Z')

# Utility function to check if uppercase
# characters are used correctly or not
def detectUppercaseUseUtil(S):

	# Length of string
	N = len(S)
	i = 0

	# If the first character is in lowercase
	if (isLower(S[0])):
		i = 1
		while (S[i] and isLower(S[i])):
			i += 1
		return True if (i == N) else False

	# Otherwise
	else:
		i = 1

		# Check if all characters
		# are in uppercase or not
		while (S[i] and isUpper(S[i])):
			i += 1

		# If all characters are
		# in uppercase
		if (i == N):
			return True
		elif (i > 1):
			return False

		# Check if all characters except
		# the first are in lowercase
		while (S[i] and isLower(S[i])):
			i += 1
		return True if (i == N) else False

# Function to check if uppercase
# characters are used correctly or not
def detectUppercaseUse(S):

	# Stores whether the use of uppercase
	# characters are correct or not
	check = detectUppercaseUseUtil(S)

	# If correct
	if (check):
		print("Yes")
	# Otherwise
	else:
		print ("No")

# Driver Code
if __name__ == '__main__':

	# Given string
	S = "GeeKs"

	# Function call to check if use of
	# uppercase characters is correct or not
	detectUppercaseUse(S)

# This code is contributed by mohit kumar 29.
