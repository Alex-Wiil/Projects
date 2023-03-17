import itertools
class Board:
    """Поле клеток"""
    def __init__(self):
        self.cells = [[i + k for k in range(3)] for i in range(1, 10, 3)]
        self.cells_lst = list(itertools.chain(*self.cells))
        self.moves = list()
        self.moves_count = len(self.moves)

class Player:
    '''Игрок'''
    def __init__(self):
        self.name = ''
        self.player_symb = 'X'

import itertools
import tabulate
class Game:
    '''Игра'''
    def start(self):
        print('\n          ДОБРОГО ВРЕМЕНИ СУТОК!\nРАДЫ ПРИВЕТСТВОВАТЬ ВАС В ИГРЕ КРЕСТИКИ '
              'НОЛИКИ!\n'.center(80))

        player1.name = input('Первый игрок - введите ваше имя: ')
        player2.name = input('Второй игрок - введите ваше имя: ')
        player2.player_symb = '0'
        print('\nПеред вами игровое поле, где каждая клетка имеет номер от 1 до 9.\n')
        self.print_picture()

    def print_picture(self):
        print("\033[3m\033[34m{}\033[0m".format(tabulate.tabulate(board.cells, tablefmt="fancy_grid")))

    def wins_combination(self):
        cel = board.cells
        fst, sec, thr = cel[0], cel[1], cel[2]

        if fst[0] == fst[1] == fst[2] or\
            sec[0] == sec[1] == sec[2] or\
            thr[0] == thr[1] == thr[2] or \
            fst[0] == sec[0] == thr[0] or \
            fst[1] == sec[1] == thr[1] or \
            fst[2] == sec[2] == thr[2] or \
            fst[0] == sec[1] == thr[2] or \
            fst[2] == sec[1] == thr[0]:
            return True
        return False

    def question_for_player(self, player1):

        while True:
            cell = (input(f'\n{player1} - Ваш ход.\nВведите номер клетки(от 1 до 9): '))

            if cell.isdigit() and 0 < int(cell) < 10 and int(cell) in board.cells_lst and int(cell) \
                    not in board.moves:
                board.moves.append(int(cell))
                return int(cell)
            print('Ошибка. Необходимо ввести номер свободной клетки (число от 1 до 9).')

    def player_step(self, cell, player_symb):

       main_lst = list()
       for row in board.cells:
           row_lst = list()
           for num in row:
               if num == cell:
                   row_lst.append(player_symb)
               else:
                   row_lst.append(num)
           main_lst.append(row_lst)
       board.cells = main_lst

    def games_circle(self, player):
        if board.moves_count != 9:
            board.moves_count += 1
            cell = self.question_for_player(player.name)
            self.player_step(cell, player.player_symb)
            print('\n')
            self.print_picture()


    def print_winer(self, player):
        print('\n\n\n')
        print(f'Победил {player}!'.upper().center(80))

    def print_drow(self):
        print('\n')
        print(f'НИЧЬЯ!'.center(80))

    def main(self, player1, player2):
        game.start()
        while board.moves_count != 9:
            self.games_circle(player1)
            if self.wins_combination():
                self.print_winer(player1.name)
                return

            self.games_circle(player2)
            if self.wins_combination():
                self.print_winer(player2.name)
                return
        self.print_drow()

player1 = Player()
player2 = Player()
board = Board()
game = Game()
game.main(player1, player2)
