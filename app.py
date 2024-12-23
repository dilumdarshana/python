def user_choice(player: str):
    choice = 'W'
    while (choice == '' or choice.isdigit() == False or int(choice) not in range(1,10)):
        choice = input('Please enter number (1-9): ')

        if (choice.isdigit() == False):
            print('Invalid input. Please enter a number.')

        if (choice == '' or int(choice) not in range(1,10)):
            print('Invalid input. Please enter between 1 and 9')
    return int(choice)

def draw_board():
    board = [' ']*9
    for i in range(9):
        if (i % 3 == 0):
            print('-------------')
        print('|', board[i], '|', board[i], '|', board[i], '|')

    

def display():
    print('Welcome to Tic Tac Toe Game...')
    print ('Player A -> X, Player B -> O')

    # draw the board
    draw_board()
    # get user choice
    #choice = user_choice('')

# display()


def addSpaces(s: str, spaces) -> str:
    result = []

    count = 0
    for cha in s:
        if count === 
        result.append(cha)

    for spac in spaces:
        result.append(s[spac])

    return ''.join(result)

res = addSpaces('LeetcodeHelpsMeLearn', [8,13,15]);
print(res)
