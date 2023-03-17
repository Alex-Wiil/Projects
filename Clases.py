from random import *
class Card:
    '''Карта'''
    def __init__(self, suit, rang):
        self.suit = suit
        self.rang = rang
class Deck:
    '''Колода карт'''
    suits = ['пик', 'червей', 'треф', 'крести']
    rangs = ['2', '3', '4', '5', '6', '7', '8', '9', 'Дама', 'Валет', 'Король', 'Туз']
    deck = list()

    for suit in suits:
        for rang in rangs:

            if rang in ['Дама', 'Валет', 'Король']:
                score = 10

            elif rang in 'Туз':
                score = 11

            else:
                score = rang
                rang = ''.join([rang, '-ка'])
            deck.append(f'{rang} {suit} - {score}')
    def __init__(self):
        self.random_lst = list()
        self.card_counter = 0
        self.bet = 0
    def random_deck(self):
        self.random_lst = list(range(1, 49))
        shuffle(self.random_lst)
        copy_lst = self.random_lst.copy()
        self.random_lst = [Deck.deck[i_card - 1] for i_card in copy_lst]

class Computer:
    def __init__(self):
        self.name = 'Компьютер'
        self.cards = list()
        self.scores = 0
        self.money = 10000
    def print_info(self):
        if self.cards is not list():
            cards = ', '.join(self.cards)
            print(f'\n{self.name}\nКарты на руках: {cards}\nТекущая сумма очков: '
                  f'{self.scores}')
            print(f'денег на счету: {self.money}')
        else:
            print(f'\n\nИгрок: {self.name}\nКарт на руках нет')
class Player:
    '''Игрок'''
    def __init__(self, name, money):
        self.name = name
        self.cards = list()
        self.scores = 0
        self.money = money
    def print_info(self, person):
        if self.cards is not list():
            cards = ', '.join(person.cards)
            print(f'\nИгрок: {person.name}\nКарты на руках: {cards}\nТекущая сумма очков: '
                  f'{person.scores}')
            print(f'денег на счету: {person.money}')
        else:
            print(f'\n\nИгрок: {person.name}\nКарт на руках нет')
    def print_score(self, person):
        print(f'Текущее количество очков: {person.scores}')

