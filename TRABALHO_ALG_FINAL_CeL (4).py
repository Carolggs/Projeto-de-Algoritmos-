###################################################################### FUNÇÕES USADAS NO PROGRAMA

#Função para ver se o arquivo realmente existe
def existe_arquivo(sala):
    import os
    if os.path.exists(sala):
        return True
    else:
        return False



    

#funçao pra ver se as coisas existem
def existe(dic,chave):
    if chave in dic.keys():
        return True
    else:
        return False



    

#Função para ver se é inteiro

def inteiro (valor):
    positivo = False
    num = 0
    while True:
        n = str(input(valor))
        if n.isnumeric():
            num = int(n)
            positivo = True
        else:

            print()
            print("\n O valor digitado não é válido! Digite um número INTEIRO \n")
        if positivo:
            return(num)





#Função para ver se realmente é uma palavra 
def TemEspaco (l):
        
    if l[0]== "":
    
        while l[0] == "" :
            print()
            print(" ERRO! você digitou vazio\n")
            
            n1= input("Digite novamente: ")
           
            y=n1.replace("-", "")
            x=y.replace(".", "")
            w=x.replace(",", "")
            l[0]= w

          
           
    

        
            while l[0].isnumeric() == True:
                    print()
                    print(" ERRO! você digitou um número\n")
                    n1= input("Digite novamente: ")
                    y=n1.replace("-", "")
                    x=y.replace(".", "")
                    w=x.replace(",", "")
                    l[0]= w

                   

                    
                   
               
    
    
    if l[0].isnumeric() == True:
            while l[0].isnumeric() == True:
                print()
                print(" ERRO! você digitou um número\n")
                n= input("Digite novamente: ")
                y=n.replace("-", "")
                x=y.replace(".", "")
                w=x.replace(",", "")
                l[0]= w

                
             

                while l[0] == "" :
                    print()
                    print(" ERRO! você digitou vazio\n")
                    n1= input("Digite novamente: ")
                    y=n1.replace("-", "")
                    x=y.replace(".", "")
                    w=x.replace(",", "")
                    l[0]= w

    
         
        
                    
                    
    return l[0]





#Função para ver se o nome já existe

def conferindo(arm, nome):
    listona=[]
    for itens in arm.values():
    
        listona.append(itens)
    
    for i in listona:
    
        for indice in i:
        
            if indice == nome[0]:
                while indice == nome[0]:
                    li=[]
                    num=input("o nome que você digitou já existe, digite novamente: ")
                    y=num.replace("-", "")
                    x=y.replace(".", "")
                    w=x.replace(",", "")
                    li.append(w)
                    TemEspaco(li)
                    
                    nome[0]= li[0]
               
            
               
    return nome[0]












#Função volta
        
def volta():
    input(" Tecle <ENTER> ")



def existe_arquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False






######################################################################### CRUD1- SALAS #################################################################################
#FUNÇÃO DE INSERIR

def incluir(arm, Sala ):

        N = arm.get(Sala)
        if N == None:
            listaNome=[]
            nome= input("Digite o nome: ").lower()
            y=nome.replace("-", "")  
            k=y.replace(".", "")
            w=k.replace(",", "")

            listaNome.append(w)
            TemEspaco(listaNome)
            conferindo(arm,listaNome)
            

            
            capacidade=inteiro("Digite a capacidade da sala: ")
            

            listaTipo=[]
            tipo= input("Digite o tipo de exibição: ")
            
            y=tipo.replace("-", "")  
            k=y.replace(".", "")
            w=k.replace(",", "")
            listaTipo.append(w)

            TemEspaco(listaTipo)
            

            listaAcessibilidade=[]
            acessibilidade= input("Digite a acessibilidade: ")
            y=acessibilidade.replace("-", "")  
            k=y.replace(".", "")
            w=k.replace(",", "")
            listaAcessibilidade.append(w)
            
            TemEspaco(listaAcessibilidade)
            
     
            arm[Sala]= [listaNome[0], capacidade, listaTipo[0], listaAcessibilidade[0]]
            print()

            print("\n ***Informações incluídas***\n")

           
                      
        else:
            print("\n A sala já está cadastrada...")
            print()
            volta()
        







        
#FUNÇÃO DE ALTERAR

