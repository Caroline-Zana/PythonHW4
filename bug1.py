class Base:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape(Base):
    def shape(self):
        return f"This is a {self.__class__.__name__.lower()} ({self.x}, {self.y})"

class Square(Shape):
    def __init__(self, x, y, size):
        super().__init__(x, y)
        self.size = size

    def draw(self):
        return f"{super().shape()}\n{'#' * self.size}"

class Circle(Shape):
    def __init__(self, x, y, size):
        super().__init__(x, y)
        self.size = size

    def draw(self):
        return f"{super().shape()}\n,-~~~-,\n,' ', ,, ,, ,, ,, ,, ,, ,,\n,,' '-,___, 
'"

def main():
    s = Square(1, 2, 3)
    print(s.shape())
    print(s.draw())

if __name__ == "__main__":
    main()

