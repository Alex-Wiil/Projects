
# Условия игры Sims следующие.

# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
# есть;
# играть;
# ходить на работу.

# Жена может:
# есть;
# покупать продукты;
# покупать шубу;
# убираться в доме.

# Кот может:
# есть;
# спать;
# драть обои.

# Ребенок может;
# Спать
# Есть
# Плакать 
# Играть с котом

# Все они живут в одном доме, дом характеризуется:
#   количеством денег в тумбочке (вначале 100);
#   количеством еды в холодильнике (вначале 50);
#   едой для кота (вначале 30);
#   количеством грязи (вначале 0).

# У людей есть имя, степень сытости (вначале 30) и степень счастья (вначале 100).
# Все люди могут гладить кота (+5 к счастью).
# У кота есть имя и степень сытости (вначале 30).

# Любое действие (в том числе и кота), кроме «есть»,
# приводит к уменьшению степени сытости на 10 пунктов.

# Взрослые едят максимум по 30 единиц еды, степень сытости растёт на один пункт за один пункт еды.
# Кот ест максимум по 10 единиц еды, степень сытости растёт на два пункта за один пункт еды.

# Степень сытости не должна падать ниже нуля, иначе человек или кот умрёт от голода.

# Деньги в тумбочку добавляет муж после работы — сразу 150 единиц.

# Еда стоит 10 денег за 10 единиц еды. Шуба стоит 350 единиц.
# Еда для кота тоже покупается — за 10 денег 10 еды.
# Грязь добавляется каждый день по пять пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если кот дерёт обои, то грязи тоже становится больше на пять пунктов.
# Если в доме грязи больше 90, у людей падает степень счастья каждый день на 10 пунктов.
# Степень счастья растёт: у мужа от игры в компьютер (на 20),
# у жены от покупки шубы (на 60, но шуба дорогая).
# Степень счастья не должна падать ниже 10, иначе человек умирает от депрессии.


class Home:
    def __init__(self):
        self.__money = 100
        self.__food = 50
        self.__cats_food = 30
        self.__dirt = 0
        self.__furs_counter = 0
        self.__foods_counter = 0
        self.__money_counter = 0

    def __str__(self):
        return f'\nДенег дома: {self.__money}\nЕды дома: {self.__food}' \
               f'\nЕды для кота дома: {self.__cats_food}\nЗагрязненность дома: {self.__dirt}'

    def get_furs_counter(self):
        return self.__furs_counter
    def set_furs_counter(self, value):
        self.__furs_counter = value

    def get_foods_counter(self):
        return  self.__foods_counter
    def set_foods_counter(self, value):
        self.__foods_counter = value

    def get_money_counter(self):
        return self.__money_counter
    def set_money_counter(self, value):
        self.__money_counter = value

    def get_money(self):
        return self.__money
    def get_food(self):
        return self.__food
    def get_cats_food(self):
        return self.__cats_food
    def get_dirt(self):
        return self.__dirt

    def set_money(self, value):
        self.__money = value
    def set_food(self, value):
        self.__food = value
    def set_cats_food(self, value):
        self.__cats_food = value
    def set_dirt(self, value):
        self.__dirt = value

import random

class Person:
    def __init__(self, name):
        self.__name = name
        self.__satiety = 30
        self.__happiness = 100
        self.__being = True

    def get_name(self):
        return self.__name

    def get_being(self):
        return self.__being
    def set_being(self, value):
        self.__being = value


    def get_satiety(self):
        return self.__satiety
    def set_satiety(self, value):
        self.__satiety = value

    def get_happiness(self):
        return self.__happiness
    def set_happiness(self, value):
        self.__happiness = value

    def __str__(self):
        if self.__being:
            return f'\nИмя: {self.get_name()}\nСытость: {self.get_satiety()}\nСчастье: {self.get_happiness()}'
        else:
            return  f'\n{self.get_name()} мертв'

    def petting_cat(self):
        self.__satiety -= 10
        self.__happiness += 20
        print(f'{self.get_name()} гладил кота.')

    def eating(self):
        meal = random.randint(10, 20)
        self.__satiety += meal
        home.set_food(home.get_food() - meal)
        home.set_foods_counter(home.get_foods_counter() + meal)
        print(f'{self.get_name()} поел.')

    def action(self):
        new_satiety = self.get_satiety() - 10
        self.set_satiety(new_satiety)

    def checking(self):
        if self.__being:
            if self.get_satiety() <= 0:
                print(f'{self.get_name()} - смерть от голода!')
                self.set_being(False)
            elif self.get_happiness() < 10:
                print(f'{self.get_name()} - смерть от депрессии!')
                self.set_being(False)

            if home.get_food() <= 0:
                print('Еда закончилась')
            elif home.get_money() <= 0:
                print('Деньги закончились')
            elif home.get_cats_food() <= 0:
                print('Еда для кота закончилась')

            if  self.get_satiety() > 0 and self.get_happiness() >= 10:
                return True

