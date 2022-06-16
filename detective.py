start = int(input("Deseja iniciar Detetive TDE? Sim(1) Não(2): "))
if start == 1:
    verificacao = True
    while verificacao:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Australia - 2008 - Em uma segunda-feira chuvosa a polícia australiana do distrito de Adelaide recebe uma ligação anônima referente a um crime. \n"
            "---------------------------------------------------------------------------------------------------------------------------------------------- \n"
            "Durante essa ligação, é revelado que ocorreu um assassinato, por envenenamento no restaurante mais luxuoso da cidade. \n"
            "-----------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Na mesma semana que se inicia a investigação, o detetive encarregado pelo caso, Oliver Williams Murray recebe em sua casa uma caixa misteriosa.\n"
            "-----------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Murray era um homem calvo de 45 anos, viúvo, de altura mediana, que era conhecido por todo distrito pelo seu temperamento explosivo. \n"
            "-----------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Ao se deparar com uma caixa desconhecida em cima de seu sofá, vários questionamentos passaram pela sua mente, de onde veio essa caixa?, o que tem dentro?\nOliver sabia que só tinha apenas um jeito de descobrir, abrindo-a.\n"
            "-----------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Enquanto se aproxima, percebe que ao lado da caixa tinha uma foto com uma coordenada e uma data. \n"
            "-----------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Ao abrir a caixa, encontra cinco cartas que continham inforamações privilegiadas sobre os principais suspeitos de assassinato, que ainda não tinham sido revelados ao público. \n"
            "-----------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Nelas estavam escritos cinco nomes: \n-----------------------------------------------------------------------------------------------------------------------------------------------\nNaomi Qian - Atual esposa do prefeito \n"
            
            "John Smith - Renomado chef da cidade \nAlex White - Faxineiro do restaurante \n"
            
            "Oswald Jobs - Escritor de romances policiais \nLoius Jordan - Nome que Oliver nunca tinha ouvido antes \n"
            "-----------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Murray após longa analise, julga melhor entregar a caixa para a polícia pela manhã. \n"
            "-----------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Contudo, Murray nesta noite, não consiguiu dormir. Intrigado, às três da manhã, Oliver vai para o endereço e cada vez que se aproxima mais do local, \npercebe que é um parque abandonado afastado de Adelaide.\n"
            "-----------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Ao descer do carro se depara com um sujeito misterioso com uma pá. Ao se aproximar, o individuo, que utilizava uma máscara, corre e se camufla nas sombras. \n"
            "-----------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Após uma longa perseguição, Oliver desiste e decide voltar para onde encontrou o sujeito misterioso. Ao olhar para todos os lados, o detetive se depara com um buraco recém cavado. \n"
            "-----------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Ao explorar o buraco, encontra um caderno com dicas de quem foi o assassino, porém está codificado. Será que você consegue ajudar o detetive?")
        c = 0
        while c < 9:
            user_action1 = int(input("Digite um número de 1 a 9 para escolher uma dica, ou 0 quando quiser acusar o assassino: "))
            c += 1
            if user_action1 == 1:
                print("Se Louis Jordan matou o prefeito, então Alex White não enviou as dicas")
            elif user_action1 == 2:
                print("Se Alex White não enviou as dicas então Naomi é cúmplice do assassinato")
            elif user_action1 == 3:
                print("Se Naomi foi cúmplice do assassinato então John Smith é culpado")
            elif user_action1 == 4:
                print("John Smith não é culpado")
            elif user_action1 == 5:
                print("Loius Jordan matou o prefeito ou Oswald matou o prefeito")
            elif user_action1 == 6:
                print("Se Loius Jordan matou o prefeito, então Naomi é cúmplice do assassinato")
            elif user_action1 == 7:
                print("Naomi não é cúmplice do assassinato")
            elif user_action1 == 8:
                print("Alex White enviou as dicas")
            elif user_action1 == 9:
                print("Louis Jordan não matou o prefeito")
            elif user_action1 == 0:
                c = 9

        escolha = int(input("Digite o nome do assassino: (1)Loius Jordan, (2)Oswald Jobs, (3)Alex White, (4)John Smith, (5)Naomi Qian:"))
        if escolha == 2:
            print("Oswald Jobs, escritor de contos policiais, atolado em dívidas e sem inspirações para seus livros, decide assassasinar o prefeito de Adelaide para sentir na pele um real conto policial.")
        else:
            print("Infelizmente você errou")

        pergunta = int(input("(1)Jogar novamente (2)Parar"))
        if pergunta == 2:
            verificacao = False

else:
    print("Detetive TDE não iniciado")