# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
import urllib.request
from utils.data import imprimir

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    imprimir('Não é possível abrir este site. Cheque sua conexão ou a existência do mesmo.', 1)
except Exception as erro:
    imprimir(f'O site não está acessível no momento, erro {erro.__class__}', 3)
else:
    imprimir('Consegui abrir o site com sucesso!', 2)
    # print(site.read())
