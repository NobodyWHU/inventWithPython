#-*- encoding=utf-8 -*-
__author__ = 'jeremy'


#英语字母的出现平率
englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

#字母按照出现平率排序
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

#英语字母
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


#统计文本中各字母出现的次数，返回字典，字母作为key，出现次数作为值
def getLetterCount(message):
    letterCount = {}
    for letter in LETTERS:
        letterCount[letter] = 0
    for letter in message:
        letter = letter.upper()
        if letter in LETTERS:
            letterCount[letter] +=1

    return letterCount

#得到元组的第一项
def getItemIndexZero(tup):
    return tup[0]

#得到按照频率排序的字典，出现次数作为key，对应的字母作为值
#可能多个字母拥有相同的频率，因此值为列表形式
def getFrequencyOrder(message):
    letterToFreq = getLetterCount(message)
    freqToLetter = {}
    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]] = [letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter)
    #对每一个频率下的字母列表进行排序，排序规则为英语字母出现频率
    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

    #将字典中的键值对转为元组，方便排序，字典中没有顺序
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemIndexZero, reverse=True)

    #抽取排序后的字母，组成字符串
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])

    return ''.join(freqOrder)

#计算有多少个是符合原有规律的
def englishFreqMatchScore(message):
    freqOrder = getFrequencyOrder(message)

    matchScore = 0
    for common in ETAOIN[0:6]:
        if common in freqOrder[0:6]:
            matchScore += 1
    for uncommon in ETAOIN[-6]:
        if uncommon in freqOrder[-6]:
            matchScore +=1

    return matchScore


if __name__ == "__main__":
    print "testing"
    teststring = "eeeeeeeeeeeddddas"
    print englishFreqMatchScore(teststring)
