from collections import Counter
import re
def makeBigram(corpus):
	bigramList = []
	bigramCount = {}
	unigramCount = {}
	for i in range(len(corpus)-1):
		bigramList.append((corpus[i], corpus[i+1]))
		if (corpus[i], corpus[i+1]) in bigramCount:
			bigramCount[(corpus[i], corpus[i+1])] += 1
		else:
			bigramCount[(corpus[i], corpus[i+1])] = 1
	for word in corpus:
		if word in unigramCount:
			unigramCount[word] += 1
		else:
			unigramCount[word] = 1
	return bigramList, bigramCount, unigramCount

def noSmoothing(bigramList, bigramCount, unigramCount):
	probList = {}
	for bigram in bigramList:
		word1 = bigram[0]
		word2 = bigram[1]
		probList[bigram] = (bigramCount[bigram])/(unigramCount[word1])
	file = open('noSmoothing.txt', 'w')

	for bigram in bigramList:
		file.write("Bigram: "+str(bigram) + '\n' "Count: "+ str(bigramCount[bigram])
				   + '\n' +"Probability: " + str(probList[bigram]) + '\n')
	return probList

def addOneSmoothing(bigramList, bigramCount, unigramCount):
	probList = {}
	cStar = {}
	for bigram in bigramList:
		word1 = bigram[0]
		word2 = bigram[1]
		probList[bigram] = (bigramCount[bigram] + 1)/(unigramCount[word1] + len(unigramCount))
		cStar[bigram] = ((bigramCount[bigram] + 1)*unigramCount[word1]) / (unigramCount[word1] + len(unigramCount))
	file = open('addOneSmoothing.txt', 'w')
	for bigram in bigramList:
		file.write("Bigram: "+str(bigram) + '\n' "Count: "+ str(cStar[bigram])
				   + '\n' +"Probability: " + str(probList[bigram]) + '\n')
	return probList, cStar 

def goodTuringDiscounting(bigramList, bigramCount, totalBigram):
	bucket = {}
	bucketList = {}
	cStar = {}
	pStar = {}
	probList = {}
	countList = {}
	for value in bigramCount.values():
		if value not in bucket:
			bucket[value] = 1
		else:
			bucket[value] += 1

	bucketList = sorted(bucket.items(), key = lambda t: t[0])
	#N1/N
	probZero = bucketList[0][1]/totalBigram    
	lastItem = bucketList[-1][0]
	#creating all the buckets from 1 to lastItem
	for i in range(1, lastItem):
		if i not in bucket:
			bucket[i] = 0

	bucketList = sorted(bucket.items(), key = lambda t: t[0])
	bucketLength =len(bucketList)
	i = 1
	for key, value in bucketList:
		if i <bucketLength-1:
			if value == 0:
				cStar[key] = 0
				pStar[key] = 0
			else:
				cStar[key] = (i+1)*(bucketList[i][1])/value
				pStar[key] = cStar[key]/totalBigram
		else:
			cStar[key] = 0
			pStar[key] = 0
		i+= 1
	for bigram in bigramList:
		probList[bigram] = pStar[bigramCount[bigram]]
		countList[bigram] = cStar[bigramCount[bigram]]
	file = open('goodTuringDiscounting.txt', 'w')

	for bigram in bigramList:
		file.write("Bigram: "+str(bigram) + '\n' "Count: "+ str(countList[bigram])
				   + '\n' +"Probability: " + str(probList[bigram]) + '\n')

	file.close()
	return probList, probZero, countList

	
#-----------------------------Main-------------------------------------
if __name__ == '__main__':
	fileName = 'HW2_S18_NLP6320-NLPCorpusTreebank2Parts-CorpusA-Unix.txt'
	corpus = []
	file = open(fileName, "r")
	text = file.read()
	for word in text.split():
		corpus.append(word)

	file.close()
	bigramList, bigramCount, unigramCount = makeBigram(corpus)
	bigramProb_ns = noSmoothing(bigramList, bigramCount, unigramCount)
	bigramProb_aos, addOneCStar = addOneSmoothing(bigramList, bigramCount, unigramCount)
	bigramProb_gt, probZero, countList = goodTuringDiscounting(bigramList, bigramCount, len(bigramList))


	test = "The president wants to control the board \'s control"
	print("Testing for Sentence: ", test)
	test = test.split() 
	bigramTest = []

	print("No smoothing calculation...")

	prob_ns = 1
	for i in range(1, len(test)):
		bigramTest.append((test[i-1], test[i]))
	for i in range(len(bigramTest)):
		if bigramTest[i] in bigramProb_ns:
			print("Probability of ", bigramTest[i], " is ", bigramProb_ns[bigramTest[i]])
			prob_ns *= bigramProb_ns[bigramTest[i]]
		else:
			print("Probability of ", bigramTest[i], " is ", 0)
			prob_ns *= 0
	print("No smoothing: ", prob_ns)
	print("\n")

	print("Add one smoothing calculation...")
	count = Counter(corpus)
	v = len(count)
	wordCount = {} #{token:{token: count}....		}
	for word1 in test:
		w = {}
		for word2 in test:
			w[word2]=len(re.findall(word1+' '+word2,text))
		wordCount[word1] = w
	prob_aos = 1
	for i in range(1,len(test)):
		prob = ((wordCount[test[i-1]][test[i]] + 1) / (sum(wordCount[test[i-1]].values()) + v)) 
		print("Probability of ", (test[i-1], test[i]), " is ", prob)
		prob_aos = prob_aos * prob

	print("Add one smoothing: ", prob_aos)
	print("\n")

	print("Good Turing calculation...")
	prob_gt = 1
	for i in range(len(bigramTest)):
		if bigramTest[i] in bigramProb_gt:
			print("Probability of ", bigramTest[i], " is ", bigramProb_gt[bigramTest[i]])
			prob_gt *= bigramProb_gt[bigramTest[i]]

		else:
			print("Probability of ", bigramTest[i], " is ", probZero)
			prob_gt *= probZero
	print("Good turing discounting probability: ", prob_gt) 

	
