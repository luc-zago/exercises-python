
def maiusculas(string):
    newString = ''
    for letra in string:
        if (ord(letra) > 64 and ord(letra) < 91):
            newString += letra
    return newString
