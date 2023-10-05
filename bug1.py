class Base:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size


class Circle(Base):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)

    def draw(self):
        return f"""
        ({self.x}, {self.y}) {self.size}
        ,-~~~-,
        ,' ', ,, ,, ,, ,, ,, ,, ,,
        ,,' '-,___, '
        """


class Square(Base):
    def shape(self):
        return "This is a square"


def main():
    s = Square(1, 2, 3)
    print(s.shape())
    print(s.draw())


if __name__ == "__main__":
    main()
