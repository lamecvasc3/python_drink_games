from random import randint


def add_men_players_in_truth_or_dare(num_men_players):

    men_players = []
    while(num_men_players != 0):
        men_players.append(input("Digite o nome de um jogador homem:"))
        num_men_players -= 1
    return men_players


def add_women_players_in_truth_or_dare(num_women_players):

    women_players = []
    while (num_women_players != 0):
        women_players.append(input("Digite o nome de uma jogadora mulher:"))
        num_women_players -= 1
    return women_players


def init_truth_or_dare():

    num_men_players = int(input("Quantos jogadores homens? "))
    num_women_players = int(input("Quantas jogadoras mulheres? "))

    men_players = add_men_players_in_truth_or_dare(num_men_players)
    women_players = add_women_players_in_truth_or_dare(num_women_players)

    select_player_in_truth_or_dare(men_players, women_players)


def truth_organizer():
    truths = ['Verdade 1',
              'Verdade 2',
              'Verdade 3',
              'Verdade 4',
              'Verdade 5',
              'Verdade 6',
              'Verdade 7']
    select_truth = randint(0,(len(truths)-1))
    return truths[select_truth]


def selected_truth(selected_player):
    truth = truth_organizer()
    print(selected_player,'é verdade que',truth)


def dare_organizer(other_players):
    other_player = randint(0, len(other_players)-1)
    dares = ['Desafio você a beijar o(a) jogador(a) '+other_players[other_player],
             'Desafio 2',
             'Desafio 3',
             'Desafio 4',
             'Desafio 5',
             'Desafio 6',
             'Desafio 7']
    dare = randint(0, len(dares)-1)
    return dares[dare]


def selected_dare(selected_player, other_players):
    dare = dare_organizer(other_players)
    print("Jogador",selected_player,"esse é seu desafio: ")
    print(dare)


def men_selected (men_players, women_players):
    select_man = randint(0,len(men_players)-1)
    print("\nJogador",men_players[select_man],"selecionado.")
    chosen_option = int(input("Verdade ou desafio?\n"
                           "Digite 0 para Verdade.\n"
                           "Digite 1 para Desafio.\n"
                           "Opção: "))
    if(chosen_option == 0):
        selected_truth(men_players[select_man])
    elif(chosen_option == 1):
        selected_dare(men_players[select_man], women_players)
    else:
        print("Opção não selecionada!")


def women_selected(women_players, men_players):
    select_woman = randint(0, len(women_players) - 1)
    print("\nJogadora", women_players[select_woman], "selecionada.")
    chosen_option = int(input("Verdade ou desafio?\n"
                              "Digite 0 para Verdade.\n"
                              "Digite 1 para Desafio.\n"
                              "Opção: "))
    if (chosen_option == 0):
        selected_truth(women_players[select_woman])
    elif (chosen_option == 1):
        selected_dare(women_players[select_woman], men_players)
    else:
        print("Opção não selecionada!")


def select_player_in_truth_or_dare(men_players, women_players):

    next = 0
    while(next != 1):
        option = randint(1,2)

        if(option == 1):
            men_selected(men_players,women_players)
        elif(option == 2):
            women_selected(women_players,men_players)

        next = int(input("\nDeseja continuar nesse jogo ou encerrar? \n"
                     "Digite 0 para continuar.\n"
                     "Digite 1 para parar esse jogo\n"))


def add_players_in_i_never(number_players):
    players = number_players
    players_names = []

    while(players != 0):
        players_names.append(input("Digite o seu nome jogador: "))
        players -= 1

    print("Jogadores cadastrados 'smile face'!")
    return players_names


def i_never_questions():
    questions = ['Eu nunca 1',
                 'Eu nunca 2',
                 'Eu nunca 3',
                 'Eu nunca 4',
                 'Eu nunca 5',
                 'Eu nunca 6']
    question_id = randint(0, len(questions)-1)
    return questions[question_id]


def i_never_organizer(players):
    next = 0
    while (next == 0):
        player_id = randint(0, len(players) - 1)
        next = int(input("\nDeseja continuar nesse jogo ou encerrar? \n"
                         "Digite 0 para continuar.\n"
                         "Digite 1 para parar esse jogo\n"))
        question = i_never_questions()
        print('Jogador(a) selecionado:',players[player_id])
        print(question)
    

def init_i_never():
    number_players = int(input('Quantos jogadores irão participar? '))
    players = add_players_in_i_never(number_players)
    i_never_organizer(players)


def add_men_player_in_bottle_game(num_men_players):
    men_players = []
    while (num_men_players != 0):
        men_players.append(input("Digite o nome de um jogador homem:"))
        num_men_players -= 1
    return men_players


