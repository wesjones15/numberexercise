# takes in phone number
# convert number into array
# convert each number into 3 possible letters
# find words from the letters

def sentence_maker(phoneNumber):
    numberList = [int(d) for d in str(phoneNumber)]
    letterList = ["", "", ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
    for i in range (len(numberList)):
        numberList[i] = letterList[int(numberList[i])]
    numberList = filter(None, numberList)



    # convList = []
    # for i in range(len(numberList)): # length of num / 2
    #     # convList.append(numberList[i][])
    #     for j in range(len(numberList[i])): # length of lett / 3,3
    #         # convList.append(numberList[i][j])
    #
    #         for k in range(i+1,len(numberList)):
    #             convList.append(numberList[i][j])
    #             for l in range(len(numberList[i])):
    #                 convList.append(numberList[k][l])
    #
    #                 print convList
    #                 convList = []
            # k += 1
            # if k >= len(numberList): k = i
                # convList.append(numberList[k][j])


    return numberList