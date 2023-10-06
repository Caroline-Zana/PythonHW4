class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def shape(self):
        return "This a shape"


class Circle(Shape):
    def __init__(self, x, y, size):
        super().__init__(x, y)
        self.size = size

    def draw(self):
        return f"""
        ({self.x}, {self.y})
        {self.size}
        , - ~ ~ ~ - ,
        , ' ' ,
        , ,
        , ,
        , ,
        , ,
        , ,
        , ,
        , ,
        , , '
        ' - , _ _ _ , '
        """


def main():
    c = Circle(1, 2, 3)
    print(c.shape())
    print(c.draw())


if __name__ == "__main__":
    main()
