# 입력
dice1, dice2, dice3 = map(int, input().split())
# print(dice1, dice2, dice3)

if dice1 == dice2 == dice3:
    print(10000 + (dice1 or dice2 or dice3) * 1000)

elif dice1 == dice2 or dice1 == dice3 or dice2 == dice3:
    if dice1 == dice2:
        print(1000 + (dice1) * 100)
    elif dice1 == dice3:
        print(1000 + (dice3) * 100)
    elif dice2 == dice3:
        print(1000 + (dice2) * 100)

elif (dice1 != dice2) and (dice1 != dice3) and (dice2 != dice3):
    max_dice = max(dice1, dice2, dice3)
    print(max_dice * 100)
    