import random
from rectangle import Rectangle


class RectangleCreator:
    FIRST_SIDE_RANGE = 10  # от 1 до 10
    SECOND_SIDE_RANGE = 20  # от 1 до 20

    def get_rectangles(size):  # size - количество прямоугольников
        rectangles = []

        for _ in range(size):
            rect = Rectangle()
            rect.a = random.randint(1, RectangleCreator.FIRST_SIDE_RANGE)  # добавили RectangleCreator перед переменной , так она была не видна (к ней нужно обращаться по имени класса)
            rect.b = random.randint(1, RectangleCreator.SECOND_SIDE_RANGE)
            rectangles.append(rect)
        return rectangles
