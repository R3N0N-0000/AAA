import random



player = []
cards = [...]

while :

    # カードを配る
    for _ in range(2):
        player.append(cards[random.randint(0,12)])

    while True:
        input("HIT or STAND")
        
        if # HITならカードを1枚配る
        else:
            break

    # CPU

    if player == cpu or (player > 21 and cpu > 21):
        print("EVEN")
    elif player == 21 and cpu != 21:
        print("BlackJack")
    elif player > cpu and player <= 21 and cpu <= 21 :
        print("WIN")
    else:
        print("LOSE")