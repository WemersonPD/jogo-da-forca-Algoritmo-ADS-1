frutas = ['MANGA','UVA','LARANJA','MORANGO','MAÇA','MARACUJA']
nomes = ['KEMILY', 'JOICE', 'WEMERSON', 'FERNANDO','FLAVIO', 'LUCAS', 'KESLEY']
objetos = ['LAPIS','CANETA', 'CELULAR','TECLADO']
import os
#pra sempre ter frutas.txt
tema_padrao1 = open('banco_de_dados/computador/frutas.txt', 'w')
tema_padrao1.close()
tema_padrao1 = open('banco_de_dados/computador/frutas.txt', 'a')
for i in frutas:
    a = i + '\n'
    tema_padrao1.write(a)
tema_padrao1.close()

#Para sempre ter nomes.txt
tema_padrao2 = open('banco_de_dados/computador/nomes.txt', 'w')
tema_padrao2.close()
tema_padrao2 = open('banco_de_dados/computador/nomes.txt', 'a')
for i in nomes:
    a = i + '\n'
    tema_padrao2.write(a)
tema_padrao2.close()

#Para sempre ter objetos.txt
tema_padrao3 = open('banco_de_dados/computador/objetos.txt', 'w')
tema_padrao3.close()
tema_padrao3 = open('banco_de_dados/computador/objetos.txt', 'a')
for i in nomes:
    a = i + '\n'
    tema_padrao3.write(a)
tema_padrao3.close()

#Para o nosso sistema de cores nas palavras
from sistema_de_cores.cores import vermelho, verde, amarelo, azul, inverte
#Para mostra os arquivos que estão dentro de uma determinada pasta
from glob import glob
from random import choice
sistema_de_pontos = 0
def url_temas():
    
    #Pega cada elemento qSue está dentro do diretorio informado e retorna uma lista com cada elemento
    url_temas = glob('banco_de_dados/computador/*.txt')

    #Por url_temas mostra todo o caminho de  cada arquivo, foi necessário manipular o conteúdo de cada elemento da lista
    
    for i in range(len(url_temas)):
        #Corta a parte do diretorio por meio de manipulação de str, ex: banco_de_dados/computador/
        tema = url_temas[i][26:]
        #"Tira a extesão" do arquivo, ex: frutas.txt, resultado: FRUTAS
        tema = tema.replace(".txt", "").upper()
        #Escreve cada tema
        print(i + 1, amarelo(tema))
        

def tema_escolhido():
    escolha_tema = int(input(verde('ESCOLHA: ')).strip()) #Pode apresentar erro caso seja informado uma str que não possa ser convertido, tenho que tratar
    todos = glob('banco_de_dados/computador/*.txt') 
    escolha = escolha_tema
    #Falta o erro pra quando digitar um tema que não exista
    #Para caso seja digitado um valor não apropriado
  

    '''while True:
        for i in range(1, len(todos) + 1):
            if i == escolha:
                escolha = -1
                break
            elif i+1 != escolha:
                escolha = 0
        if escolha == -1:
            break
        elif escolha == 0:
            print(vermelho('OPÇÃO INVÁLIDA!'))
            escolha_tema = int(input(verde('ESCOLHA: ')).strip())
            escolha = escolha_tema'''

    for i in range(escolha_tema):
        if i + 1 == escolha_tema:
            url = str(todos[i])
            arquivo = open(url, 'r')
            
            opcoes = []
            for opcao in arquivo:
                opcoes.append(opcao.strip())
    print(escolha_tema)
    return opcoes
    
    

    arquivo.close()
#Titulo
print(amarelo('JOGO DA FORCA'))

#Opção do jogo (jogar, adm, sair)
opções = input(verde('1 - JOGAR, 2 - MODO ADMINISTRADOR, 3 - SAIR, 4 - INFORMAÇÕES: '))
#Caso a opção seja inválida
while not(opções == '1' or opções == '2' or opções == '3'):
    print(vermelho('OPÇÃO INVÁLIDA'))
    opções = input(verde('1 - JOGAR, 2 - MODO ADM, 3 - SAIR, 4 - INFORMAÇÕES: : '))

