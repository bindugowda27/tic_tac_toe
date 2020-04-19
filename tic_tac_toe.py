import random
from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('-----------')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('-----------')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
    
def player_input():
    marker = ' '
    
    while not (marker == 'x' or marker == 'o'):
        marker = input("enter a marker x/o for player 1 : ").lower()
           
    if marker == 'x':
        return ('x','o')
    else:
        return ('o','x')   
    
def place_marker(board,marker,position):
    board[position]=marker
    
def win_check(board,marker):
    if(     (board[7]==marker and board[8]==marker and board[9]==marker) or
            (board[4]==marker and board[5]==marker and board[6]==marker) or
            (board[1]==marker and board[2]==marker and board[3]==marker) or
            (board[7]==marker and board[4]==marker and board[1]==marker) or
            (board[8]==marker and board[5]==marker and board[2]==marker) or
            (board[9]==marker and board[6]==marker and board[3]==marker) or
            (board[7]==marker and board[5]==marker and board[3]==marker) or
            (board[9]==marker and board[5]==marker and board[1]==marker)  ):
            return True
    else:
            return False
            

 
def choose_first():
        num = random.randint(0,1)
        
        if num == 1:
            return 'player 1'
        else:
            return 'player 2'
        
def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    isFull = True
    for i in board:
        if i == ' ':
            isFull = False
    return isFull

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def players_choice(board):
    position = 0
     
    while not position in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("enter your next position : "))
        
    return position
        
def replay():
    return input("Do you want to play again (y/n) : ").lower().startswith('y')

while True:
    
    board = [ ' ' ]* 10           #  implies 10 empty spaces in board
    
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    
    print(turn + "will play first")
    
    play_game = input("are you ready to play the game y/n ").lower().startswith('y')
    
    if play_game:
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if turn == 'player 1' :
            # game logic starts here for player 1
            
            display_board(board)
            position = players_choice(board)
            place_marker(board,player1_marker,position)
            
            if win_check(board,player1_marker):
                display_board(board)
                print("player 1 won the game !!! congrates")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is Draw, Better luck next time")
                    break
                else:
                    turn = "player 2"
                    
                    
        else:
            # player 2 logic
            
            display_board(board)
            position = players_choice(board)
            place_marker(board,player2_marker,position)
            
            if win_check(board,player2_marker):
                display_board(board)
                print("player 2 won the game !!! congrates")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is Draw, Better luck next time")
                    break
                else:
                    turn = "player 1"
                    
    if not replay():
            break
            