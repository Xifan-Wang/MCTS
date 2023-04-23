import numpy as np
class Board():
    def __init__(self, n_rows:int = 3, n_columns:int = 3, n_consectives = 3, player_zero_id = 0, player_one_id = 1):
        self.rows = n_rows
        self.cols = n_columns
        self.k = n_consectives
        self.state = np.empty(shape=(self.rows, self.cols))
        self.state[:] = np.nan
        self.p0 = player_zero_id
        self.p1 = player_one_id
    
    def __str__(self):
        return str(self.state)
    
    def select_stone(self, player):
        if player == self.p0:
            return 0
        elif player == self.p1:
            return 1
        else:
            raise ValueError(f"Error, there is no player: {player}")

    def check_winner_stone(self):
        n = self.state.shape[0]
        k = self.k
        for row in self.state:
            for i in range(n-k+1):
                window = row[i:i+k]
                if len(set(window)) == 1 and not np.isnan(window[0]):
                    return window[0]
        
        for col in self.state.T:
            for i in range(n-k+1):
                window = col[i:i+k]
                if len(set(window)) == 1 and not np.isnan(window[0]):
                    return window[0]
            
        for row_idx in range(n-k+1):
            for col_idx in range(n-k+1):
                window_2d = self.state[row_idx:row_idx+k, col_idx:col_idx+k]
                diag1 = np.diag(window_2d)
                diag2 = np.diag(np.fliplr(window_2d))
                if len(set(diag1)) == 1 and not np.isnan(diag1[0]):
                    return diag1[0]
                if len(set(diag2)) == 1 and not np.isnan(diag2[0]):
                    return diag2[0]
        return None
    
    def examine(self, winner_stone):
        if winner_stone is None:
            if not np.isnan(self.state).any():
                print("It'a tie!")
        else:
            if winner_stone == 0:
                print(f"{self.p0} has won!")
            else:
                print(f"{self.p1} has won!")
    
    def move(self, player, row_idx, col_idx):
        try:
            stone = self.select_stone(player)
        except ValueError as error:
            print(error)
        if not np.isnan(self.state[row_idx, col_idx]):
            print(f"Can't place a stone in the {row_idx, col_idx} position")
        else:
            stone = self.select_stone(player)
            self.state[row_idx][col_idx] = stone
            winner_stone = self.check_winner_stone()
            self.examine(winner_stone)
            print(str(self.state))

    
    
board = Board(player_zero_id="a", player_one_id="b")
print(board)
board.move("a", 1, 1)
board.move("a", 1, 1)
board.move("a", 2, 2)
