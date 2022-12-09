class UI:
    right_1, left_1, right_2, left_2 = 1, 1, 1, 1
    turn = 1
    def show(self):
        if self.turn == 1:
            print(f"{right_2} {left_2}\n\n{left_1} {right_1}")
        else:
            print(f"{right_1} {left_1}\n\n{left_2} {right_2}")
show