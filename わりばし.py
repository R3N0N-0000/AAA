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
            n = input(f"My {self.hands[self.turn][0]} or {self.hands[self.turn][1]}\n")
            if n in str(self.hands[self.turn]):
                break
        while True:
            enemy = input(f"Enemy {self.hands[self.turn*-1][0]} or {self.hands[self.turn*-1][1]}\n")
            if enemy in str(self.hands[self.turn*-1]):
                break

    def attack(self, me, enemy):
        ...

    def trial(self):
        ...


waribashi = Waribashi()
waribashi.show()
waribashi.input_()