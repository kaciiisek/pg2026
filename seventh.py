class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position

        if self.color == "white":
            move = (row + 1, col)
        else:
            move = (row - 1, col)

        if self.is_position_on_board(move):
            return [move]
        return []

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        for i in range(1, 8):
            directions = [
                (row + i, col + i),
                (row + i, col - i),
                (row - i, col + i),
                (row - i, col - i)
            ]

            for move in directions:
                if self.is_position_on_board(move):
                    moves.append(move)

        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        for i in range(1, 9):
            if i != row:
                moves.append((i, col))
            if i != col:
                moves.append((row, i))

        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        # věž + střelec
        row, col = self.position
        moves = []

        # tahy věže
        for i in range(1, 9):
            if i != row:
                moves.append((i, col))
            if i != col:
                moves.append((row, i))

        # tahy střelce
        for i in range(1, 8):
            directions = [
                (row + i, col + i),
                (row + i, col - i),
                (row - i, col + i),
                (row - i, col - i)
            ]

            for move in directions:
                if self.is_position_on_board(move):
                    moves.append(move)

        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        row, col = self.position

        moves = [
            (row - 1, col - 1),
            (row - 1, col),
            (row - 1, col + 1),
            (row, col - 1),
            (row, col + 1),
            (row + 1, col - 1),
            (row + 1, col),
            (row + 1, col + 1)
        ]

        return [move for move in moves
                if self.is_position_on_board(move)]

    def __str__(self):
        return f'King({self.color}) at position {self.position}'
