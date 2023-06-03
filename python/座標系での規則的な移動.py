"""開始時点の x , y 座標と移動の歩数 N が与えられます。
以下の図のように時計回りに渦を巻くように移動を N 歩行った後の x , y 座標 を答えてください。

なお、マスの座標系は下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。 """


X,Y,N=map(int,input().split())  #初期位置、移動回数入力
Board=[]  #通ったか判別する用の盤面
DirState=0  #向いている方向:北=0,東=1,南=2,西=3
Board.append([X,Y])
for i in range(N):
    if DirState%4==0: #北を向いているとき
        if [X+1,Y] in Board: #右隣移動済み
            Y-=1
            Board.append([X,Y])
        else:
            X+=1 
            DirState+=1
            Board.append([X,Y])
    elif DirState%4==1: #東を向いているとき
        if [X,Y+1] in Board:
            X+=1
            Board.append([X,Y])
        else:
            Y+=1 
            DirState+=1
            Board.append([X,Y])
    elif DirState%4==2: #南を向いているとき
        if [X-1,Y] in Board:
            Y+=1 
            Board.append([X,Y])
        else:
            X-=1 
            DirState+=1 
            Board.append([X,Y])
    elif DirState%4==3: #西を向いているとき
        if [X,Y-1] in Board:
            X-=1 
            Board.append([X,Y])
        else:
            Y-=1 
            DirState+=1 
            Board.append([X,Y])
print(X,Y)
        