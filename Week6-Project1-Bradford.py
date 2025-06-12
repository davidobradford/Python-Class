plainText = input("Enter a line of plain text: ")
distance = int(input("Enter the distance value: "))

codestring = ""
listOfWords = plainText.split()

for word in listOfWords:
    code = ""
    for ch in word:
        ordValue = ord(ch)  
        if ordValue >= ord("!") and ordValue <= ord("~"):
            cipherValue = ordValue + distance
            if cipherValue > ord('~'):
                cipherValue = ord('!') + distance - \
                              (ord('~') - ordValue + 1)
            code += chr(cipherValue)
    if code != "":
        if codestring == "":
            codestring = code
        else:
            codestring = codestring + " " + code 

print(codestring)
