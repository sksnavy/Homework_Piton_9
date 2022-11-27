# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

board = {'1': ' ' , '2': ' ' , '3': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '7': ' ' , '8': ' ' , '9': ' ' }

print ('Формат доски:')
print('1 2 3')         
print('4 5 6')
print('7 8 9')
print('-----')

board_keys = []

for key in board:
    board_keys.append(key)

def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def print_pobeda(turn):
    print("Игра окончена")                
    print("Победил: " +turn)

def game():

    turn = 'X'
    count = 0

    for i in range(10):
        print("Ходит игрок, " + turn + ". Выберите клетку")
        print_board(board)
        
        move = input()        

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("Клетка занята.")
            print("Выберите клетку")
            continue

        
        if count >= 5:
            if board['1'] == board['2'] == board['3'] != ' ': # Пересечение по верхней линии
                print_board(board)
                print_pobeda(turn)               
                break
            elif board['4'] == board['5'] == board['6'] != ' ': # Пересечение по средней линии
                print_board(board)
                print_pobeda(turn)
                break
            elif board['7'] == board['8'] == board['9'] != ' ': # Пересечение по нижней линии
                print_board(board)
                print_pobeda(turn)
                print_pobeda(turn)
                break
            elif board['1'] == board['4'] == board['7'] != ' ': # Пересечение по левому краю
                print_board(board)
                print_pobeda(turn)
                break
            elif board['2'] == board['5'] == board['8'] != ' ': # Пересечение по средней линии
                print_board(board)
                print_pobeda(turn)
                break
            elif board['3'] == board['6'] == board['9'] != ' ': # Пересечение по левому краю
                print_board(board)
                print_pobeda(turn)
                break 
            elif board['3'] == board['5'] == board['7'] != ' ': # Пересечение по диагонали
                print_board(board)
                print_pobeda(turn)
                break
            elif board['1'] == board['5'] == board['9'] != ' ': # Пересечение по диагонали
                print_board(board)
                print_pobeda(turn)
                break 
        
        if count == 9:
            print("Конец игры")                
            print("Ничья!")
        
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
        
    restart = input("Хотите сыграть ещё раз? (y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            board[key] = " "
        
        game()

if __name__ == "__main__":
    game()