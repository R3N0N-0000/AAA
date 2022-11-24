import random


cpu = random.randint(1,3)
while :
    player = int(input("1:グー、2:チョキ、3:パー"))

    if player == cpu:
        print("CPU : ",cpu)
        print("EVEN")
    elif (player == 1 and cpu == 2) or (player == 2 and cpu == 3) or (player == 3 and cpu == 1):
        print("CPU : ",cpu)
        print("WIN")
    elif (player == 1 and cpu == 3) or (player == 2 and cpu == 1) or (player == 3 and cpu == 2):
        print("CPU : ",cpu)
        print("LOSE")
    else:
        print("1~3の数字を入力してください。")