def alterar(arm, Sala):
     N = arm.get(Sala)
     if N == None:
         L=[]
         CAD=input("Essa Sala não está cadastrada, deseja cadastrá-la (s/n)?").lower()
         L.append(CAD)
         if L[0]== "s" :
             incluir(arm, Sala)
         else:
             print()
             print("\n OK!")
             print()
             volta()
         
     else:
        print("\n  Essa sala já está cadastrada\n")
        print("\n  Hora de mudar os dados então...\n")
        
        listaNome=[]
        nome= input("Digite o nome: ").lower()
        y=nome.replace("-", "")  
        k=y.replace(".", "")
        w=k.replace(",", "")

        listaNome.append(w)
        TemEspaco(listaNome)
        conferindo(arm,listaNome)
        

            
        capacidade=inteiro("Digite a capacidade da sala: ")
            

        listaTipo=[]
        tipo= input("Digite o tipo de exibição: ")
        y=tipo.replace("-", "")  
        k=y.replace(".", "")
        w=k.replace(",", "")

        listaTipo.append(w)
        TemEspaco(listaTipo)
            

        listaAcessibilidade=[]
        acessibilidade= input("Digite a acessibilidade: ")
        y=acessibilidade.replace("-", "")  
        k=y.replace(".", "")
        w=k.replace(",", "")

        listaAcessibilidade.append(w)
        TemEspaco(listaAcessibilidade)
            

        
        #aqui coloca no dicionario
        arm[Sala]= [listaNome[0], capacidade, listaTipo[0], listaAcessibilidade[0]]
        

        print(" ***Informações incluídas*** \n")
        







        
#FUNÇÃO DE EXCLUIR

def excluir(arm, Sala):
    N = arm.get(Sala)
    if N == None:
         CAD=input("Essa Sala não está cadastrada, deseja cadastrá-la (s/n)?").lower()
         if CAD== "s":
             incluir(arm, Sala)
         else:
             print("\n OK! \n")
             print()
             volta()
    else:
       del arm[Sala]
       
        
       print("\n ***Informações excluídas*** \n")
        
    







    
#FUNÇÃO DE MOSTRAR UMA SALA
    
def mostrar(arm, Sala):

    vazio={}
    if arm == vazio:
        print()
        print(" ***Não há nada para visualizar*** ")
        print()
        volta()
    else:
         N = arm.get(Sala)
         if N == None:
             CAD=input("Essa Sala não está cadastrada, deseja cadastrá-la (s/n)?").lower()
             if CAD== "s":
                 incluir(arm, Sala)
             else:
                 print("\n OK! \n")
                 print()
                 volta()

         else:
            #print() é só para pular linha
            print()
            print()
         
            print("Dados da Sala: \n")

            print("Nome:", arm[Sala][0])
            print("Capacidade:", arm[Sala][1])
            print("Tipo de exibição:", arm[Sala][2])
            print("Acessibilidade:", arm[Sala][3])
            print()








#FUNÇÃO MOSTRAR TODAS AS SALAS
def mostrarSalas(arm):

    vazio={}
    if arm == vazio:
        print(" ***Não há nada para visualizar***")
        print()
        volta()
    else:
   
   

        for elements in arm:

            lista= arm[elements]
        
            print("Número da sala:",elements)
            print("Nome:", lista[0])
            print("Capacidade:", lista[1])
            print("Tipo de exibição:", lista[2])
            print("Acessibilidade:", lista[3])
            print()
            print()
        volta()


def grava_salas(arm):

    arq = open("salas.txt", "w")
    
    
    

    
            
    l=[]
    for elements in arm:
        
        num= str(elements)
                
        for i in arm[elements]:
            x= str(i)
            l.append(x)
        
        
                

        linha= num + " / " + l[0] + " / "+  str(l[1])+ " / "+  l[2] + " / " +l[3] + " "  +  "\n"
        
                
        arq.write(linha)
       
        
        l=[]
        
    arq.close()

        



#Função de recuperar os dados das salas

def recupera_salas(arm):

    
    if ( existe_arquivo("salas.txt") ):

        
        arq = open("salas.txt", "r")

        
        for linha in arq:

            
           
            linha = linha[:len(linha)-1]

            
            lista = linha.split(" / ")
            

            numero = int(lista[0])
            
            nome = lista[1]
           
            capacidade = int(lista[2])
           
            tipo = lista[3]
            
            acessibilidade =lista[4]
          

            
            arm[numero] = [nome, capacidade, tipo, acessibilidade]
            

        






        
                                                                ###### FUNÇÃO SUBMENU DE SALAS #####

