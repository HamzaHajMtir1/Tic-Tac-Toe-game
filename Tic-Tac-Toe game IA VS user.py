"""A tic-tac-toe game  IA VS user"""
import tkinter as tk
import random


class TicTacToe:

    def __init__(self):
        self.board = [""] * 9
        self.player = "X"
        self.ai = "O"

    def play_move(self, index, player):
        if self.board[index] == "":
            self.board[index] = player
            return True
        else:
            return False

    def check_win(self, player):
        for i in range(3):
            if (self.board[i*3] == self.board[i*3+1] == self.board[i*3+2] == player or
                self.board[i] == self.board[i+3] == self.board[i+6] == player):
                return True
        if (self.board[0] == self.board[4] == self.board[8] == player or
            self.board[2] == self.board[4] == self.board[6] == player):
            return True
        return False

    def minimax(self, player):
        if self.check_win(self.ai):
            return 1
        elif self.check_win(self.player):
            return -1
        elif "" not in self.board:
            return 0

        scores = []
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = player
                score = self.minimax(self.player if player == self.ai else self.ai)
                self.board[i] = ""
                scores.append(score)

        if player == self.ai:
            return max(scores)
        else:
            return min(scores)

    def ai_move_minimax(self):
        scores = []
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = self.ai
                score = self.minimax(self.player)
                self.board[i] = ""
                scores.append(score)
            else:
                scores.append(-2)
        max_score_index = scores.index(max(scores))
        self.play_move(max_score_index, self.ai)


class TicTacToeGUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.buttons = []
        self.game_running = False
        self.game = TicTacToe()

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text="", font=("Helvetica", 20), width=5, height=2,
                                    command=lambda index=i*3+j: self.on_click(index))
                button.grid(row=i, column=j)
                self.buttons.append(button)

        self.status_label = tk.Label(self.window, text="", font=("Helvetica", 16))
        self.status_label.grid(row=3, column=0, columnspan=3)

        self.restart_button = tk.Button(self.window, text="Restart Game", font=("Helvetica", 16),
                                        command=self.restart_game)
        self.restart_button.grid(row=4, column=0, columnspan=3)

        self.game_running = True

    def on_click(self, index):
        if self.game_running:
            if self.game.play_move(index, self.game.player):
                self.update_board()
                if self.game.check_win(self.game.player):
                    self.end_game("You win!")
                elif "" not in self.game.board:
                    self.end_game("Tie game")
                else:
                    self.game.ai_move_minimax()
                    self.update_board()
                    if self.game.check_win(self.game.ai):
                        self.end_game("AI wins!")

    def update_board(self):
        for i in range(9):
            self.buttons[i]["text"] = self.game.board[i]

    def end_game(self, message):
        self.game_running = False
        self.status_label["text"] = message

    def restart_game(self):
        self.game_running = True
        self.game = TicTacToe()
        self.status_label["text"] = ""
        for i in range(9):
            self.buttons[i]["text"] = ""

    def start(self):
        self.window.mainloop()


if __name__ == "__main__":
    gui = TicTacToeGUI()
    gui.start()
