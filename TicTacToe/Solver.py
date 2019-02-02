class Solver(object):
    def __init__(self):
        pass
    
    def getWinner(self, game_board):
        case_table = {
            0 : "0",
            1 : "X",
            None: "<tie>"
        }

        result = self._getWinner(game_board)

        return case_table[result]
    
    def _getWinner(self, game_board):
        row_winner = self._row_winner(game_board)
        if row_winner:
            return row_winner

        column_winner = self._column_winner(game_board)
        if column_winner:
            return column_winner

        diagonal_winner = self._diagonal_winner(game_board)
        if diagonal_winner:
            return diagonal_winner

        return None

    def _row_winner(self, game_board):
        for row in game_board:
            if row[0] == row[1] == row[2]:
                # Must return the winning_character
                return row[0]

        return None 

    def _column_winner(self, game_board):
        for i in range(3):
            if game_board[0][i] == game_board[1][i] == game_board[2][i]:
                return game_board[0][i]
        
        return None

    def _diagonal_winner(self, game_board):
        right_left_diagonal = game_board[0][0] == game_board[1][1] == game_board[2][2]
        left_right_diagonal = game_board[2][2] == game_board[1][1] == game_board[0][0]

        if right_left_diagonal or left_right_diagonal:
            return game_board[1][1]
        
        return None