def salas(dic):
    esc= 0
    while esc != 6:
        print()
        print()
        print()
        print("\n Submenu de Salas: \n")
        print("1 - Incluir sala")
        print("2 - Alterar sala")
        print("3 - Excluir sala")
        print("4 - Mostrar sala")
        print("5 - Mostrar todas as salas")
        print("6 - Sair do menu de salas")

        esc=inteiro("\nEscolha um tópico (digite o número do tópico): ")
        print()
        while esc <1 or esc >6:
            print("\n Erro! Opção inválida")
            esc=inteiro("\nEscolha um tópico (digite o número do tópico): ")
            
            
        if esc == 1:
                n1= inteiro("Digite o número da sala: ")
                incluir(dic, n1)

               
                
        if esc == 2:
            n2= inteiro("\nDigite o número da sala que você quer alterar: ")
            alterar(dic, n2)

        if esc == 3:
                n3= inteiro("\nDigite o número da sala que você quer excluir: ")
                excluir(dic, n3)

        if esc == 4:
                n4= inteiro("\nDigite o número da sala que você quer mostrar: ")
                mostrar(dic, n4)
    
        if esc == 5:
                mostrarSalas(dic)

        if esc == 6:
                grava_salas(dic)
        



###################################################################### CRUD2- FILMES ##################################################################################

def existe_arquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

def Incluir_Filme(dados):

    codigo_filme = input("Digite o código do Filme: ")
    if codigo_filme == "":
      while len(codigo_filme) == 0:
           print("Você não digitou nada!")
           codigo_filme = input("Digite o codigo do filme: ")
    if codigo_filme.isnumeric() == False:
        while codigo_filme.isnumeric() == False:
            print("Digite um número, não uma palavra! ")
            codigo_filme = input("Digite o codigo do filme: ")
            
    nome_filme = input("Digite o nome do filme: ")
    if nome_filme == "":
      while len(nome_filme) == 0:
           print("Você não digitou nada!")
           nome_filme = input("Digite o nome do filme: ")
    if nome_filme.isnumeric() == True:
        while nome_filme.isnumeric() == True:
            print("Digite uma palavra, não um número! ")
            nome_filme = input("Digite o nome do filme: ")
            
    if codigo_filme not in dados and nome_filme not in dados:
        data_lançamento = input("Digite o ano de lançamento: ")
        if data_lançamento == "":
            while len(data_lançamento) == 0:
                print()
                print("Você não digitou nada!")
                print()
                data_lançamento = input("Digite a data de lançamento: ")
        if data_lançamento.isnumeric() == False:
            while data_lançamento.isnumeric() == False:
                print("Digite um número, não uma palavra! ")
                data_lançamento = input("Digite o a data de lançamento")
        
        
        genero = input("Digite genero do filme: ")
        if genero == "":
            while len(genero) == 0:
                print()
                print("Você não digitou nada!")
                print()
                genero = input("Digite o genero: ")
        if genero.isnumeric() == True:
            while genero.isnumeric() == True:
                print("Digite uma palavra, não um número! ")
                genero = input("Digite o genero do filme: ")

        lista_atores = []

        qtd_atores = int(input("Quantos atores estão atuando: "))
        for i in range(qtd_atores):
            nome_ator = input("Digite o nome do ator(a): ")
            if nome_ator == "":
                while len(nome_ator) == 0:
                    print()
                    print("Você não digitou nada!")
                    print()
                    nome_ator = input("Digite o nome do ator(a): ")
            if nome_ator.isnumeric() == True:
                while nome_ator.isnumeric() == True:
                    print("Digite uma palavra, não um número! ")
                    nome_ator = input("Digite o nome do ator(a): ")
            lista_atores.append(nome_ator)
                        

        dados[codigo_filme]=(nome_filme, data_lançamento,genero,qtd_atores, lista_atores)
        print("Dados inseridos com sucesso!")
        enter = input("Caso queira continuar, aperte ENTER")

    else:
            print("Filme já cadastrado!")
            enter = input("Caso queira continuar, aperte ENTER")

def Gravar(dados):
    arq = open("teste.txt", "w")    
    for codigo_filme in dados:
        tupla = dados[codigo_filme]
        atores = "#".join(tupla[4])
        linha = codigo_filme + "-" + str(tupla[0]) + "-" + str(tupla[1]) + "-" + str(tupla[2]) + "-" + str(tupla[3]) + "-" + atores + "\n"
        arq.write(linha)

    arq.close()



