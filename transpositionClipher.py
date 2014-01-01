__author__ = 'Jeremy'

message = 'Common sense is not so common.'

key = 8
num = len(message)

def encryptMessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]

            pointer +=key

    return ''.join(ciphertext)



def main():
    rows = num // 10 +1
    translated = ''
    for j in range(key):
        for i in range(rows):
            flag = i*key+j
            if flag < num:
                translated += message[flag]

    print translated

if __name__ == "__main__":
    main()
