"""マップの行数 H と列数 W , 障害物を '#' で移動可能な場所を '.' で表した H 行 W 列のマップ S_1 ... S_H , 現在の座標 sy , sx , 移動の回数 N が与えられます。
続けて N 回の移動の向き d_1 ... d_N と移動するマス数 l_1...l_N が与えられます。

はじめは北を向いています。

各移動が可能である場合、スタート位置を含む移動の際に通ったマップのマスを '*' に変更してください。
移動が可能でない場合、障害物やマップの端までできる限り移動をして通ったマップのマスを '*' に変更したのち、以降の移動を打ち切ってください。

移動が終了した時のマップを出力してください。

移動可能であるということは、以下の図の通り
「今いるマスから移動先のマスまでに障害物がない かつ 移動先がマップの範囲外でない」
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
        Board[Y][X]="*"
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
        break
    else:
        DirState+=State
    
Board[Y][X]="*"
for s in Board: #盤面の表示
    print("".join(s))