def recupera(dados):

    if ( existe_arquivo("teste.txt") ):

        arq = open("teste.txt", "r")

        for linha in arq:
            linha = linha[:len(linha)-1]
            lista = linha.split("-")
            codigo_filme = lista[0]
            nome_filme = lista[1]
            data_lançamento = lista[2]
            genero = lista[3]
            qtd_atores = lista[4]
            tot_atores = lista[5]
            liste1 = tot_atores.split("#")
            dados[codigo_filme]=(nome_filme, data_lançamento,genero,qtd_atores, liste1)



def Listar_um_Filme(dados,codigo_filme):
    if codigo_filme in dados:
        dados = dados[codigo_filme]
        u = ['Filme','Lançamento','Gênero','N° de Atores']
        print(f"{u[0]}: {dados[0]}")
        print(f"{u[1]}: {dados[1]}")
        print(f"{u[2]}: {dados[2]}")
        print(f"{u[3]}: {dados[3]}")
        for i in dados[-1]:
            print("Ator(a): ",i)

        
    else:
        print("Filme não está cadastrado")


def Alterar_Filme(dados,chave): 
  Listar_um_Filme(dados,chave)
  confirma = input("Tem certeza que deseja alterar? (S/N): ").upper()
  
  if confirma == 'S':
                
        nome_filme = input("Digite o nome do filme: ")
        if nome_filme == "":
          while len(nome_filme) == 0:
               print("Você não digitou nada!")
               nome_filme = input("Digite o nome do filme: ")
        if nome_filme.isnumeric() == True:
            while nome_filme.isnumeric() == True:
                print("Digite uma palavra, não um número! ")
                nome_filme = input("Digite o nome do filme: ")
                
               
        data_lançamento = input("Digite o ano de lançamento: ")
        if data_lançamento == "":
            while len(data_lançamento) == 0:
                print()
                print("Você não digitou nada!")
                print()
                data_lançamento = input("Digite a data de lançamento: ")

            
            
        genero = input("Digite genero do filme: ")
        if genero == "":
            while len(genero) == 0:
                    print()
                    print("Você não digitou nada!")
                    print()
                    genero = input("Digite o genero: ")
        if genero.isnumeric() == True:
            while genero.isnumeric() == True:
                print("Digite uma palavra, não um número! ")
                genero = input("Digite o genero do filme: ")

        lista_atores = []

        qtd_atores = int(input("Quantos atores estão atuando: "))
        for i in range(qtd_atores):
            nome_ator = input("Digite o nome do ator(a): ")
            if nome_ator == "":
                while len(nome_ator) == 0:
                    print()
                    print("Você não digitou nada!")
                    print()
                    nome_ator = input("Digite o nome do ator(a): ")
            if nome_ator.isnumeric() == True:
                while nome_ator.isnumeric() == True:
                    print("Digite uma palavra, não um número! ")
                    nome_ator = input("Digite o genero do filme: ")
            lista_atores.append(nome_ator)
            dados[chave]=(nome_filme, data_lançamento,genero,qtd_atores, lista_atores)

        print("Dados alterados com sucesso!")
        enter = input("Caso queira continuar, aperte ENTER")

  else:
 
            print("Alteração cancelada!")
            enter = input("Caso queira continuar, aperte ENTER")
 
    
def Excluir_Filme(dados,chave):

        confere = dados.get(chave)
        if confere == None:
            print("Filme não cadastrado!")
            print("Essa sala não está cadastrada")
            cadastrar = input("Deseja cadastrar? ").upper()
            if cadastrar == 'S':
                  Incluir_Filme(dados)
            else:
               print("OK!")
               
        else:

            Listar_um_Filme(dados,chave)

            apagar = input("Deseja apagar os dado inseridos desse código? (S/N)").upper()

            if apagar == 'S':
                del dados[chave]
                print("Dados apagados com sucesso!")
                enter = input("Caso queira continuar, aperte ENTER")


def Listar_todos_os_Filmes(dados):

    print()
    print("Dado de cada filme cadastrado: ")
    print()
    for codigo_filme in dados:
        tupla = dados[codigo_filme]
        u = ['Filme:','Lançamento:','Gênero:','Quantidade de atores:']
        print("Código:",codigo_filme)
        print(f"{u[0]} {tupla[0]}")
        print(f"{u[1]} {tupla[1]}")
        print(f"{u[2]} {tupla[2]}")
        print(f"{u[3]} {tupla[3]}")
        z = list(dados)
        ç = len(z)//len(z)
        atores = tupla[4]
        for i in range(ç):
            for g in atores:
               print("Atores: ", g)
            print()
                
    print("")
    enter = input("Caso queira continuar, aperte ENTER")




