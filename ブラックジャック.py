while :

    # カードを配る

    while STANDを選ぶまで:
        input("HIT or STAND")
        
        if # HITならカードを1枚配る

    # CPU

    if player == cpu or (player > 21 and cpu > 21):
        print("EVEN")
    elif player == 21 and cpu != 21:
        print("BlackJack")
    elif player > cpu and player <= 21 and cpu <= 21 :
        print("WIN")
    else:
        print("LOSE")