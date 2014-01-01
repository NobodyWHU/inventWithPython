__author__ = 'Jeremy'

import time, os, sys, transpositionDecrypt, transpositionClipher

def main():
    inputFilename = 'frankenstein.txt'

    outputFilename = 'frankenstein.encrypted.txt'
    myKey = 10
    myMode = 'encrypt'

    if not os.path.exists(inputFilename):
        print("the file %s does not exist.Quiting..." % (inputFilename))
        sys.exit()
    if os.path.exists(outputFilename):
        print("this will overwrite the file %s. (C)ontinue or (Q)uite?" % (outputFilename))
        response = raw_input('>')
        if not response.lower().startswith('c'):
            sys.exit()

    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionClipher.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s, characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))


if __name__ == "__main__":
    main()

