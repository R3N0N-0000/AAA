import random

cpu = random.randint(0, 2)


while True:
    player = input("1:グー　2:チョキ　3:パー\n")
    if player in ("1", "2", "3"):
        player = int(player)-1
        break

hand = ["グー", "チョキ", "パー"]

print("You :", hand[player])
print("CPU :", hand[cpu])

if player == cpu:
    print("EVEN")
elif hand[player - 2] == hand[cpu]:
    print("WIN")
else:
    print("LOSE")