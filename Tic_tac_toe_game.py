import itertools

def win(current_game):
    
    # check if a list has same number
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
        
    # horizontal
    for row in game:
        if all_same(row):
            print("Player {} is the winner horizontally!".format(row[0]))
            return True
    
    # vertical
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print("Player {} is the winner vertically!".format(check[0]))
            return True
    
    # \ diagonal
    diags = []
    for idx in range(len(game)):
        diags.append(game[idx][idx])
    if all_same(diags):
        print("Player {} is the winner diagonally! (\)".format(diags = []))
        return True
        
    # / diagonal 0,2 1,1 2,0
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])
    if all_same(diags):
        print("Player {} is the winner diagonally! (/)".format(diags = []))
        return True
        
    return False

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This space is occupied, try another!")
            return False
        
        # print column numbers
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError:
        print("Did you attempt to play a row or column outside the range of 0,1 or 2? (IndexError)")
        return False
    except Exception as e:
        print(str(e))
        return 0

play = True
players = [1,2]
while play:

    # Loop Board Setup
    game_size = int(input("What size game TicTacToe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    
    game_won = False
    player_cycle = itertools.cycle([1, 2])
    game_board(game, just_display=True)
    while not game_won:
        current_player = next(player_cycle)
        played = False
        while not played:
            print("Player: {}".format(current_player))
            column_choice = int(input("Which column? "))
            row_choice = int(input("Which row? "))
            played = game_board(game, player=current_player, row=row_choice, column=column_choice)
    
        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n)")
            if again.lower() == "y":
                print("Restarting!")
            elif again.lower() == "n":
                print("Bye-bye!!")
                play = False
            else:
                print("Not a valid answer, well... thanks for playing!")
                play = False
