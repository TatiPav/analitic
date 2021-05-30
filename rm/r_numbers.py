from random import choice

class RNumbers:
    def __init__(self, n_points=5000):
        self.n_points = n_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_numbers(self):
        while len(self.y_values) < self.n_points:
            # Перемещаемся в направлении до достижения предельной длины,
            # вправо/влево
            x_direction = choice([1, -1])
            # расстояние/выбор  дальности перемещения
            x_distance = choice([0, 1, 2, 3, 4])
            # шаг/направление/расстояние
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # если оба равны нулю
            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


