frase = input ("introduce una frase: ")
vocal = input ("introduce una vocal: ")

vocalmay = vocal.upper()
frasemay = frase.replace(vocal, vocalmay)

print(frasemay)
