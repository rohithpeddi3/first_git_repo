#Numbers on the column element 2,8,14
#Dictionary is made mapping all the numbers in respective columns to initial input

board = []

def form_initial_board():
    for x in range(5):
        if x%2==0:
            board.append([" "," "," "," "," ","|"," "," "," "," "," ","|"," "," "," "," "," "])
        else :
            board.append(["-----------------"])
        print "".join(board[x])

def print_board():
    for x in range(5):
        print "".join(board[x])

form_initial_board()

#dictionary of all mappings to actual user input and display output
row_places={'1':'0','2':'2','3':'4'}
col_places={'1':'2','2':'8','3':'14'}

#returns the winning value if present else returns False
def is_winning_state():
    if board[0][2] == board[0][8] and board[0][8]==board[0][14] and board[0][2] !=" ":
        return board[0][2]
    elif board[0][2] == board[2][2] and board[2][2]==board[4][2] and board[0][2] !=" ":
        return board[0][2]
    elif board[0][2] == board[2][8] and board[2][8]==board[4][14] and board[0][2] !=" ":
        return board[0][2]
    elif board[2][2] == board[2][8] and board[2][8]==board[2][14] and board[2][2] !=" ":
        return board[2][2]
    elif board[4][2] == board[4][8] and board[2][8]==board[4][14] and board[4][2] !=" ":
        return board[4][2]
    elif board[0][14] == board[2][8] and board[2][8]==board[4][2] and board[4][2] !=" ":
        return board[0][14]
    elif board[0][6] == board[2][8] and board[2][8]==board[4][14] and board[0][6] !=" ":
        return board[0][8]
    elif board[0][14] == board[2][14] and board[2][14] == board[4][14] and board[2][14] !=" ":
        return board[0][8]
    else:
        return False

# Based on the return value of winning state it decides who wins
# if it is not winning state returns -1 and game can continue
# else it returns 0 and game stops

def who_wins():
    result = is_winning_state()
    print "----->", result
    if result=="O":
        print "First Player has won!"
        return True
    elif result=="X":
        print "Second Player has won"
        return True
    else:
        return False

def place_mark(row,col,turn):
    ac_row = int(row_places[row])
    ac_col = int(col_places[col])

    #print ac_row," ",ac_col

    if board[ac_row][ac_col]=="X" or board[ac_row][ac_col]=="O":
        print "it is already marked"
        return False
    else:
        if turn%2==0:
            board[ac_row][ac_col] ="O"
            #print board[ac_row][ac_col]
        else:
            board[ac_row][ac_col] = "X"
            #print board[ac_row][ac_col]
        return True


print "First player gets: O and Second player gets: X"

turn=0
while True:
    #print "Enter the row and column number to place your mark"
    if turn%2==0:
        print "First player has to choose"
    else :
        print "Second player has to choose"
    row_val = raw_input("row number: ")
    col_val = raw_input("column number: ")

    if place_mark(row_val,col_val,turn):
        print
        print_board()
        print
        if who_wins():
            break
        else:
            turn+=1
