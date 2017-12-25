import numpy as np

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

###mod 26
def encryptVigenere(gamma, text):
    textLen = len(text)
    gammaLen = len(gamma)

    # Формируем ключевое слово(растягиваем гамму на длину текста)
    keyText = []
    for i in range(textLen // gammaLen):
        for symb in gamma:
            keyText.append(symb)
    for i in range(textLen % gammaLen):
        keyText.append(gamma[i])

    # Шифрование
    code = []
    for i in range(textLen):
        code.append(alphabet[(alphabet.index(text[i]) + alphabet.index(keyText[i])) % 26])

    return ''.join(code)


def decryptVigenere(gamma, code):
    codeLen = len(code)
    gammaLen = len(gamma)

    # Формируем ключевое слово(растягиваем гамму на длину текста)
    keyText = []
    for i in range(codeLen // gammaLen):
        for symb in gamma:
            keyText.append(symb)
    for i in range(codeLen % gammaLen):
        keyText.append(gamma[i])

    # Расшифровка
    text = []
    for i in range(codeLen):
        text.append(alphabet[(alphabet.index(code[i]) - alphabet.index(keyText[i]) + 26) % 26])

    return ''.join(text)

def encryptCaesar(key, text):
    code = []
    for i in range(len(text)):
        code.append(alphabet[(alphabet.index(text[i]) + int(key)) % 26])

    return ''.join(code)


def decryptCaesar(key, code):
    text = []
    for i in range(len(code)):
        text.append(alphabet[(alphabet.index(code[i]) - int(key)) % 26])

    return ''.join(text)


if __name__ == "__main__":

    asd=[]
    for i in range (ord("A"),ord("z")):
        for j in range(ord("A"),ord("z")):
            asd.append((i+j))
        asd.append("\n")

    print(asd)







