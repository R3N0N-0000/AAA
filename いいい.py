import random



# 乱数2つ
player = random.randint(1, 6)
cpu = random.randint(1, 6)
print("You :", player)


# 予想させる
predict = input("higher or lower than CPU")


# 点数をつける
score = 0
print("cpu :",cpu)
if (predict == "higher" and player > cpu) or (predict == "lower" and player < cpu):
    score += 1


# 指定回数で終わらせる  