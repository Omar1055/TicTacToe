import math


def choose_sign():
    while True:
        player_sign = input("Choose your sign (X or O): ").upper()
        if player_sign == 'X' or player_sign == 'O':
            return player_sign
        else:
            print("Invalid sign. Please choose 'X' or 'O'.")


class TicTacToe:
    def __init__(self):
        self.board = [None for _ in range(9)]

    def create_board(self):
        board_str = (f"|{self.board[0] or ' '}|{self.board[1] or ' '}|{self.board[2] or ' '}|\n"
                     f"|{self.board[3] or ' '}|{self.board[4] or ' '}|{self.board[5] or ' '}|\n"
                     f"|{self.board[6] or ' '}|{self.board[7] or ' '}|{self.board[8] or ' '}|")
        print(board_str)

    def player_move(self, player_sign):
        while True:
            try:
                move = int(input("Enter your move [1:9]: "))
                if move < 1 or move > 9:
                    print("Invalid move. Please enter a number between 1 and 9.")
                elif self.board[move - 1] is not None:
                    print("Invalid move. That position is already taken.")
                else:
                    self.board[move - 1] = player_sign
                    break
            except ValueError:
                print("Invalid move. Please enter a number.")

    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]

        for condition in win_conditions:
            a, b, c = condition
            if self.board[a] == self.board[b] == self.board[c] is not None:
                return True

        return False

    def check_tie(self):
        return all(cell is not None for cell in self.board)

    def comp_move(self, player_sign):
        comp_sign = 'X' if player_sign == 'O' else 'O'
        bestScore = -math.inf
        bestMove = None
        for i in range(9):
            if self.board[i] is None:
                self.board[i] = comp_sign
                score = self.minimax(0, False, player_sign, comp_sign)
                self.board[i] = None
                if score > bestScore:
                    bestScore = score
                    bestMove = i
        self.board[bestMove] = comp_sign

    def minimax(self, depth, isMaximizing, player_sign, comp_sign):
        if self.check_winner():
            if isMaximizing:
                return -1
            else:
                return 1
        elif self.check_tie():
            return 0

        if isMaximizing:
            bestScore = -math.inf
            for i in range(9):
                if self.board[i] is None:
                    self.board[i] = comp_sign
                    score = self.minimax(depth + 1, False, player_sign, comp_sign)
                    self.board[i] = None
                    bestScore = max(bestScore, score)
            return bestScore
        else:
            bestScore = math.inf
            for i in range(9):
                if self.board[i] is None:
                    self.board[i] = player_sign
                    score = self.minimax(depth + 1, True, player_sign, comp_sign)
                    self.board[i] = None
                    bestScore = min(bestScore, score)
            return bestScore


def main():
    game = TicTacToe()
    print("Welcome to Tic Tac Toe!")
    player_sign = choose_sign()
    print(f"You chose {player_sign}. Let's start the game!")
    game.create_board()

    while not game.check_winner() and not game.check_tie():
        game.player_move(player_sign)
        game.create_board()
        if game.check_winner() or game.check_tie():
            break
        print("----------------")
        print("Computer's turn:")
        game.comp_move(player_sign)  # Moved here
        game.create_board()

    if game.check_winner():
        print("Congratulations! You won!")
    elif game.check_tie():
        print("It's a tie!")


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
