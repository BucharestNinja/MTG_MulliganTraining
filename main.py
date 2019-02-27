import random
import numpy
import sys
deck=[]
already=[]
loop=1
maxHand=7
Yourhand=0;

def draw():#手札をデッキから引く
    shuffle=numpy.random.randint(0,i)#リスト内からランダムにカードの番号を選ぶ
    if shuffle not in already:#既に一度出てきたカードの番号でないかを確認する
     print(deck[shuffle])
     already.append(shuffle)#一度出てきたカードでないならその番号をリストに入れる
    else:
      draw()#一度出てきたカードならもう一度draw()の最初に戻ってカードを選び直す

def start():
 global maxHand
 global Yourhand
 while Yourhand<maxHand:
     draw()
     Yourhand+=1
 print("keep or mulligan")
 print("\nPress k or m")
 KorM=input()
 if KorM=="k":
     sys.exit()
 elif KorM=="m":
     if maxHand==0:
         sys.exit()
     else:
         maxHand-=1
         Yourhand=0
         print(maxHand)
         start()

data =open('deck.txt',"r") #デッキのデータを読み込む
for cardList in data:
  num,*card=cardList.split(" ",1)#カードの枚数とカードの名前を分ける
  stripNum=num.rstrip()
  #print(stripNum)
  while loop<=int(stripNum):
       deck.extend([*card]) #デッキリストのカードを先頭から一行ずつ読み込む
       loop+=1
  loop=1
  #print(*card)
i=len(deck)
#print(i)

start()
