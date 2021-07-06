

class Coord:
    def __init__(self, draft_coord='a1'):
        self.letter: str = draft_coord[0]
        self.digit: int = int(draft_coord[1])


class ChessFigure:
    def __init__(self, isWite: bool = True):
        self.is_white = isWite


class Pawn(ChessFigure):
    pass


def safe_pawns(pawns: set) -> int:
    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