def menu_filmes(esc_menu):

    opc = 0
    
    while ( opc != 6 ):

        print()
        print("Submenu de Filmes")
        print()        
        print("1 - Incluir Filme")
        print("2 - Alterar Filme")
        print("3 - Excluir um Filme")
        print("4 - Listar um Filme")
        print("5 - Listar todos os Filmes")
        print("6 - Sair")


        opc = int(input("Digite uma opção: "))

        if opc == 1:
            Incluir_Filme(esc_menu)

        elif opc == 2:
            codigo_filme = input("Código do filme para alterar: ")
            Alterar_Filme(esc_menu, codigo_filme)
            
        elif opc == 3:
            codigo_filme=input("Código do filme para remover: ")
            Excluir_Filme(esc_menu, codigo_filme)
            
        elif opc == 4:
            codigo_filme=input("Código do filme para consultar: ")
            Listar_um_Filme(esc_menu, codigo_filme)
            enter = input("Caso queira continuar, aperte ENTER")
            
        elif opc == 5:
            Listar_todos_os_Filmes(esc_menu)

        elif opc == 6:
            Gravar(esc_menu)







###########################################################################  CRUD3- SESSÕES ###########################################################################

#FUNÇÃO DE INCLUIR UMA SESSÃO

def incluir_sessao(dicS, dicF, dicE, numero, codigo, date, hour):
    

    if existe(dicS, numero):
        
       
        if  existe(dicF, codigo):
            chave=(numero, codigo, date, hour)
            if existe(dicE, chave):
                print()
                print()
                print(" Essa sessão já está cadastrada!\n")
                print()
                
            else:
                preco=float(input("Digite o preço do ingresso: "))
                dicE[chave]=[preco]

                print(dicE)

                print("\n ***Informações incluídas***\n")

                print()

                volta()

        else:
            print()
            print(" *** A sala ou o filme não está cadastrado*** \n")
            volta()
            

    else:
        print()
        print(" ***A sala ou o filme não está cadastrado*** \n")
        volta()
    



#FUNÇÃO DE ALTERAR UMA SESSÃO

def alterar_sessao(dicS, dicF, dicE, sala, filme, date, hour):
    chave= (sala, filme, date, hour)
    
    print(chave)
    
    if existe(dicE, chave):
        print("\n  Essa sessão já está cadastrada\n")        
        print("\n  Hora de mudar os dados então...\n")

        
        preco1=float(input("Digite o novo preço: "))
        dicE[chave]= [preco1]
        print(dicE)

        print()
        print()
        print(" ***Informações incluídas*** \n")
        
    else:
       
        print()
        print("\n ***Esta sessão não está cadastrada***\n")
        print()
        
        print(" Para cadastrar essa sessão você precisa cadastrar a sala e o filme primeiro...")
        print()
        print(" Se a sala e o filme já estiverem cadastrados, ele só vai criar a nova sessão normalmente")
        print()

        escolha= input("Deseja cadastrar a sala e o filme? (s/n)").lower()
        if escolha== "s":
            
            incluir(dicS, sala)
            grava_salas(dicS)

           

            Incluir_Filme(dicF)
            Gravar(dicF)
            
            print()
            print(" Tente cadastrar agora...\n")
            
            print()
            
            
            preco2= float(input("Digite o  preço: "))
            dicE[chave]= [preco2]
            print("do novo:", dicE)

        else:
            print()
            print(" OK!")
            
            volta()
            







#FUNÇÃO DE EXCLUIR UMA SESSÃO
def Excluir_Sessao (dicS, dicF, dicE, numero, codigo, date, hour ):
    chave=(numero, codigo, date, hour)
    N = dicE.get(chave)
    if N == None:
         CAD=input("Essa sessão não está cadastrada, deseja cadastrá-la (s/n)?").lower()
         if CAD== "s":
           
            print()
            print(" Digite os dados da sala \n") 
            incluir(dicS, numero)
            grava_salas(dicS)

           

            Incluir_Filme(dicF)
            Gravar(dicF)
            
            print()
            print(" Tente cadastrar agora...\n")
            
            print()
            
            
            preco3= float(input("Digite o  preço: "))
            dicE[chave]= [preco3]
            print("do novo:", dicE)


            print("***As informações foram inseridas***")

            

         else:
             print("\n OK! \n")
             print()
             volta()
    else:
       del dicE[chave]
       
        
       print("\n ***Informações excluídas*** \n")
        
    




    









