import sys

if len(sys.argv) < 2:
	print 'Not enough command-line arguments. Enter the file name as an argument.'
else:

	# Load the file into RAM
	with open(sys.argv[1]) as f:
	    content = f.readlines()

	# Variables for counting the characters
	characterTotal = 0
	spacesTotal = 0
	tabsTotal = 0
	commentedCharactersTotal = 0

	# To keep track of whether a /**/ style comment is active
	multiLineComment = False

	# For every line in the file
	for i in content:
		# For keeping track of whether a // comment is active. Resets each line.
		singleLineComment = False

		# For every character on this line
		for charIndex in range(len(i)):
			if i[charIndex] == ' ':
				spacesTotal += 1
			elif i[charIndex] == '\t':
				tabsTotal += 1

			# Checks position in line to prevent the code from using an invalid index
			elif i[charIndex] == '/' and charIndex + 1 < len(i):
				if i[charIndex + 1] == '/':
					singleLineComment = True
				elif i[charIndex + 1] == '*':
					multiLineComment = True

			elif i[charIndex] == '*' and charIndex + 1 < len(i) and i[charIndex + 1] == '/':
				multiLineComment = False
				commentedCharactersTotal += 2

			# Ignore first character of windows new lines ('\r\n')
			if i[charIndex] != '\r' or charIndex + 1 >= len(i) or i[charIndex + 1] != '\n':
				# Do not count newlines as comment characters
				if (singleLineComment or multiLineComment) and i[charIndex] != '\n':
					commentedCharactersTotal += 1

				characterTotal += 1

	# Output statistics. Percentages are given to 2 decimal places

	print 'In the file ' + sys.argv[1] + ' there are ' + str(characterTotal) + ' characters in total'

	print 'Of these characters,\n%d are spaces (%.2f%%)' % (spacesTotal, ((spacesTotal / float(characterTotal)) * 100.0))

	print '%d are tabs (%.2f%%)' % (tabsTotal, ((tabsTotal / float(characterTotal)) * 100.0))

	print 'and %d are commented out (%.2f%%)' % (commentedCharactersTotal, ((commentedCharactersTotal / float(characterTotal)) * 100.0))

	print ''
