from rich.table import Table
from rich.console import Console
from rich.text import Text
import json

class Board():
    def __init__(self):
        self.console=Console()

    def display_board(self):
        table = Table(show_header=False,show_lines=True)
        board=get_board()
        for rows in board["board"]:
            row=[]
            for cell in rows:
                if board["current_player"]%2:
                    row.append(Text(f" {cell} ",style="bold green" if cell=="X" else None))
                else:
                    row.append(Text(f" {cell} ",style="bold green" if cell=="O" else None))
            table.add_row(*row)
        self.console.print(table)

    def update_board(self,row,col):
        board=get_board()
        if row<0 or row>2 or col<0 or col>2:
            msg=Text("Invalid cell",style="bold red")
            self.console.print(msg)
            return None
        
        if board["board"][row][col]==" ":
            board["board"][row][col]=("X" if board["current_player"]%2 else "O")
            board["current_player"]=1-board["current_player"]
            set_board(board)
        else:
            msg=Text("Cell already filled",style="bold red")
            self.console.print(msg)

        board_cells=board["board"]
        if board_cells[0][0]==board_cells[0][1]==board_cells[0][2]!=" " or \
            board_cells[1][0]==board_cells[1][1]==board_cells[1][2]!=" " or \
            board_cells[2][0]==board_cells[2][1]==board_cells[2][2]!=" " or \
            board_cells[0][0]==board_cells[1][0]==board_cells[2][0]!=" " or \
            board_cells[0][1]==board_cells[1][1]==board_cells[2][1]!=" " or \
            board_cells[0][2]==board_cells[1][2]==board_cells[2][2]!=" " or \
            board_cells[0][0]==board_cells[1][1]==board_cells[2][2]!=" " or \
            board_cells[0][2]==board_cells[1][1]==board_cells[2][0]!=" ":
            msg=Text(f"Player {board['current_player']+1} won",style="bold green")
            self.console.print(msg)
            self.reset_board()
        else:
            self.console.print(Text(f"Player {3-(board['current_player']+1)} turn",style="bold green"))

    def reset_board(self):
        board={"board":[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],"current_player":0}
        set_board(board)
        self.current_player=0

def get_board():
    with open("board.json","r") as f:
        return json.load(f)
    
def set_board(board):
    with open("board.json","w") as f:
        json.dump(board,f,indent=4)