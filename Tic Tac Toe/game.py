class TicTacToeBoard:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for j in range(3)]

    def display(self):
        for row in self.board:
            print("|".join(row))
            print("---")
    
class TicTacToeGame:
    def __init__(self,player1,player2):
        self.players = [player1,player2]
        self.board = TicTacToeBoard()
        self.currplayer = player1
    
    def switch_player(self):
        self.currplayer = self.players[1] if self.currplayer == self.players[0] else self.players[0]

    def check_winner(self,marker):
        for i in range(3):
            if any(all(self.board.board[i][j]==marker) for j in range(3)) or any(all(self.board.board[j][i]==marker) for j in range(3)) or all(self.boeard.board[i][i]==marker) or all(self.board.board[i][2-i] == marker):
                return True
        else:
            return False
    
    def check_draw(self):
        return all(self.board.board[i][j]!=" " for i in range(3) for j in range(3))

class Audi:
    def __init__(self,name,city):
        self.name = name
        self.city = city

class CinemalHall:
    def __init__(self):
        self.audis = [Audi]

    