import random
from noughts_and_crosses_move_exception import invalid_move

def draw_grid(Grid,spacer):
    for m in range(3):
        Line=Grid[m]
        Line=[Line[0],'|',Line[1],'|',Line[2]]
        for n in range(5):
            print(Line[n], end='')
        print()
        if m<2:
            for n in range(5):
                print('-', end='')
            print()
    print(' ')

def choose_square(Grid,piece,player):
    if player==1:
        print(piece)
        x=input('Player, choose a row number: ')
        y=input('Now choose a column number: ')
    elif player==0:
        [x,y]=random_select()
    x=int(x)
    y=int(y)
    X=x-1
    Y=y-1
    try:
        invalid_move(Grid,x,y)
        Grid[X][Y]=piece
        return [Grid,x,y]
    except ValueError as e:
        if player==1:
            print(e, 'Please select another square.')
        [Grid,x,y]=choose_square(Grid,piece,player)
        return [Grid,x,y]

def random_select():
    x=random.randrange(1,4)
    y=random.randrange(1,4)
    return[x,y]

def have_you_won(Grid,piece,x,y,player):
    Candidates=[]
    Row=check_row(Grid,x)
    Candidates.append(Row)
    Column=check_others(Grid,y,'Vertical')
    Candidates.append(Column)
    if x==y:
        Diag1=check_others(Grid,y,'Diag_forward')
        Candidates.append(Diag1)
    if x+y==4:
        Diag2=check_others(Grid,y,'Diag_backward')
        Candidates.append(Diag2)
    for char in range(len(Candidates)):
        if is_line_winning(Candidates[char]):
            if player==1:
                return ['Well done, you are the winner']
            elif player==0:
                return ['Sorry, the computer has won this time.']
    return ''

def check_row(Grid,x):
    Row=Grid[x-1]
    return Row

def check_others(Grid,y,offset):
    Row=[]
    for char in range(3):
        if offset=='Vertical':
            Row.append(Grid[char][y-1])
        elif offset=='Diag_forward':
            Row.append(Grid[char][char])
        elif offset=='Diag_backward':
            Row.append(Grid[char][2-char])
    return Row

def is_line_winning(Line):
    if Line[0]==Line[1]==Line[2]:
        return True
    else:
        return False

def one_player_noughts_and_crosses():
    Grid=[[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
    spacer=['-','-','-','-','-']
    Moves=1
    Winner=''
    P=random.randrange(0,2)
    while Moves<=9 and Winner=='':
        if (Moves%2)==0:
            piece='x'
        elif (Moves%2)==1:
            piece='o'
        player=P%2
        draw_grid(Grid,spacer)
        [Grid, x, y]=choose_square(Grid,piece,player)
        if Moves>=5:
            Winner=have_you_won(Grid,piece,x,y,player)
        Moves=Moves+1
        P=P+1
    draw_grid(Grid,spacer)
    if Winner!='':
        Winner="".join(Winner)
        print(Winner)
    elif Moves>9:
        print('This game has ended in a draw.')
