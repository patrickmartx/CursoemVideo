# Cores no terminal
# \033[style:text:backm
# \033[0:33:44m
# Style: 0 = none | 1 = bold | 4 = underline | 7 = negative
# Text: 30 até 37
# Back: 40 até 47

print("\033[0:30:41mTeste\033[m de projeto")
print("\033[1:32mVerdadeiro\033[m ou \033[1:31mFalso\033[m")
nome = "Patrick"
print("Prazer em te conhecer, {}{}{}.".format('\033[1:34m', nome, '\033[m'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco': '\033[7:30m'
         }
print(f"Me mude de {cores['amarelo']}COR{cores['limpa']}")
