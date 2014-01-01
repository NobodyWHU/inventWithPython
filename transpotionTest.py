# coding=utf-8
__author__ = 'Jeremy'

import random, sys, transpositionClipher, transpositionDecrypt

def main():
    random.seed(40)

    for i in range(20):
        #初始化带测试的字符串
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        message = list(message)
        random.shuffle(message)
        message = ''.join(message)

        print('Test #%s:  "%s..."' % (i+1, message))

        for key in range(1, len(message)):
            encrypted = transpositionClipher.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            if message != decrypted:
                print("Mismatch with key %s and message %s." % (key, message))
                print(decrypted)
                sys.exit()
    print("Transposition cipher test passed")


if __name__ == "__main__":
    main()

