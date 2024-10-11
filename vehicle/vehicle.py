class Vehicle:
    __COLOR_VARIANTS = ['blue',
                        'red',
                        'green',
                        'black',
                        'white']

    def __init__(self,
                 owner,
                 model,
                 engine_power,
                 color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return (f'Мощность двигателя: '
                f'{self.__engine_power}')

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()}\n'
              f'{self.get_horsepower()}\n'
              f'{self.get_color()}\n'
              f'Владелец: {self.owner}\n')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}\n')