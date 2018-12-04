#Open text file to read
file = open('lotr.txt', 'r')
lines = file.readlines()

#Put words from text file into list
V = []
for word in lines:
    V.append(word.strip('\n'))

def longest_chain(V, chain=[], longest=[]):
	"""
	Take a list of words from external file and return the longest
	chain  of  words  that  meet  the  chaining  condition.

	ARGUMENTS:
	:param V: 		The word list
	:param chain:   our current chain of words
	:param longest: our current longest chain of words
	"""

	extended = False
	#Append the first word of each chain
	for word in V:
		if len(chain) == 0:
			chain.append(word)
			#Append chaining words that fit the chaining condition
			for words in V:
				if chain[-1][-1].lower() == words[0].lower():
					chain.append(words)
					extended = True
			#Declare longest chain, and save it in longest[]		
			if extended == True:
				if len(chain)>len(longest):
					longest.clear()
					for i in chain:
						longest.append(i)

			chain.clear()
	return longest
