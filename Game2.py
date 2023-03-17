from Classes import Deck, Card, Player, Computer
import random

class Game:
    '''Игра'''
    def get_card(self, person, computer):              # ДАТЬ КАРТУ ИЗ КОЛОДЫ
        if self.conditions_for_game(person, computer):

            if deck.card_counter > 47:
                deck.card_counter = 0

            new_card = deck.random_lst[deck.card_counter].split(' - ')

            if person.name != 'Компьютер':
                print(f'  - {new_card[0]}')
            person.cards = person.cards + [new_card[0]]
            score = int(new_card[-1])

            if person.scores >= 21 and score == 11:
                score = 1
            person.scores += score

            deck.card_counter += 1

    def reset_info(self, person):           # СБРОС КАРТ И ОЧКОВ ПОСЛЕ КОНА
        person.cards = list()
        person.scores = 0
        computer.cards = list()
        computer.scores = 0

    def start(self, person):               # НАЧАЛО ИГРЫ(СБРОС И ВЫДАЧА ПО 2 КАРТЫ)
        self.reset_info(person)
        self.get_card(person, computer)
        self.get_card(person, computer)

    def end(self, person, computer):       # КОНЕЦ КОНА(ВЫВОД СТАТУСА ИГРОКОВ)
        person.print_info(person)
        computer.print_info()

    def conditions_for_game(self, person, computer):    # УСЛОВИЯ ДЛЯ ПРОДОЛЖЕНИЯ ИГРЫ

        if person.money <= 0:
            print('У ВАС КОНЧИЛИСЬ ДЕНЬГИ!')
            return False
        elif computer.money <= 0:
            print('У КОМПЬТЕРА КОНЧИЛИСЬ ДЕНЬГИ!')
            return False

        if person.scores > 21:
            # print('> 21')
            print()
            print('ВЫ ПРОИГРАЛИ!\n'.center(50))
            self.winer(computer, person)
            print(f'КОЛИЧЕСТВО ОЧКОВ: {person.scores}.'.center(50))
            self.end(person, computer)
            return False
        else:
            # print('else')
            if person.scores == 21:
                self.result(person, computer)
                return False
            else:
                return True

    def questions_for_player(self, person, computer):          # ВОПРОС ИГРОКУ

        while self.conditions_for_game(person, computer):

            while True:
                question = input('\nЖелаете ещё карту? (да/нет) ').lower().strip()
                if question == 'да':
                    self.get_card(person, computer)
                    player.print_score(player)

                    break
                elif question == 'нет':
                    self.result(person, computer)
                    return
                else:
                    print('Не понял, повторите.')


    def result(self, person, computer):             # ИТОГИ КОНА

        if person.scores > computer.scores or computer.scores > 21:
            word = 'ВЫИГРАЛИ'
            winer, loser = person, computer

        elif person.scores < computer.scores:
            word = 'ПРОИГРАЛИ'
            winer, loser = computer, person
        if person.scores == computer.scores:
            print('\n')
            print('НИЧЬЯ!'.center(50))
            return
        self.winer(winer, loser)
        print()
        print(f'    {person.name.upper()} - ВЫ {word}!'.center(50))


        print(f'КОЛИЧЕСТВО ОЧКОВ ПО: {person.scores}.'.center(50))
        self.end(person, computer)

    def winer(self, person, computer):            # ПОБЕДИТЕЛЬ КОНА
        person.money += deck.bet
        computer.money -= deck.bet

    def bet_checking(self, bet, person):
        if person.money >= bet:
            return True
        return False

    def main(self, person):                     # ОСНОВНАЯ

        print()
        print(f'{player.name.upper()} ДОБРО ПОЖАЛОВАТЬ В ИГРУ 21!'.center(80))

        while self.conditions_for_game(person, computer):

            while True:
                deck.bet = int(input('\nВведите ставку: '))
                if not self.bet_checking(deck.bet, person):
                    print('У вас нет столько денег.')
                elif not self.bet_checking(deck.bet, computer):
                    print('У компьютера недостаточно денег.')
                else:
                    break

            deck.random_deck()
            print()
            print(f'ВЫ ПОЛУЧИЛИ:')
            self.start(player)
            player.print_score(player)
            self.start(computer)
            player.print_info(player)

            self.questions_for_player(player, computer)

            while True:
                play_game = input('Желаете продолжить играть? (да/нет) ').strip().lower()
                if play_game == 'нет':
                    print()
                    print('КОНЕЦ ИГРЫ!\n'.center(50))
                    return
                elif play_game == 'да':
                    self.reset_info(person)
                    break
                else:
                    print('Не понял, повторите.')


computer = Computer()
player = Player('Елизавета Лизочка Лизушка', 10000)
deck = Deck()
game = Game()

game.main(player)
