class ChessPiece:
    def __init__(self, position):
        self.position = position

    def get_valid_moves(self):
        pass


class Rook(ChessPiece):
    def get_valid_moves(self):
        moves = []
        col, row = self.position[0], int(self.position[1])

        # Horizontal moves
        for i in range(1, 9):
            if i != row:
                moves.append(col + str(i))

        # Vertical moves
        for i in range(ord('A'), ord('I')):
            new_col = chr(i)
            if new_col != col:
                moves.append(new_col + str(row))

        return moves


class Queen(ChessPiece):
    def get_valid_moves(self):
        moves = []
        col, row = self.position[0], int(self.position[1])

        # Horizontal moves
        for i in range(1, 9):
            if i != row:
                moves.append(col + str(i))

        # Vertical moves
        for i in range(ord('A'), ord('I')):
            new_col = chr(i)
            if new_col != col:
                moves.append(new_col + str(row))

        # Diagonal moves
        for i in range(1, 9):
            if i != row:
                diff = abs(i - row)
                if ord(col) + diff <= ord('H'):
                    moves.append(chr(ord(col) + diff) + str(i))
                if ord(col) - diff >= ord('A'):
                    moves.append(chr(ord(col) - diff) + str(i))

        return moves


class Bishop(ChessPiece):
    def get_valid_moves(self):
        moves = []
        col, row = self.position[0], int(self.position[1])

        # Diagonal moves
        for i in range(1, 9):
            if i != row:
                diff = abs(i - row)
                if ord(col) + diff <= ord('H'):
                    moves.append(chr(ord(col) + diff) + str(i))
                if ord(col) - diff >= ord('A'):
                    moves.append(chr(ord(col) - diff) + str(i))

        return moves
class Knight(ChessPiece):
    def get_valid_moves(self):
        moves = []
        col, row = self.position[0], int(self.position[1])

        # Knight moves
        knight_moves = [
            (ord(col) + 2, row + 1),
            (ord(col) + 2, row - 1),
            (ord(col) - 2, row + 1),
            (ord(col) - 2, row - 1),
            (ord(col) + 1, row + 2),
            (ord(col) + 1, row - 2),
            (ord(col) - 1, row + 2),
            (ord(col) - 1, row - 2),
        ]

        for move in knight_moves:
            new_col = chr(move[0])
            new_row = move[1]
            if ord('A') <= move[0] <= ord('H') and 1 <= new_row <= 8:
                moves.append(new_col + str(new_row))

        return moves
