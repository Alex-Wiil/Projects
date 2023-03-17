
# Автомобиль имеет координаты своего положения и угол, описывающий направление движения.
# Он может быть изначально поставлен в любую точку с любым направлением,
# может проехать в выбранном направлении определённое расстояние и может повернуть,
# то есть изменить текущее направление на любое другое (передаём привет математике и формулам).

# У автобуса, кроме того, что имеется у автомобиля, имеются поля,
# содержащие число пассажиров и количество полученных денег, изначально равное нулю.
# Также есть методы «войти» и «выйти», изменяющие число пассажиров.


import math
class Car:
    '''
        Класс Автомобиль, который описывает функции автомобиля
        Args:
           __coordinate_x int: координаты x
           __coordinate_y int: координаты y
           __direction int: направление

        Methods:
            print_coordinates: Выводит на экран координаты автомобиля
            going: Метод который по заданному направлению (градусы) и заданной дальности (километры),
                  определяет новые координаты автомобиля
    '''

    def __init__(self, coordinate_x, coordinate_y):
        self.__coordinate_x = coordinate_x
        self.__coordinate_y = coordinate_y
        self.__direction = 0

    def print_coordinates(self):
        print(f'x: {self.__coordinate_x}, y: {self.__coordinate_y}')

    def going(self, dictance, direction):
        '''
            Метод Движение, который определяет координаты пункта назначения по расстоянию и направлению и
            присваивает координатам автомобиля новые значения

            :param dictance int: расстояние до точки назначения(км)
            :param direction int: направление движения(градусы)

                Сначала метод проверяет введенные значения: расстояние и направление на соответствие
            допустимым, в противном случае выводит сообщение об ошибке

                Затем приводит значение направления к "рабочему значению" (число от -360 до 360)
                Если значение направления отрицательное, переводит его в соответсвующее положительное

                Далее находятся новые координаты автомобиля методом сложения старых координат и
            расстояния по осям x и y до точки назначения, (метод по двум углам и стороне треугольника)
                Известное расстояние - это гипотенуза, два катета - это расстояние по оси x и y.

                Если направление равно 0, то координаты x не изменяются,а координаты y - увеличиваются на расстояние.
                Если направление в диапазоне от 1 до 90, то координаты x и y - увеличиваются на длины
            соответствующих катетов.
                Если направление в диапазоне от 91 до 180, то координаты x - увеличиваются на длину
            соответствующего катета, а координаты y - уменьшаются.
                Если направление в диапазоне от 181 до 270, то координаты x - уменьшаются на длину
            соответствующего катета, а координаты y - уменьшаются.
                Если направление в диапазоне от 271 до 360, то координаты x и y - уменьшаются на длины
            соответствующих катетов.

                Далее координатам автомобиля, присваивается новое значение.
                Направлению в котором стоит автомобиль присваивается новое значение которое соответствует
            формату(от 0 до 359 градусов)

        '''

        if not isinstance(dictance, (int, float)) or not isinstance(direction, (int, float)):
            print('Ошибка. Введены некорректные данные.')
            return

        self.__direction += direction
        direction = self.__direction
        direction %= 360

        if direction < 0:
            direction = 360 + direction

        x2 = math.cos(math.radians(90 - direction)) * dictance
        y2 = math.sin(math.radians(90 - direction)) * dictance

        if direction in range(91, 181):
            x2 = math.sin(math.radians(180 - direction)) * dictance
            y2 = - math.cos(math.radians(180 - direction)) * dictance

        elif direction in range(181, 271):
            x2 = - math.cos(math.radians(270 - direction)) * dictance
            y2 = - math.sin(math.radians(270 - direction)) * dictance

        elif direction in range(271, 361):
            x2 = - math.sin(math.radians(360 - direction)) * dictance
            y2 = math.cos(math.radians(360 - direction)) * dictance

        elif direction == 0:
            x2 = 0
            y2 = dictance

        self.__coordinate_x = self.__coordinate_x + x2
        self.__coordinate_y = self.__coordinate_y + y2
        self.__direction %= 360

class Bus(Car):
    '''
            Класс Автобус, который описывает функции автобуса
            Args:
               __coordinate_x int: координаты x
               __coordinate_y int: координаты y
               __direction int: направление
               __money int: деньги в кассе
               __killometrage int: километраж
               __seats list: список мест в автобусе(1 - место, занято, 0 - свободно)
               __pasangers int: количество пассажиров
            Methods:
                __str__: выводит информацию о автобусе
                enter int: метод который осуществляет посадку пассажиров
                exit int: метод который осуществляет высадку пассажиров
                print_pasangers: выводит информацию о количестве пассажиров
                move: метод который вызывает метод going(осуществляет движение),а также
                расчитывает прибыль и километраж
        '''

    def __init__(self, coordinate_x, coordinate_y):
        super().__init__(coordinate_x, coordinate_y)
        self.__money = 0
        self.__killometrage = 0
        self.__seats = [0 for i in range(18)]
        self.__pasangers = 0


    def __str__(self):
        print('Статус автобуса:'.upper())
        self.print_pasangers()
        return f'  Денег в кассе: {self.__money}\n  Километров пройдено: {self.__killometrage}\n'

    def enter(self, pasangers):
        if not isinstance(pasangers, int) or pasangers <= 0:
            print('Ошибка, некорректное значение числа пассажиров.')
            self.enter(int(input('Введите число пассажиров ')))
        if 18 - self.__pasangers < pasangers:
            print(f'В автобусе недостаточно мест.\n'
                  f'Количество пассажиров которые не поместились {pasangers - 18 - self.__pasangers}')
            self.__pasangers = 18
        else:
            print(f'В атобус вошло пассажиров: {pasangers}')
            self.__seats = self.__seats[:-pasangers]
            self.__pasangers += pasangers


    def exit(self, pasangers):
        if not isinstance(pasangers, int) or pasangers <= 0:
            print('Ошибка, некорректное значение числа пассажиров.')
            self.exit(int(input('Введите число пассажиров ')))
        if pasangers > self.__pasangers:
            print('Неверное значение, в автобусе нет столько пассажиров.')
            self.exit(int(input('Введите число пассажиров ')))
        else:
            print(f'Из атобуса вышло пассажиров: {pasangers}')
            self.__seats = self.__seats[:-pasangers]
            self.__pasangers -= pasangers

    def print_pasangers(self):
        print('  Пассажиров:', self.__pasangers)

    def move(self, dictance, direction):
        print(f'\nАвтобус проехал {dictance} км\n')
        self.going(dictance, direction)
        self.__money += dictance * 5 * self.__pasangers
        self.__killometrage += dictance

car = Car(0, 0)
# car.print_coordinates()
# car.going(4, 180)
# car.print_coordinates()
# car.going(4, 180)
# car.print_coordinates()
# print()
bus = Bus(0, 0)
bus.going(4, 180)
bus.print_coordinates()
bus.going(4, 180)
bus.print_coordinates()

# bus.print_pasangers()
print(bus)

bus.enter(12)
bus.move(dictance=5, direction=90)
print(bus)

bus.exit(9)
bus.move(dictance=7, direction=180)
print(bus)

bus.move(dictance=15, direction=90)
print(bus)
