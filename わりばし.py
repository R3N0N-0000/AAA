class Waribashi:
    hands = ["", [1, 1], [1, 1]]
    turn = -1

    def show(self):
        if self.turn == 1:
            print("\nPlayer1's turn\n")
        else:
            print("\nPlayer2's turn\n")

        for i in (0, 1):
            if self.hands[self.turn*-1][i]:
                print(self.hands[self.turn*-1][i], end = " ")
            else:
                print(end = "  ")
        print()
        for i in (1, 0):
            if self.hands[self.turn][i]:
                print(self.hands[self.turn][i], end = " ")
            else:
                print(end = "  ")
        print()

    def input_(self):
        print()
        break_ = False
        while True:
            for i in range(2):
                if not self.hands[self.turn][i]:
                    my_num = self.hands[self.turn][not i]
                    break_ = True
                    break
            if break_:
                break
                         
            my_num = input(f"My : {self.hands[self.turn][0]} or {self.hands[self.turn][1]}\n")
            if my_num in str(self.hands[self.turn]):
                break
        
        while True:
            breal_ = False
            for i in range(2):
                if not self.hands[self.turn*-1][i]:
                    enemy_hand = self.hands[self.turn*-1][not i]
                    break_ = True
                    break
            if break_:
                break

            enemy_num = input(f"Enemy : {self.hands[self.turn*-1][0]} or {self.hands[self.turn*-1][1]}\n")
            if enemy_num in str(self.hands[self.turn*-1]):
                break
                return int(my_num), enemy_hand

    def attack(self, my_num, enemy_hand):
        self.hands[self.turn*-1][enemy_hand] += my_num
        if  self.hands[self.turn*-1][enemy_hand] >= 5:
            self.hands[self.turn*-1][enemy_hand] -= 5

    def trial(self):
        if self.hands[self.turn*-1][0] == 0 and self.hands[self.turn*-1][1] == 0:
            if self.turn == 1:
                print("player_1  WIN")
            elif self.turn == -1:
                print("prayer_2  WIN")
            return False
        return True



waribashi = Waribashi()
while waribashi.trial():
    waribashi.turn *= -1
    waribashi.show()
    my_num, enemy_hand = waribashi.input_()
    waribashi.attack(my_num, enemy_hand)