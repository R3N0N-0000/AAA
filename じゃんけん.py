import random

cpu = str(random.randint(1,3))

# 入力
while True:
    player = input("1:グー　2:チョキ　3:パー")
    if player in ("1","2","3"):
        break

print("You :",player)
print("CPU :",cpu)

# 勝敗判定
# 引き分け
if player == cpu:
    print("EVEN")
# 勝ち
elif (player == "1" and cpu == "2") or (player == "2" and cpu == "3") or (player == "3" and cpu == "1"):
    print("WIN")
# 負け
else:
    print("LOSE")