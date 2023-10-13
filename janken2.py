'''
Created on 2023/10/13

@author: t21cs009
'''
import random

hands = ["グー", "チョキ", "パー"]

count = 0

while(count < 1):
    a = random.randrange(9)%3
    b = random.randrange(9)%3
    c = random.randrange(9)%3
    if((a == 2 and b == 0 and c == 0) or ((a < b and b - a == 1) and (a < c and c - a == 1))):
        game = "Aの勝ち"
        count += 1
    elif((b == 2 and a == 0 and c == 0) or ((b < a and a - b == 1) and (b < c and c - b == 1))):
        game = "Bの勝ち"
        count += 1
    elif((c == 2 and a == 0 and b == 0) or ((c < a and a - c == 1) and (c < b and b - a == 1))):
        game = "Cの勝ち"
        count += 1
    elif(a == b and b == c):
        game = "引き分け"
    print("Aの手 : " + hands[a] + " v.s. Bの手 : " + hands[b] + " v.s. Cの手 : " + hands[c] + " -> " + game)