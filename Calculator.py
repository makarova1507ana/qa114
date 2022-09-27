class divisorEqualZero(Exception):#класс для исключения (деление на ноль)
    pass

class Calculator:
    def __init__(self, x1, x2):#просто пустой инициализатор
        if x2 == 0:
            raise divisorEqualZero(x2)  # выбрасываем исключение в класс описанный выше
        self.x1 = x1
        self.x2 = x2

    def add(self):# метод сложения двух переданных переменных
        return self.x1 + self.x2

    def mult(self):# метод умножения двух переданных переменных
        return self.x1 * self.x2

    def subtr(self):# метод вычитания двух переданных переменных
        return self.x1 - self.x2

    def div(self):# метод деления двух переданных переменных
        return self.x1 / self.x2