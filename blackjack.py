"""
hint：0到51裡面任意數字，除以13，商數為花色，餘數為點數
"""
import random
#換算並印出牌面花色
def printCard(color):
    for i in color:
        if i // 13 == 0:
            print(chr(9824), end = '') #列印黑桃
        elif i // 13 == 1:
            print(chr(9829), end = '') #列印紅心
        elif i // 13 == 2:
            print(chr(9830), end = '') #列印方塊
        else:
            print(chr(9827), end = '') #列印梅花
        
        if i % 13 == 0:
            print('A', end = ' ') #餘數為0，印A
        elif i % 13 == 10:
            print('J', end = ' ') #餘數為10，印J
        elif i % 13 == 11:
            print('Q', end = ' ') #餘數為11，印Q
        elif i % 13 == 12:
            print('K', end = ' ') #餘數為12，印K
        else:
            print(i % 13 + 1, end = ' ') #餘數要加一，才會剛好是點數
    print()
#把牌面資訊印出來    
def printMessage():
    print('玩家的牌：', end = '')
    printCard(playerCard)
    print('玩家的牌面點數：', sum(playerPoint))
    print('莊家的牌：', end = '')
    printCard(bankerCard)
    print('莊家的牌面點數：', sum(bankerPoint))
    print('*************************************')
#計算牌面點數  
def cardPoint(x): #回傳牌的點數
    if x % 13 == 0: #牌A，回傳點數11
        return 11
    elif x % 13 > 9: #牌J、Q、K，回傳點數10
        return 10
    else:
        return x % 13 + 1 #因為list從0開始，1代表兩點，直接回傳牌面點數
#發牌
def deal(gamerCard, gamerPoint):
    temp = card.pop()
    gamerCard.append(temp)
    gamerPoint.append(cardPoint(temp))

card = list(range(0, 52))
random.shuffle(card) #用shuffle函式洗亂

playerCard = list()
playerPoint = list()
bankerCard = list()
bankerPoint = list()

#以下開始發牌流程，上面都是在定義函式而已
for i in range(2): #玩家要發兩張牌
    deal(playerCard, playerPoint)

deal(bankerCard, bankerPoint) #莊家發牌

printMessage()

while True:
    ans = input('玩家要加牌嗎？（Y/N）：')
    if ans == 'N' or ans == 'n':
        break
    deal(playerCard, playerPoint)
    if sum(playerPoint) > 21:
        if 11 in playerPoint:
            playerPoint[playerPoint.index(11)] = 1
            printMessage()
        else:
            printMessage()
            print('玩家爆牌，莊家獲勝')
            break
    else:
        printMessage()
if sum(playerPoint) < 22:
    while sum(bankerPoint) < 17:
        deal(bankerCard, bankerPoint)
        if sum(bankerPoint) > 21:
            if 11 in bankerPoint:
                bankerPoint[bankerpoint.index(11)] = 1
        printMessage()
    if sum(bankerPoint) > 21:
        print('莊家爆牌，玩家勝利')
    elif sum(bankerPoint) > sum(playerPoint):
        print('莊家勝利')
    elif sum (bankerPoint) < sum(playerPoint):
        print('玩家勝利')
    elif sum(bankerPoint) == sum(playerPoint):
        print('和局')
