class Waribashi:
    player_1, player_2 = [1, 1], [1, 1]
    turn = -1

    def show(self):
        if self.turn == 1:
            print(f"{self.player_2[1]} {self.player_2[0]}\n\n{self.player_1[0]} {self.player_1[1]}")
        else:
            print(f"{self.player_1[0]} {self.player_1[1]}\n\n{self.player_2[1]} {self.player_2[0]}")

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
        # plyer_2[enemy] += player_1[me]
        if self.turn == 1:
            self.player_2[enemy] += self.player_1[me]
        else:
            self.player_1[enemy] += self.player_2[me]

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