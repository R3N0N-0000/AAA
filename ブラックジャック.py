import random



player = []
cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]



#while :

    # カードを配る
for _ in range(2):
    player.append(cards[random.randint(0,12)])
print()
'''
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
'''