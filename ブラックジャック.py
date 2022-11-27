import random



player = []
cards = [[1,1,1,1][2,2,2,2][...]]

while :

    # カードを配る
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