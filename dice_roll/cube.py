from random import randint

class Cube:
    """Один куб, по умолчанию шестигранный"""
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        # Возвращает случайное число от 1 до числа граний
        return randint(1, self.num_sides)
