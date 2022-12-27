import random

num = 15

while num > 0:
    dice = random.randint(1, 6)
    num -= dice
    while True:
        question = input("サイコロを振りますか？ y/n\n")
        if question == "y":
            break_ = False
            break
        elif question == "n":
            break_ = True
            break
    if break_:
        break
    print("\nサイコロの目は", str(dice), "です")
    if num > 0:
        print("ゴールまであと", str(num),"\n")
    else:
        print("GOAL")