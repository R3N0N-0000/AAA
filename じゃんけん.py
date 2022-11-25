import random

cpu = random.randint(1,3)

# 入力


# 勝敗判定
# 引き分け
if player == cpu:
    print("EVEN")
# 勝ち
elif (player == "1" and cpu == "2") or (player == "2" and cpu == "3") or (player == "3" and cpu == "1"):
    print("WIN")
# 負け
elif (player == "1" and cpu == "3") or (player == "2" and cpu == "1") or (player == "3" and cpu == "2"):
    print("LOSE")