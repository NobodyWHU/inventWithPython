#-*- encoding=utf-8 -*-
__author__ = 'Jeremy'

import pyperclip

#待加密的字符串
message = 'This is my secret message.'

#加解密钥值
key = 18

#告诉程序是加密还是解密
mode = 'encrypt'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#保存加密后或者解密后的结果
translated = ''

#初始化信息全转化为大写
message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        translated += LETTERS[num]
    else:
        translated += symbol

print(translated)