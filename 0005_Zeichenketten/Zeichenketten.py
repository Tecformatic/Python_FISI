# Imports

# Functions


def countWords(inputSTR: str):
    words = inputSTR.split(" ")
    return len(words)

def getNumbers(inputSTR: str):
    tmp = ""
    for i in inputSTR:
        if i.isnumeric():
            tmp = tmp + i
    return tmp

def checkPalindrom(inputSTR: str):
    if inputSTR.upper() == inputSTR[::-1].upper():
        return True
    else:
        return False

def genPassword(startValue: str):
    pw = ""
    tmpctr = True
    words = startValue.lower().split(" ")
    for i in range(0, len(words)):
        if i % 2 != 0:
            pw += words[i][0].upper()
        else:
            pw += words[i][0].lower()
    return pw.replace("e", "3").replace("E", "3").replace("o", "0").replace("O", "0")


    
            
# Code
satz = str(input("Bitte Satz eingeben: "))
print(f"Anzahl Wörter: {countWords(satz)}")

numB = str(input("Zeichenkette mit Zahlen: "))
print(f"Zahlen Plain: {getNumbers(numB)}")

palinput = str(input("Palindrome Check: "))
print(f"Is Palindrome: {checkPalindrom(palinput)}")

pw = str(input("Sentence for PW: "))
print(f"PW: {genPassword(pw)}")

