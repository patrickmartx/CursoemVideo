# Manipulando cadeias de texto

frase = "curso em vídeo python"

print(frase[9:])

print(len(frase))

print(frase.count('o',0,13))

print(frase.find('o'))

print('curso' in frase)

print(frase.replace('python', 'android'))

print(frase.upper())

print(frase.capitalize())

print(frase.title())

lista = frase.split()
print('-'.join(lista))

print(lista)

print('='*30)

frase2 = '   Aprenda Python  '

print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())