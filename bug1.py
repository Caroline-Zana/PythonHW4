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


def main():
    c = Circle(2, 2, 1)
    print("This is a circle")
    print(c.draw())


if __name__ == "__main__":
    main()
