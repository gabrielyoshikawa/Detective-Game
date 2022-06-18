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
            "Ao abrir a caixa, encontra seis cartas que continham informações privilegiadas sobre os principais suspeitos de assassinato, que ainda não tinham sido revelados ao público. \n"
            "-----------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Nelas estavam escritos seis nomes: \n-----------------------------------------------------------------------------------------------------------------------------------------------\nNaomi Qian - Atual esposa do prefeito \n"
            
            "John Smith - Renomado chef da cidade \nSheldon Wallace - Gastrônomo \nAlex White - Faxineiro do restaurante \n"
            
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
            "Ao explorar o buraco, encontra um caderno com dicas de quem foi o assassino, porém está codificado. Será que você consegue ajudar o detetive?"
            "\n-----------------------------------------------------------------------------------------------------------------------------------------------")

        c = 0
        while c < 11:
            user_action1 = int(input("Digite um número de 1 a 11 para escolher uma dica, ou 0 quando quiser acusar o assassino: "))
            c += 1
            if user_action1 == 1:
                print("Se Louis Jordan matou o prefeito, então Alex White não enviou as dicas")
            elif user_action1 == 2:
                print("Se Alex White não enviou as dicas então Naomi é cúmplice do assassinato")
            elif user_action1 == 3:
                print("Se Naomi foi cúmplice do assassinato então John Smith matou o prefeito")
            elif user_action1 == 4:
                print("John Smith não matou o prefeito")
            elif user_action1 == 5:
                print("Loius Jordan estava no restaurante quando o prefeito morreu ou Oswald matou o prefeito")
            elif user_action1 == 6:
                print("Se Loius Jordan estava no restaurante quando o prefeito morreu, então Naomi é cúmplice do assassinato")
            elif user_action1 == 7:
                print("Naomi não é cúmplice do assassinato")
            elif user_action1 == 8:
                print("Alex White enviou as dicas")
            elif user_action1 == 9:
                print("Louis Jordan não matou o prefeito")
            elif user_action1 == 10:
                print("Loius Jordan estava no restaurante quando o prefeito morreu ou Sheldon Wallace estava no restaurante quando o prefeito morreu")
            elif user_action1 == 11:
                print("Sheldon Wallace estava no restaurante quando o prefeito morreu")
            elif user_action1 == 0:
                c = 11

        user_guess = int(input("Digite o nome do assassino: Loius Jordan(1), Oswald Jobs(2), Alex White(3), John Smith(4), Naomi Qian(5), Sheldon Wallace(6): "))
        if user_guess == 1:
            print("Loius Jordan, era um nômade, que estava apenas de passagem pelo distrito de Adelaide, quando foi julgado como culpado pelo assassinato do prefeito Renato Flaviano Oswin. Jordan nunca saiu da prisão.")
        elif user_guess == 2:
            print("Oswald Jobs, escritor de contos policiais, atolado em dívidas e sem inspirações para seus livros, decide assassasinar o prefeito de Adelaide para sentir na pele um real conto policial.")
        elif user_guess == 3:
            print("Alex White, faxineiro do restaurante no qual ocorreu o crime, foi condenado à 30 anos de cadeia por envenenamento do prefeito Renato Flaviano Oswin. Anos depois, foi descoberto que Alex White era inocente e foi o responsável pelas dicas.")
        elif user_guess == 4:
            print("Nessa sexta-feira ocorreu o julgamento de John Smith, dono do restaurante no qual ocorreu o assassinato do prefeito Renato Flaviano Oswin. Somente após 30 anos foi descoberto que Smith não era o assassino.")
        elif user_guess == 5:
            print("Naomi Qian, esposa do prefeito Renato Flaviano Oswin, nessa sexta-feira foi condenada à 30 anos de cadeia por envenenamento. Anos depois, foi descoberto que Naomi Qian era inocente.")
        elif user_guess == 6:
            print("O gastronômo Sheldon Wallace, nessa sexta-feira é acusado de assassinar o prefeito Renato Flaviano Oswin. Após 30 anos foi descoberto que foi acusado de maneira errônea")
        else:
            print("Erro")

        play_again = int(input("Deseja jogar novamente? Sim(1) Não(2): "))
        if play_again == 2:
            verificacao = False

else:
    print("Detetive TDE não iniciado")

'''
p == Loius Jordan estava no restaurante quando o prefeito morreu
q == Alex White não enviou as dicas
r == Naomi é cúmplice do assassinato
s == John Smith matou o prefeito
t == Oswald matou o prefeito
u == Sheldon Wallace estava no restaurante quando o prefeito morreu


1 == p -> q     Se Loius Jordan estava no restaurante quando o prefeito morreu então Alex White não enviou as dicas
2 == q -> r     Se Alex White não enviou as dicas então Naomi é cúmplice do assassinato
3 == r -> s     Se Naomi é cúmplice dos assassinatos então John Smith matou o prefeito
4 == ~s         John Smith não matou o prefeito
5 == p v t      Loius Jordan estava no restaurante quando o prefeito morreu ou Oswald matou o prefeito
6 == p -> r     Se estava no restaurante quando o prefeito morreu então Naomi é cúmplice do assassinato
7 == ~r         Naomi não é cúmplice do assassinato
8 == ~q         Alex white enviou as dicas
9 == ~p         Loius Jordan não estava no restaurante quando o prefeito morreu
10 == p v u     Loius Jordan estava no restaurante quando o prefeito morreu ou Sheldon Wallace estava no restaurante quando o prefeito morreu 
11 == u         Sheldon Wallace estava no restaurante quando o prefeito morreu 
#Conclusão
12 == t         Oswald matou o prefeito  
'''