# нтерфейс для взаимодействия  - вызввать сами прямоугольники


from rectangle import Rectangle


class View:
    def convert(rectangles):
        if isinstance(rectangles, (list, tuple)):
            result = "List of rectangles:\n"
            for rect in rectangles:
                if isinstance(rect, Rectangle):
                    result += str(rect) + "\n"

            return result
