import random
import re

class Sugoroku:
    players = []
    positions = dict()
    size = 0

    def input_size(self):
        while True:
            size = input("Sugoroku size: ")
            size = size.strip()
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
            player = input("player's name: ")
            player = player.strip()
            if not player:
                break
            self.players.append(player)
            self.positions[player[0].upper()] = 0
            # TODO
            # 頭文字が同じ名前は入れないようにする
        print(self.players)
        print(self.positions)

    def play(self):
        ...

    def display(self):
        for player in self.players:
            p = player[0].upper()
            position = self.positions[p]
            space = " " * position
            print(f"{space}{p}")
        print("-" * self.size)




def main():
    sugoroku = Sugoroku()
    sugoroku.input_size()
    sugoroku.input_players()
    sugoroku.display()
    sugoroku.positions["R"] = 2
    sugoroku.display()
    sugoroku.positions["K"] = 1
    sugoroku.display()

if __name__ == "__main__":
    main()