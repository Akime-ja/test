"""マップの行数 H と列数 W , 障害物を '#' で移動可能な場所を '.' で表した H 行 W 列のマップ S_1 ... S_H , 現在の座標 sy, sx, 移動の回数 N が与えられます。
続けて、 N 回の移動の向き d_1 ... d_N と移動するマス数 l_1 ... l_N が与えられます。

プレイヤーははじめ北を向いています。

各移動が可能である場合、移動後の y , x 座標 を出力してください。
移動が可能でない場合(移動しきれない場合)、移動できるところまで移動した後の座標を出力した後に "Stop" を出力して、以降の移動を打ち切ってください。

各移動が可能であるということは、以下の図の通り
「今いるマスから移動先のマスまでに障害物がない　かつ　移動先がマップの範囲外でない」
ということを意味します。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。"""

Row,Col,Y,X,N=map(int,input().split())
Board = [list(input()) for _ in range(Row)]
DirState=0 #向いている方向:北=0、東=1、南=2、西=3
State=0 #右回り=1,左回り=-1,エラー=2
for i in range(N):
    MoveDir,MoveDis=input().split()
    MoveDis=int(MoveDis)
    if MoveDir=="R":
        State=1 
    elif MoveDir=="L":
        State=-1
    for j in range(MoveDis):
        if DirState%4==0:
            X+=State
            if X<0 or X>Col-1 or Board[Y][X]=="#":
                X-=State
                State=2
                break
        elif DirState%4==2:
            X-=State
            if X<0 or X>Col-1 or Board[Y][X]=="#":
                X+=State
                State=2
                break
        elif DirState%4==3:
            Y-=State
            if Y<0 or Y>Row-1 or Board[Y][X]=="#":
                Y+=State
                State=2
                break
        elif DirState%4==1:
            Y+=State
            if Y<0 or Y>Row-1 or Board[Y][X]=="#":
                Y-=State
                State=2
                break
    if State==2:
        print(Y,X)
        print("Stop")
        break
    else:
        print(Y,X)
        DirState+=State