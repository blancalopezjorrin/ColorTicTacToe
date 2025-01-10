import numpy as np

class ComputerPlayer:
    def __init__(self):
        """
        Inicializa el jugador de computadora como 'X'.
        """
        self.symbol = 'X'
        self.opponent_symbol = 'O'

    def computer_move(self, board):
        """
        Encuentra el mejor movimiento para el jugador de computadora.
        
        Args:
            board (list of list): Representación del tablero como una matriz 3x3.
        
        Returns:
            tuple: Coordenadas del mejor movimiento en formato (fila, columna).
        """
        best_score = -float('inf')
        best_move = None

        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    # Simula el movimiento
                    board[row][col] = self.symbol
                    score = self.minimax(board, False)
                    # Deshace el movimiento
                    board[row][col] = 0
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        
        return best_move

    def minimax(self, board, is_maximizing):
        """
        Aplica el algoritmo minimax para determinar el valor de un movimiento.
        
        Args:
            board (list of list): Representación del tablero como una matriz 3x3.
            is_maximizing (bool): Indica si el jugador actual es el maximizador.
        
        Returns:
            int: La puntuación del tablero.
        """
        winner = self.check_winner(board)
        if winner == self.symbol:
            return 1
        elif winner == self.opponent_symbol:
            return -1
        elif self.is_draw(board):
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == 0:
                        board[row][col] = self.symbol
                        score = self.minimax(board, False)
                        board[row][col] = 0
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == 0:
                        board[row][col] = self.opponent_symbol
                        score = self.minimax(board, True)
                        board[row][col] = 0
                        best_score = min(best_score, score)
            return best_score

    def check_winner(self, board):
        """
        Verifica si hay un ganador en el tablero.
        
        Args:
            board (list of list): Representación del tablero como una matriz 3x3.
        
        Returns:
            str: El símbolo del ganador ('X', 'O') o None si no hay ganador.
        """
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != 0:
                return row[0]

        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
                return board[0][col]

        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
            return board[0][0]

        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
            return board[0][2]

        return None

    def is_draw(self, board):
        """
        Verifica si el tablero está lleno sin ganadores.
        
        Args:
            board (list of list): Representación del tablero como una matriz 3x3.
        
        Returns:
            bool: True si es empate, False en caso contrario.
        """
        for row in board:
            if 0 in row:
                return False
        return True

