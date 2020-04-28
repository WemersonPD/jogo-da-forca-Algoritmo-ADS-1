def vermelho(a):
    return '\033[31;1m' + a + '\033[0;0m'

def verde(a):
    return '\033[32;1m' + a + '\033[0;0m'


def azul(a):
    return '\033[34;1m' + a + '\033[0;0m'

def amarelo(a):
    return '\033[93;1m' + a + '\033[0;0m'

def inverte(a):
    return '\033[1;7m' + a + '\033[0;0m'

'''
fundo preto = '\033[40m'
  17 fundo vermelho = '\033[41m'
  18 fundo verde = '\033[42m'
  19 fundo amarelo = '\033[43m'
  20 fundo azul = '\033[44m'
  21 fundo magenta = '\033[45m'
  22 fundo ciano = '\033[46m'
  23 fundo branco = '\033[47m'


  Preto	\033[1;30m	\033[1;40m
Vermelho	\033[1;31m	\033[1;41m
Verde	\033[1;32m	\033[1;42m
Amarelo	\033[1;33m	\033[1;43m
Azul	\033[1;34m	\033[1;44m
Magenta	\033[1;35m	\033[1;45m
Cyan	\033[1;36m	\033[1;46m
Cinza Claro	\033[1;37m	\033[1;47m
Cinza Escuro	\033[1;90m	\033[1;100m
Vermelho Claro	\033[1;91m	\033[1;101m
Verde Claro	\033[1;92m	\033[1;102m
Amarelo Claro	\033[1;93m	\033[1;103m
Azul Claro	\033[1;94m	\033[1;104m
Magenta Claro	\033[1;95m	\033[1;105m
Cyan Claro	\033[1;96m	\033[1;106m
Branco	\033[1;97m	\033[1;107m
Negrito	\033[;1m	-
Inverte	\033[;7m	-
Reset (remove formatação)	\033[0;0m	-
'''
