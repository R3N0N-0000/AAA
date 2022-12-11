class Waribashi:
    right_1, left_1, right_2, left_2 = 1, 1, 1, 1
    turn = 1
    def show(self):
        if self.turn == 1:
            print(f"{self.right_2} {self.left_2}\n\n{self.left_1} {self.right_1}")
        else:
            print(f"{self.right_1} {self.left_1}\n\n{self.left_2} {self.right_2}")

    def input_(self):
        x = input("right or left")
        if x in ("right"):

        elif x in ("left"):
            
        else:
            print("rigth か left で入力してください")
    def attack(self):
        

waribashi = Waribashi()

waribashi.show()
