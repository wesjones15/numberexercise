# takes in phone number
# convert number into array
# convert each number into 3 possible letters
# find words from the letters
import itertools

wordFile = open('words.txt', 'r')
lines = wordFile.read().split()

def sentence_maker(phoneNumber):
    numberList = [int(d) for d in str(phoneNumber)]
    letterList = ["", "", ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
    for i in range (len(numberList)):
        numberList[i] = letterList[int(numberList[i])]
    numberList = filter(None, numberList)

    convList = []
    for j in itertools.product(*numberList):
        strWord = ''
        for k in range(len(j)):
            strWord += j[k]
        convList.append(strWord)
    wordList = []
    actualWordList = []
    for l in range(len(convList)):
        for m in range(len(lines)):
            if lines[m] in convList[l] and len(lines[m]) > 1:
                wordList.append(convList[l])
                actualWordList.append(lines[m])
    # return convList
    # return wordList
    return set(actualWordList)
