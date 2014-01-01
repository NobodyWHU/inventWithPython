# coding=utf-8
__author__ = 'jeremy'
import math

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptMessage(myKey, myMessage)

    print(plaintext)

def decryptMessage(key, message):
    #加上float强制转换，不然会自动向下取整
    numOfColumns = math.ceil(len(message) / float(key))

    numOfRows = key
    numOfShadeBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = ['']*int(numOfColumns)

    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col +=1

        if (col == numOfColumns) or (col == numOfColumns-1 and row >= numOfRows - numOfShadeBoxes):
            col = 0
            row +=1
    return ''.join(plaintext)


if __name__ == "__main__":
    main()
