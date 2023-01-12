import random
import re

class Sugoroku:
    players = []
    goal_players = []
    positions = dict()
    size = 0

    def input_size(self):
        while True:
            size = input("Sugoroku size: ").strip()
            result = re.match(r"^[0-9]+$", size)
            if result:
                self.size = int(size)
            if self.size <= 0:
                print("正の整数を入力してください")
            else:
                break
        print(f"size = {self.size}")

    def input_players(self):
        while True:
            player = input("player's name: ").strip()
            if not player:
                break
            self.players.append(player)
            self.positions[player] = 0
        print(self.players)
        print(self.positions)

    def display(self):
        sep = "-" * self.size
        print(sep)
        for player in self.players:
            position = self.positions[player]
            space = " " * position
            c = player[0].upper()
            print(f"{space}{c}")
        print(sep)

    def play(self):
        while True:
            for n, player in enumerate(self.players):
                input(player + " ")
                steps = random.randint(1, 6)
                input(f"{steps} steps ")
                pos = self.positions[player]
                next_pos = pos + steps
                next_pos = min(next_pos, self.size)
                input(f"{pos} -> {next_pos} ")
                self.positions[player] = next_pos
                self.display()
                if next_pos == self.size:
                    self.goal_players.append(self.players.pop(n))
                    if len(self.players) == 0 and len(self.goal_players) == 1:
                        print("GOAL")
                        return
                    else:
                        print(f"{player} GOAL\n")
                    if len(self.players) == 1:
                        return
    

def main():
    sugoroku = Sugoroku()
    sugoroku.input_size()
    sugoroku.input_players()
    sugoroku.display()
    sugoroku.play()

if __name__ == "__main__":
    main()