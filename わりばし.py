class Waribashi:
    player_1, player_2 = [1, 1], [1, 1]
    turn = -1

    def show(self):
        if self.turn == 1:
            print(f"{self.player_2[1]} {self.player_2[0]}\n\n{self.player_1[0]} {self.player_1[1]}")
        else:
            print(f"{self.player_1[1]} {self.player_1[0]}\n\n{self.player_2[0]} {self.player_2[1]}")

    def input_(self):
        while True:
            me = input("My R or L\n")
            if me in ("R", "r"):
                me = 1
                break
            elif me in ("L", "l"):
                me = 0
                break
                
        while True:
            enemy = input("Enemy R or L\n")
            if enemy in ("R", "r"):
                enemy = 1
                break
            elif enemy in ("L", "l"):
                enemy = 0
                break

        return me, enemy

    def attack(self, me, enemy):
        if self.turn == 1:
            self.player_2[enemy] += self.player_1[me]
            if self.player_2[enemy] >= 5:
                self.player_2[enemy] -= 5 # -= 5
                if 0 in self.player_2:
                    self.player_2.remove(0)
        else:
            self.player_1[enemy] += self.player_2[me]
            if self.player_1[enemy] >= 5:
                self.player_1[enemy] -= 5
                if 0 in self.player_1:
                    self.player_1.remove(0)

    def trial(self):
        if self.player_1 == [5, 5]:
            return 2
        elif self.player_2 == [5, 5]:
            return 1


waribashi = Waribashi()
while not waribashi.trial():
    waribashi.turn *= -1
    waribashi.show()
    me, enemy = waribashi.input_()
    waribashi.attack(me, enemy)
    
print(f"Player{waribashi.trial()} Win!")