#Caso o usuario queira jogar apenas com o nosso banco de dados
if opções == '1':
    #Função com todos os url_temas
    print(amarelo('QUE OS JOGOS COMECEM'))
    print(amarelo('ESCOLHA UM DOS TEMA:'))
    url_temas()
    
    
    def jogar():
        traço = []
        global sistema_de_pontos
        palavra_secreta = choice(tema_escolhido()).upper().strip()
        
        print(amarelo('ESCOLHA UMA DIFICULDADE:'))
        nivel = input(verde('1 - FÁCIL, 2 - MEDIO, 3 - DIFICIL: ')).strip()
        while not(nivel == '1' or nivel == '2' or nivel == '3'):
            print(vermelho('RESPOSTA INVÁLIDA!'))
            nivel = input(verde('1 - FÁCIL, 2 - MEDIO, 3 - DIFICIL: ')).stript()
        if (nivel == '1'):
            tentativa = 8
        elif (nivel == '2'):
            tentativa = 6
        elif (nivel == '3'):
            tentativa = 4
        
        print(azul('VOCÊ TEM DIREITO A %i ERROS'%tentativa))
        

        print(amarelo('VOCÊ TEM %i PONTOS'%sistema_de_pontos ))
        for i in palavra_secreta:
            traço.append('_')

        print(amarelo('Acerte a palavra: ')) #Quero colocar uma funçao de informações aqui
        print(amarelo(str(traço)))
        letra = input(verde('DIGITE UMA LETRA: ')).upper().strip()
        
        lista_palavra_secreta = list(palavra_secreta)
        letra_antiga = []
        palavra_correta = 0
        while True: 
            if tentativa == 0:
                print('GAME OVER!')
                palavra_correta = 0
                break

            if(letra in palavra_secreta and tentativa > 0):
                index = 0
                print(azul('ACERTOU'))
                if letra_antiga == []:
                    sistema_de_pontos += 10
                else:
                    for i in range(len(letra_antiga)):
                        if letra_antiga[i] == letra:
                            repetida = 1
                            break
                        else:
                            repetida = 0
                    if repetida == 0:
                        sistema_de_pontos += 10
                    else:
                        print(vermelho('LETRA REPETIDA!'))

                        

                print(amarelo('VOCÊ TEM %i PONTOS'%sistema_de_pontos ))
                for procura in palavra_secreta:
                    index += 1
                    if procura == letra:
                        traço[index-1] = letra
                print(amarelo(str(traço)))
                
                if traço == lista_palavra_secreta:
                    print(amarelo('PALAVRA CORRETA '))
                    palavra_correta = 1
                    break
                letra_antiga = letra
                letra = input(verde('DIGITE UMA LETRA: ')).upper().strip()
            else:
                print(vermelho('ERROU'))
                tentativa -= 1
                sistema_de_pontos -= 10
                print(amarelo('VOCÊ TEM %i PONTOS'%sistema_de_pontos ))
                print(vermelho('VOCÊ TEM DIREITO A MAIS %i ERROS'%tentativa))
                letra = input(verde('DIGITE UMA LETRA: ')).upper().strip()
        
        if palavra_correta == 1:
            print(amarelo('Você quer jogar novamente? (1 - SIM, 2 - NÃO'))
            resposta = int(input(amarelo('RESPOSTA: ')))
            if resposta == 1:
                print(amarelo('VAMOS CONTINUAR!'))
                url_temas()
                jogar()
            if resposta == 2:
                print(amarelo('OK, VAMOS PARAR!'))
                

    jogar()



if opções == '2':
    print(amarelo('MODO ADMINISTRADOR'))
    def ADMINISTRADOR():
        print(amarelo('1 - APAGAR TEMA, 2 - CRIAR/ALTERAR TEMA, 3 - ADD PALAVRA A UM TEMA'))
        adm = int(input(verde('Escolha: ')))
        while not(adm == 1 or adm == 2 or adm == 3):
            print('OPÇÃO INVÁLIDA!')
            print(amarelo('1 - APAGAR TEMA, 2 - CRIAR/ALTERAR TEMA, 3 - ADD PALAVRA A UM TEMA'))
            adm = int(input(verde('ESCOLHA')))
        
        print(amarelo('O SISTEMA TEM OS TEMAS: '))
        url_temas()
        
        #Para apagar tema:
        if adm == 1:
            url = glob('banco_de_dados/computador/*.txt')
            escolha = int(input((verde('ESCOLHA: '))))
            for i in range(len(url)):
                if i+1 == escolha:
                    
                    os.remove(url[i])
    
                #Falta ainda
        
        #Para add tema, dizendo o nome dele
        if adm == 2:
            
            print(vermelho('OBS: SE VOCÊ COLOCAR O NOME DE UM TEMA JÁ EXISTENTE, ELE SERÁ REESCRITO!'))
            nome_tema = input(verde('Digite o nome do novo tema: ')).upper()

            dir_mais_nome_tema = 'banco_de_dados/computador/' + nome_tema + '.txt'
            new_tema = open(dir_mais_nome_tema, 'a')
            print(azul('O NOME DO NOVO TEMA É: '),nome_tema)
            new_tema.close()

            def nova_palavra():
                print(amarelo('AGORA VAMOS COLOCAR UMA PALAVRA NESTE TEMA!'))
                print(vermelho('OBS: ESCREVA APENAS UMA PALAVRA SEM ESPAÇO!'))
                new_tema = open(dir_mais_nome_tema, 'a')
                new_palavra = input(verde('DIGITE UMA PALAVRA PARA SER INCLUIDA NO TEMA: ').strip().upper())
                new_palavra = new_palavra + '\n'
                new_tema.write(new_palavra)
                new_tema.close()
            nova_palavra()

            def lista_de_elementos():
                new_tema = open(dir_mais_nome_tema, 'r')
                opcoes = []
                for conteudo in new_tema:
                    opcoes.append(conteudo.strip())
                
                print(amarelo('o tema %s tem:')%nome_tema, opcoes, amarelo('como opção(ões)'))
                new_tema.close()
            lista_de_elementos()
            
            print(verde('VOCÊ QUER ADICIONAR MAIS PALAVRAS AO TEMA?'))
            request = input(amarelo('1 - SIM, 2 - NÃO'))
            while not(request == '1' or request == '2'):
                print(vermelho('OPÇÃO INVÁLIDA!'))
                print(verde('VOCÊ QUER ADICIONAR MAIS PALAVRAS AO TEMA?'))
                request = input(amarelo('1 - SIM, 2 - NÃO'))
            
            if request == '1':
                while request == '1':
                    nova_palavra()
                    lista_de_elementos()
                    print(verde('VOCÊ QUER ADICIONAR MAIS PALAVRAS AO TEMA?'))
                    request = input(amarelo('1 - SIM, 2 - NÃO'))
                    while not(request == '1' or request == '2'):
                        print(vermelho('OPÇÃO INVÁLIDA!'))
                        print(verde('VOCÊ QUER ADICIONAR MAIS PALAVRAS AO TEMA?'))
                        request = input(amarelo('1 - SIM, 2 - NÃO'))
                    if request == 2:
                        break
                print(azul('OK!'))
            else:
                print(azul('OK!'))
        
    ADMINISTRADOR()




 
          
        
        

    


    