#FUNÇÃO DE LISTAR UMA SESSÃO
def Listar_uma_Sessao(dicS, dicF, dicE, sala, filme, date, hour):
    chave=(sala, filme, date, hour)
    if existe(dicE, chave):
        
           
           print()
           print("Dados da Sessão:")
           mostrar(dicS, sala)
           print("Dados do Filme: \n")
           Listar_um_Filme(dicF, filme)

           print()

           print("Preço do ingresso: R$",dicE[chave][0])

           print()

           print("Data da sessão: ", date)
           print()
           print("Horário da sessão: ", hour)

           print()
           print()
           
           print()

    else:
           print()
           print("\n ***Esta sessão não está cadastrada***\n")
           print()
        
           print(" Para cadastrar essa sessão você precisa cadastrar a sala e o filme primeiro...")
           print()
           print(" Se a sala e o filme já estiverem cadastrados, ele só vai criar a nova sessão normalmente")
           print()

           escolha= input("Deseja cadastrar a sala e o filme? (s/n)").lower()
           if escolha== "s":
            
                incluir(dicS, sala)
                grava_salas(dicS)

           

                Incluir_Filme(dicF)
                Gravar(dicF)
            
                print()
                print(" Tente cadastrar agora...\n")
            
                print()
            
            
                preco2= float(input("Digite o novo preço: "))
                dicE[chave]= [preco2]
                print("do novo:", dicE)

           else:
                print()
                print(" OK!")
            
                volta()

            



#FUNÇÃO DE MOSTRAR TODOS

def Listar_todas_as_Sessoes(dicS, dicF, dicE):
    
    
    vazio={}
    if dicE== vazio:

        print()
        print(" Não há nada para visualizar ")
        print()
    else:
      
        for i in dicE:
                   
            sala1 = i[0]
            filme1 = i[1]
            date1= i[2]
            hour1= i[3]

            
            Listar_uma_Sessao(dicS, dicF, dicE, sala1, filme1, date1, hour1)

            print()
            print()

    




#FUNÇÃO DE GARAVAR OS DADOS DA LISTA SESSÕES

def grava_sessoes(dicE):

    arq = open("sessoes.txt", "w")
    
            
    l=[]
    for elements in dicE:
        
        num = str(elements[0])
        codigo = str(elements[1])
        date= str(elements[2])
        hour= str(elements[3])
        

                
        for i in dicE[elements]:
            x= str(i)
            l.append(x)
        
        
                

        linha= num + " / " + codigo + " / " + date + " / " + hour + " / "  +l[0]  +  "\n"
        
                
        arq.write(linha)
       
        
        l=[]
        
    arq.close()

        


#FUNÇÃO DE RECUPERAR OS DADOS DAS SESSÕES
    
def recupera_sessoes(dicE):
    
    
    if ( existe_arquivo("sessoes.txt") ):

        
        arq = open("sessoes.txt", "r")

        
        for linha in arq:

            
           
            linha = linha[:len(linha)-1]

            
            lista = linha.split(" / ")
            

            numero = int(lista[0])
            
            codigo = lista[1]
           
            data = (lista[2])
           
            hora = lista[3]
            
            preco =float(lista[4])

            chave=(numero, codigo, data, hora)
          

            
            dicE[chave]= [preco]

            
       

       
   





                                    #### Função de Menu Sessões ###

        

