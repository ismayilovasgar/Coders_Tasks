class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Piece:
    first_move = "True"

    def __init__(self, color):
        if color.lower() != 'black' and color.lower() != 'white':
            raise ValueError('Invalid Color Value')
        self.color = color.lower()

    def __str__(self):
        return f'The current piece color is {self.color} and the strong is {self.get_strong()}'

    def __repr__(self):
        return f'The current piece color is {self.color} and the strong is {self.get_strong()}'

    def get_strong(self): # Override
        pass


class Pawn(Piece):
    shape = "P"
    type = "Pawn"
    __strong = "1"

    def __init__(self, color):
        super().__init__(color)

    @classmethod
    def get_strong(cls):
        return cls.__strong

    @classmethod
    def set_strong(cls, value):
        cls.__strong = value


class Rook(Piece):
    shape = "R"
    type = "Rook"
    __strong = "5"

    def __init__(self, color):
        super().__init__(color)

    @classmethod
    def get_strong(cls):
        return cls.__strong

    @classmethod
    def set_strong(cls, value):
        cls.__strong = value


class Knight(Piece):
    shape = "N"
    type = "Knight"
    __strong = "3"

    def __init__(self, color):
        super().__init__(color)

    @classmethod
    def get_strong(cls):
        return cls.__strong

    @classmethod
    def set_strong(cls, value):
        cls.__strong = value


class Bishop(Piece):
    shape = "B"
    type = "Bishop"
    __strong = "3"

    def __init__(self, color):
        super().__init__(color)

    @classmethod
    def get_strong(cls):
        return cls.__strong

    @classmethod
    def set_strong(cls, value):
        cls.__strong = value


class Queen(Piece):
    shape = "Q"
    type = "Queen"
    __strong = "9"

    def __init__(self, color):
        super().__init__(color)

    @classmethod
    def get_strong(cls):
        return cls.__strong

    @classmethod
    def set_strong(cls, value):
        cls.__strong = value


class King(Piece):
    shape = "K"
    type = "King"
    __strong = "priceless"

    def __init__(self, color):
        super().__init__(color)

    @classmethod
    def get_strong(cls):
        return cls.__strong

    @classmethod
    def set_strong(cls, value):
        cls.__strong = "priceless"


# ----------------------------------------------
pos = Position(4, 5)
pawn = Pawn("white")
print(pawn)  # The current piece is white and the age is 1

pawn = Pawn("Black")
print(pawn)  # The current piece is black and the age is 1
