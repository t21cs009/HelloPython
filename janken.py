'''
Created on 2023/10/13

@author: t21cs009
'''
#3回勝負で勝敗を決めるように修正した
import random

hands = ["グー", "チョキ", "パー"]

acount = 0
bcount = 0

while(acount < 3 and bcount < 3):
    a = random.randrange(9)%3
    b = random.randrange(9)%3
    if((a == 2 and b == 0) or (a < b and b - a == 1)):
        game = "Aの勝ち"
        acount += 1
    elif((b == 2 and a == 0) or (a > b and a - b == 1)):
        game = "Bの勝ち"
        bcount += 1
    elif(a == b):
        game = "引き分け"
    print("Aの手 : " + hands[a] + " v.s. Bの手 : " + hands[b] + " -> " + game)