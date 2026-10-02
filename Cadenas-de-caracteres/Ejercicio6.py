frase = input ("introduce una frase: ")
vocal = input ("introduce una vocal: ")

vocalmin = vocal.lower()
vocalmay = vocal.upper()

frasemay = frase.replace(vocalmin, vocalmay)

print(frasemay)