def add_women_player_in_bottle_game(num_women_players):
    women_players = []
    while (num_women_players != 0):
        women_players.append(input("Digite o nome de uma jogadora mulher:"))
        num_women_players -= 1
    return women_players


def bottle_game_organizer(men_players,women_players):
    next = 0
    while(next == 0):
        man_id = randint(0, len(men_players)-1)
        woman_id = randint(0, len(women_players)-1)
        print("Jogodor 1:", men_players[man_id])
        print("Jogodor 2:", women_players[woman_id])
        next = int(input("\nDeseja continuar nesse jogo ou encerrar? \n"
                         "Digite 0 para continuar.\n"
                         "Digite 1 para parar esse jogo\n"))


def init_bottle_game():
    num_men_players = int(input("Quantos jogadores homens? "))
    num_women_players = int(input("Quantas jogadoras mulheres? "))

    men_players = add_men_player_in_bottle_game(num_men_players)
    women_players = add_women_player_in_bottle_game(num_women_players)

    bottle_game_organizer(men_players,women_players)


def add_players_in_who_drinks(number_players):
    players = number_players
    players_names = []

    while (players != 0):
        players_names.append(input("Digite o seu nome jogador: "))
        players -= 1

    print("Jogadores cadastrados 'smile face'!")
    return players_names


def who_drinks_organizer(players):
    next = 0

    while(next == 0):
        player_id = randint(0, len(players)-1)
        print("Jogador selecionado:",players[player_id])
        next = int(input("\nDeseja continuar nesse jogo ou encerrar? \n"
                         "Digite 0 para continuar.\n"
                         "Digite 1 para parar esse jogo\n"))


def init_who_drinks():
    number_players = int(input('Quantos jogadores irão participar? '))
    players = add_players_in_who_drinks(number_players)

    who_drinks_organizer(players)


def main():

    print('        ░░░▓███████▓░')
    print(' ░░░░░░░░▓██▓▓▒▒▒▒▒▓▓█▓░ ')
    print('░░░░░▒██▓▒░░░░░░░░░░░▒▓█▒░░░░')
    print('░░░░██▒░░░░░░░░░░░░░░░░░▓█░░░ ')
    print('░░░██▒▒▒▒░░░░░░░░░▓▓▓▒░░░░██░░ ')
    print('░░█▓▓▓░▓██▒░░░░░▒█▓▒▒██▓░░░██░ ')
    print('░██▓▓░░▓███░░░░▒█░░░░███▓░░░█▓ ')
    print('▒█░█░░░░░░█▓░░░▓▓░░░░░░░█░░░▒█ ')
    print('██░▓█▓▓▓▓▓█▒░░░▒█▓▓▓▓▓▓▓▓░░░░█ ')
    print('██░░░░░░░░░░░░░░░░░░░░░░░░░░░█ ')
    print('██░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░█ ')
    print('░█▒░░███████████████████▓░░░▒█ ')
    print('░▓█░░▒█▓▓▓▓▓▓▓▓█████▓▓▓█▓░░░█▓ ')
    print('░░██░░▓█▓▓▓▓▓██▓▓▓▓██▓██░░░██░ ')
    print('░░░██░░▓██▓▓█▓░░░░░░▒██▒░░██░░ ')
    print('░░░░██▓░░▓██▓░░░░░▒▓▓▓░░▓██       ')
    print("Olá, simbora pra esse jogo!!\n\n")
    print("Selecione no menu qual será  o jogo: ")

    selected_game = int(input('Digite 1 para jogar "Eu nunca"\n'
                          'Digite 2 para jogar "Verdade ou desafio?"\n'
                          'Digite 3 para jogar "Jogo da garrafa"\n'
                          'Digite 4 para jogar "Quem bebe?"\n\n'
                          'Opção selecionada: '))

    if(selected_game == 1):
        print('Você selecionou "Eu nunca"! (Não vale mentir em (T^T))\n')
        init_i_never()
        pass
    elif(selected_game == 2):
        print('Você selecionou "verdade ou desafio!" (Eu só escolho desafios bons viu (#^.^#))\n')
        init_truth_or_dare()
    elif(selected_game == 3):
        print('Você selecionou "Jogo da garrafa"! (Não tenho garrafa aqui, mas não se preocupem, ainda vai rolar beijos)\n')
        init_bottle_game()
    elif(selected_game == 4):
        print('Você selecionou "Quem bebe?"! (Esse é muito bom para esquentar)\n')
        init_who_drinks()
    else:
        print("Opção não selecionada!")


main()