# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9. | B) Em que posição foi digitado o primeiro valor 3. | C) Quais foram os números pares

valorUm = int(input("Digite um número: "))
valorDois = int(input("Digite outro número: "))
valorTres = int(input("Digite mais um número: "))
valorQuatro = int(input("Digite o último número: "))

tuplaNumeros = (valorUm, valorDois, valorTres, valorQuatro)
pares = 0
for i in range(0, len(tuplaNumeros)):
    if tuplaNumeros[i] % 2 == 0:
        pares += 1



print(f"Você digitou os valores {tuplaNumeros}\n"
      f"O valor 9 aparece {tuplaNumeros.count(9)} vezes\n"
      f"O valor 3 apareceu na {tuplaNumeros.index(3)+1}ª posição\n"
      f"Os valores pares digitados fora {pares}")