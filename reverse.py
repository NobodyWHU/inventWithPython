__author__ = 'Jeremy'

#Reverse Clipher

message = 'Three can keep a secret, if two of them are dead.'
translated = ''

i = len(message)-1
while i >= 0:
    translated = translated + message[i]
    i -=1

print translated

#another way to reverse the string
print message[::-1]
