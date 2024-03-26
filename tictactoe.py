class TicTacToe:
    def __init__(self):
        self.board = [None for _ in range(9)]

    def create_board(self):
        board_str = (f"|{self.board[0] or ' '}|{self.board[1] or ' '}|{self.board[2] or ' '}|\n"
                     f"|{self.board[3] or ' '}|{self.board[4] or ' '}|{self.board[5] or ' '}|\n"
                     f"|{self.board[6] or ' '}|{self.board[7] or ' '}|{self.board[8] or ' '}|")
        print(board_str)

    @property
    def choose_sign(self):
        while True:
            player_sign = input("Choose your sign (X or O): ").upper()
            if player_sign == 'X' or player_sign == 'O':
                return player_sign
            else:
                print("Invalid sign. Please choose 'X' or 'O'.")

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

    def play_game(self):
        print("Welcome to Tic Tac Toe!")
        player_sign = self.choose_sign
        opponent_sign = 'X' if player_sign == 'O' else 'O'

        print(f"Player 1: {player_sign}\nPlayer 2: {opponent_sign}\n")

        while True:
            self.create_board()
            self.player_move(player_sign)
            if self.check_winner():
                self.create_board()
                print("Congratulations! You win!")
                break
            elif self.check_tie():
                self.create_board()
                print("It's a tie!")
                break

            self.create_board()
            self.player_move(opponent_sign)
            if self.check_winner():
                self.create_board()
                print("You lose!")
                break
            elif self.check_tie():
                self.create_board()
                print("It's a tie!")
                break


# Create an instance of the TicTacToe class
game = TicTacToe()

# Start the game
game.play_game()
