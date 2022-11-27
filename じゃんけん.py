import random

cpu = str(random.randint(1,3))


while True:
    player = input("1:グー　2:チョキ　3:パー")
    if player in ("1","2","3"):
        break

hand = ["グー","チョキ","パー"]

print("You :",hand[int(player)-1])
print("CPU :", hand[int(cpu)-1])


if player == cpu:
    print("EVEN")
elif (player == "1" and cpu == "2") or (player == "2" and cpu == "3") or (player == "3" and cpu == "1"):
    print("WIN")
else:
    print("LOSE")