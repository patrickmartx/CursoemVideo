# Cores no terminal
# \033[style:text:backm
# \033[0:33:44m
# Style: 0 = none | 1 = bold | 4 = underline | 7 = negative
# Text: 30 até 37
# Back: 40 até 47
'''
   1 vermelho = '\033[31m'
   2 verde = '\033[32m'
   3 azul = '\033[34m'
   4
   5 ciano = '\033[36m'
   6 magenta = '\033[35m'
   7 amarelo = '\033[33m'
   8 preto = '\033[30m'
   9
  10 branco = '\033[37m'
  11
  12 restaura cor original = '\033[0;0m'
  13 negrito = '\033[1m'
  14 reverso = '\033[2m'
  15
  16 fundo preto = '\033[40m'
  17 fundo vermelho = '\033[41m'
  18 fundo verde = '\033[42m'
  19 fundo amarelo = '\033[43m'
  20 fundo azul = '\033[44m'
  21 fundo magenta = '\033[45m'
  22 fundo ciano = '\033[46m'
  23 fundo branco = '\033[47m'
'''
cores = {'limpa':'\033[m',
         'vermelho': '\033[31m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'magenta': '\033[35m',
         'ciano': '\033[36m',
         'branco': '\033[37m',

         'pretoebranco': '\033[7:30m'
         }

print("\033[0:30:41mTeste\033[m de projeto")
print("\033[1:32mVerdadeiro\033[m ou \033[1:31mFalso\033[m")
nome = "Patrick"
print("Prazer em te conhecer, {}{}{}.".format('\033[1:34m', nome, '\033[m'))
print(f"Me mude de {cores['amarelo']}COR{cores['limpa']}")
