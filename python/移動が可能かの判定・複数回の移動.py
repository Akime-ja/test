"""マップの行数 H と列数 W , 現在の座標 sy , sx , 移動の回数 N が与えられます。
続けて、障害物を '#' で、移動可能な場所を '.' で表した H 行 W 列 のマップ S_1 ... S_H と N 回の移動の向き d_1 ... d_N が与えられます。

移動者ははじめ北を向いています。移動者は、1 回の移動で次の行動を行います。

「移動の向きに方向転換したのち、1 マス進む。」

各移動が可能である場合、移動後の y , x 座標を出力してください。
移動が可能でない場合、移動後の座標を出力する代わりに "Stop" を出力して、以降の移動を打ち切ってください。

各移動が可能であるということは、以下の図の通り
「移動先が障害物でない　かつ　移動先がマップの範囲外でない」
ということを意味します。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。"""



Row,Col,Y,X,N=map(int,input().split())
Board = [list(input()) for _ in range(Row)]
DirState=0 #向いている方向:北=0、東=1、南=2、西=3
for i in range(N):
    MoveDir=input()
    if MoveDir=="R":
        State=1 
    elif MoveDir=="L":
        State=-1
    if DirState%4==0:
        X+=State
        if X<0 or X>Col-1 or Board[Y][X]=="#":
            print("Stop")
            break
    elif DirState%4==2:
        X-=State
        if X<0 or X>Col-1 or Board[Y][X]=="#":
            print("Stop")
            break
    elif DirState%4==3:
        Y-=State
        if Y<0 or Y>Row-1 or Board[Y][X]=="#":
            print("Stop")
            break
    elif DirState%4==1:
        Y+=State
        if Y<0 or Y>Row-1 or Board[Y][X]=="#":
            print("Stop")
            break
    print(Y,X)
    DirState+=State