import random


cpu = random.randint(1,3)
player = int(input("グー：１、チョキ：２、パー：３　あなたが出す手は？"))


if player == cpu:
    print("あいこです。")
elif player == 1 and cpu == 2:
    print("相手はチョキを出しました。あなたの勝ちです。")
elif player == 1 and cpu == 3:
    print("相手はパーを出しました。あなたの負けです。")
elif player == 2 and cpu == 3:
    print("相手はパーを出しました。あなたの勝ちです。")
elif player == 2 and cpu == 1:
    print("相手はグーを出しました。あなたの負けです。")
elif player == 3 and cpu == 1:
    print("相手はグーを出しました。あなたの勝ちです。")
elif player == 3 and cpu == 2:
    print("相手はチョキを出しました。あなたの負けです。")
else:
    print("1~3の数字を入力してください。")