def sessoes(dicSala, dicFilmes,dicSessoes):
    esc= 0
    while esc != 6:
        print()
        print()
        print()
        print("\n Submenu de Sessões: \n")
        print("1 - Incluir sessão")
        print("2 - Alterar sessão")
        print("3 - Excluir sessão")
        print("4 - Mostrar sessão")
        print("5 - Mostrar todas as sessões")
        print("6 - Sair do menu de sessões")

        esc=inteiro("\nEscolha um tópico (digite o número do tópico): ")
        print()
        while esc <1 or esc >6:
            print("\n Erro! Opção inválida")
            esc=inteiro("\nEscolha um tópico (digite o número do tópico): ")
            
            
        if esc == 1:
                n1=inteiro("Digite o número da sala: ")
                n2=input("Digite o código do filme: ")
                
                #código do lucas para verificar
                if n2 == "":
                    while len(n2) == 0:
                       print()
                       print(" ERRO! você digitou vazio\n")
                       n2 = input("Digite o codigo do filme: ")
                if n2.isnumeric() == False:
                    while n2.isnumeric() == False:
                        print()
                        print(" ERRO! Digite um número inteiro\n ")
                        
                        n2 = input("Digite o código do filme: ")
            

            
                dia = int(input("Digite o dia: "))
                dia1 = list(str(dia))
                if len(dia1) > 2 or dia > 31:
                   while len(dia1) > 2 or dia > 31:
                      print("Digitação inválida!")
                      dia = int(input("Digite o dia: "))
                      dia1 = list(str(dia))


                mes = int(input("Digite o mês: "))
                mes1 = list(str(mes))
                if len(mes1) > 2 or mes > 12:
                   while len(mes1) > 2 or mes > 12:
                     print("Digitação inválida!")
                     mes = int(input("Digite o mês: "))
                     mes1 = list(str(mes))


                ano = int(input("Digite o ano: "))
                ano1 = list(str(ano))
                if len(ano1) > 4 or ano > 9999:
                   while len(ano1) > 4 or ano > 100000:
                      print("Digitação inválida!")
                      ano = int(input("Digite o ano: "))
                      ano1 = list(str(ano))


                data1 = str(dia) + '/' + str(mes) + '/' + str(ano)
                
                hora= input("Digite a hora: ")
               
                incluir_sessao(dicSala, dicFilmes, dicSessoes, n1, n2, data1, hora)

               
                
        if esc == 2:
            n3=inteiro("Digite o número da sala: ")
            n4=input("Digite o código do filme: ")
            if n4 == "":
                while len(n4) == 0:
                    print()
                    print(" ERRO! você digitou vazio\n")
                    n4 = input("Digite o codigo do filme: ")
            if n4.isnumeric() == False:
                    while n4.isnumeric() == False:
                        print()
                        print(" ERRO! Digite um número inteiro\n ")
                        
                        n4= input("Digite o código do filme: ")
            
            dia = int(input("Digite o dia: "))
            dia1 = list(str(dia))
            if len(dia1) > 2 or dia > 31:
                while len(dia1) > 2 or dia > 31:
                    print("Digitação inválida!")
                    dia = int(input("Digite o dia: "))
                    dia1 = list(str(dia))


            mes = int(input("Digite o mês: "))
            mes1 = list(str(mes))
            if len(mes1) > 2 or mes > 12:
                while len(mes1) > 2 or mes > 12:
                    print("Digitação inválida!")
                    mes = int(input("Digite o mês: "))
                    mes1 = list(str(mes))


            ano = int(input("Digite o ano: "))
            ano1 = list(str(ano))
            if len(ano1) > 4 or ano > 9999:
                while len(ano1) > 4 or ano > 100000:
                    print("Digitação inválida!")
                    ano = int(input("Digite o ano: "))
                    ano1 = list(str(ano))


            data2 = str(dia) + '/' + str(mes) + '/' + str(ano)
               
            hora= input("Digite a hora: ")
               

            alterar_sessao(dicSala, dicFilmes, dicSessoes, n3, n4, data2, hora)

            

        
        if esc == 3:
                n5=inteiro("Digite o número da sala: ")
                n6=input("Digite o código do filme: ")
                if n6 == "":
                    while len(n6) == 0:
                       print()
                       print(" ERRO! você digitou vazio\n")
                       n6 = input("Digite o codigo do filme: ")
                if n6.isnumeric() == False:
                    while n6.isnumeric() == False:
                        print()
                        print(" ERRO! Digite um número inteiro\n ")
                        
                        n6 = input("Digite o código do filme: ")
            

                
                dia = int(input("Digite o dia: "))
                dia1 = list(str(dia))
                if len(dia1) > 2 or dia > 31:
                   while len(dia1) > 2 or dia > 31:
                      print("Digitação inválida!")
                      dia = int(input("Digite o dia: "))
                      dia1 = list(str(dia))


                mes = int(input("Digite o mês: "))
                mes1 = list(str(mes))
                if len(mes1) > 2 or mes > 12:
                   while len(mes1) > 2 or mes > 12:
                     print("Digitação inválida!")
                     mes = int(input("Digite o mês: "))
                     mes1 = list(str(mes))


                ano = int(input("Digite o ano: "))
                ano1 = list(str(ano))
                if len(ano1) > 4 or ano > 9999:
                   while len(ano1) > 4 or ano > 100000:
                      print("Digitação inválida!")
                      ano = int(input("Digite o ano: "))
                      ano1 = list(str(ano))


                data3 = str(dia) + '/' + str(mes) + '/' + str(ano)
                
                hora= input("Digite a hora: ")
               

                Excluir_Sessao(dicSala, dicFilmes, dicSessoes, n5, n6, data3, hora)

                
        
        if esc == 4:
                n7=inteiro("Digite o número da sala: ")
                n8=input("Digite o código do filme: ")
                if n8 == "":
                    while len(n8) == 0:
                       print()
                       print(" ERRO! você digitou vazio\n")
                       n8 = input("Digite o codigo do filme: ")
                if n8.isnumeric() == False:
                    while n8.isnumeric() == False:
                        print()
                        print(" ERRO! Digite um número inteiro\n ")
                        
                        n8 = input("Digite o código do filme: ")
            

                
                dia = int(input("Digite o dia: "))
                dia1 = list(str(dia))
                if len(dia1) > 2 or dia > 31:
                   while len(dia1) > 2 or dia > 31:
                      print("Digitação inválida!")
                      dia = int(input("Digite o dia: "))
                      dia1 = list(str(dia))


                mes = int(input("Digite o mês: "))
                mes1 = list(str(mes))
                if len(mes1) > 2 or mes > 12 or mes:
                   while len(mes1) > 2 or mes > 12:
                     print("Digitação inválida!")
                     mes = int(input("Digite o mês: "))
                     mes1 = list(str(mes))


                ano = int(input("Digite o ano: "))
                ano1 = list(str(ano))
                if len(ano1) > 4 or ano > 9999:
                   while len(ano1) > 4 or ano > 100000:
                      print("Digitação inválida!")
                      ano = int(input("Digite o ano: "))
                      ano1 = list(str(ano))


                data4 = str(dia) + '/' + str(mes) + '/' + str(ano)
                
                hora= input("Digite a hora: ")
               

                
                Listar_uma_Sessao(dicSala, dicFilmes, dicSessoes, n7, n8, data4, hora)


        
        if esc == 5:

            
                Listar_todas_as_Sessoes(dicSala, dicFilmes, dicSessoes)
       
        if esc == 6:
                grava_sessoes(dicSessoes)
        