class Husband(Person):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        home.set_money(home.get_money() + 150)
        self.action()
        home.set_money_counter(home.get_money_counter() + 150)
        print(f'{self.get_name()} (муж) - работал.')

    def play(self):
        self.set_happiness(self.get_happiness() + 20)
        self.action()
        print(f'{self.get_name()} (муж) - играл в компьютер.')

    def daily_life(self):
        if self.checking():
            self.set_happiness(self.get_happiness() - 1)
            if self.get_satiety() <= 10:
                self.eating()
            else:
                if self.get_happiness() <= 15:
                    choice = ['кот', 'игра'][random.randint(0, 1)]
                    if choice == 'кот':
                        self.petting_cat()
                    else:
                        self.play()
                else:
                    self.work()

class Wife(Person):

    def __init__(self, name):
        super().__init__(name)

    def cleaning(self):
        clean = random.randint(80, 100)
        if home.get_dirt() < clean:
            home.set_dirt(0)
        else:
            home.set_dirt(home.get_dirt() - clean)
        self.action()
        print(f'{self.get_name()} (жена) - убиралась дома.')

    def shopping(self):
        home.set_money(home.get_money() - 350)
        self.set_happiness(self.get_happiness() + 60)
        self.action()
        home.set_furs_counter(home.get_furs_counter() + 1)
        print(f'{self.get_name()} (жена) - купила шубу.')

    def buy_groceries(self):
        home.set_food(home.get_food() + 50)
        home.set_cats_food(home.get_cats_food() + 20)
        home.set_money(home.get_money() - 70)
        self.action()
        print(f'{self.get_name()} (жена) - купила продукты и кошачий корм.')

    def daily_life(self):
        if self.checking():
            self.set_happiness(self.get_happiness() - 1)
            if self.get_satiety() <= 10:
                self.eating()
            else:
                if self.get_happiness() <= 30:

                    choice = ['кот', 'шуба'][random.randint(0, 1)]
                    if choice == 'кот':
                        self.petting_cat()
                    else:
                        self.shopping()
                else:
                    if home.get_food() <= 60 or home.get_cats_food() <= 15:
                        self.buy_groceries()
                    else:
                        self.cleaning()

class Cat:
    def __init__(self, name):
        self.__name = name
        self.__cats_satiety = 30

    def get_cats_name(self):
        return  self.__name

    def get_cats_satiety(self):
        return  self.__cats_satiety

    def set_cats_satiety(self, value):
        self.__cats_satiety = value

    def eating(self):
        meal = random.randint(1, 5)
        self.__cats_satiety += meal * 2
        home.set_cats_food(home.get_cats_food() - meal)
        print(f'Кот {self.__name} поел.')

    def make_mess(self):
        home.set_dirt(home.get_dirt() + 5)
        self.__cats_satiety -= 10
        print(f'Кот {self.__name} драл обои.')

    def slipping(self):
        self.__cats_satiety -= 10
        print(f'Кот {self.__name} спал.')

    def daily_life(self):
        if self.get_cats_satiety() <= 0:
            print('Кот умер.')
        else:
            if self.get_cats_satiety() <= 15:
                self.eating()
            else:
                choice = ['спать', 'вредить'][random.randint(0, 1)]
                if choice == 'спать':
                    self.slipping()
                else:
                    self.make_mess()

class Child(Person):
    def play_with_cat(self):
        self.set_happiness(self.get_happiness() + 15)
        self.action()
        print(f'{self.get_name()} играл с котом')

    def crying(self):
        self.set_happiness(self.get_happiness() - 5)
        self.action()
        print(f'{self.get_name()} плакал')

    def sleeping(self):
        self.set_happiness((self.get_happiness() + 5))
        self.action()
        print(f'{self.get_name()} спал')

    def daily_rutine(self):
        if self.checking():
            # self.set_happiness(self.get_happiness() - 1)
            if self.get_satiety() <= 10:
                self.eating()
            else:
                if self.get_happiness() <= 10:

                    choice = ['сон', 'игра'][random.randint(0, 1)]
                    if choice == 'сон':
                        self.sleeping()
                    else:
                        self.play_with_cat()
                else:
                    self.crying()

class Life:
    def main(self):
        ben = Husband('Ben')
        sindy = Wife('Sindy')
        cat1 = Cat('Tom')
        cat2 = Cat('Jerry')
        child1 = Child('Jimmi')

        for i in range(1, 366):
            if not ben.get_being():
                break
            if home.get_dirt() >= 90:
                ben.set_happiness(ben.get_happiness() - 10)
                sindy.set_happiness(sindy.get_happiness() - 10)
            home.set_dirt(home.get_dirt() + 5)

            print('\n')
            print(f'День {i}-й'.center(50))
            print('~' * 50, '\n')

            ben.daily_life()
            sindy.daily_life()
            cat1.daily_life()
            cat2.daily_life()
            child1.daily_rutine()

            print(ben)
            print(sindy)
            print(child1)

            print(f'\nСытость {cat1.get_cats_name()} (кот):   {cat1.get_cats_satiety()}')
            print(f'Сытость {cat2.get_cats_name()} (кот): {cat2.get_cats_satiety()}')
            print(home)

        print('~' * 50)
        print('~' * 50)
        print(f'\nЗА ВСЁ ВРЕМЯ:\nЕды сьедено:  {home.get_foods_counter()}\n'
              f'Денег заработано: {home.get_money_counter()}\n'
              f'Шуб куплено: {home.get_furs_counter()}')

home = Home()
life = Life()
life.main()
