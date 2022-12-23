class Waribashi:
    hands = ["", [1, 1], [1, 1]]

    turn = 1

    def show(self):
        for j in (-1, 1):
            for i in range(2):
                print(self.hands[self.turn*j][i], end = " ")
            print()

    def input_(self):
        while True:
            my_num = input(f"My : {self.hands[self.turn][0]} or {self.hands[self.turn][1]}\n")
            if my_num in str(self.hands[self.turn]):
                break
        while True:
            enemy_num = input(f"Enemy : {self.hands[self.turn*-1][0]} or {self.hands[self.turn*-1][1]}\n")
            if enemy_num in str(self.hands[self.turn*-1]):
                break
        for i in range(2):
            if self.hands[self.turn*-1][i] == int(enemy_num):
                enemy_hand = i
                return int(my_num), enemy_hand

    def attack(self, my_num, enemy_hand):
        self.hands[self.turn*-1][enemy_hand] += my_num
        if  self.hands[self.turn*-1][enemy_hand] >= 5:
            self.hands[self.turn*-1][enemy_hand] -= 5

    def trial(self):
        ...


waribashi = Waribashi()
waribashi.show()
my_num, enemy_hand = waribashi.input_()
waribashi.attack(my_num, enemy_hand)