###################################################################### RELATÓRIO ######################################################################################


                
def relatorio(dicS, dicF, dicE, a1, a2):
    
    print("Relatório: Sessões entre os anos de", a1, " até ", a2,":")
    print("---------------------------------------------\n")
    
    for chave in dicE.keys():
        valor = chave[2]
        data = valor
        data1 = data.split("/")
        a = int(data1[-1])
        if ( a >= a1 and a <= a2 ):
            sala = chave[0]
            filme = chave[1]
            date = chave[2]
            hour = chave[3]
            Listar_uma_Sessao(dicS, dicF, dicE, sala, filme, date, hour)
            print("----------------------------\n")
    print("")









                                                     ###################### PROGRAMA PRINCIPAL #####################


# FUNÇÃO DO MENU PRINCIPAL

def menu():
    print("\n Menu de Opções: \n ")
    print("1 - Submenu de Salas")
    print("2 - Submenu de Filmes")
    print("3 - Submenu de Sessões")
    print("4 - Relatório")
    print("5 - Sair")



 

dic_salas={}

Dic_Filmes= {}

dic_sessoes={}

recupera_salas(dic_salas)

recupera(Dic_Filmes)

recupera_sessoes(dic_sessoes)
apertou= 0
while apertou != 5:

    # mostra o menu :
    menu()
   
    apertou=inteiro("\nEscolha uma opção (digite o número da opção): ")

    while apertou < 1 or apertou > 5 :
        
        print("\n Erro! Opção inválida")
        apertou=inteiro("\nEscolha uma opção (digite o número da opção): ")

   
    if apertou == 1:
        salas(dic_salas)


  
    if apertou == 2:
        menu_filmes(Dic_Filmes)

        
    
    if apertou == 3:
           
        sessoes(dic_salas, Dic_Filmes, dic_sessoes)

    
    if apertou == 4:
        a1 = int(input("Digite o ano inicial:"))
        
        a2 = int(input("Digite o ano final:"))
        relatorio(dic_salas, Dic_Filmes, dic_sessoes, a1, a2)

    
print()
print(" Saindo... até mais! ")

