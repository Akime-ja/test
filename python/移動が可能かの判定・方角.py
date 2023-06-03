"""マップの行数 H と列数 W , 障害物を '#' で、移動可能な場所を '.' で表した H 行 W 列のマップ S_1 ... S_H が与えられます。
続けて現在の座標 sy , sx ,１マス移動する方角 m が与えられるので、移動が可能かどうかを判定してください。

移動が可能であるということは、以下の図の通り
「移動先が障害物でない　かつ　移動先がマップの範囲外でない」
ということを意味します。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。 """


Row,Col,Y,X,MoveDir=input().split()
Row=int(Row)
Col=int(Col)
Y=int(Y)
X=int(X)
Board = [list(input()) for _ in range(Row)]
if MoveDir=="N":
    if Y==0 or Board[Y-1][X]=="#":
        print("No")
    else:
        print("Yes")
elif MoveDir=="S":
    if Y==Row-1 or Board[Y+1][X]=="#":
        print("No")
    else:
        print("Yes")
elif MoveDir=="W":
    if X==0 or Board[Y][X-1]=="#":
        print("No")
    else:
        print("Yes")
elif MoveDir=="E":
    if X==Col-1 or Board[Y][X+1]=="#":
        print("No")
    else:
        print("Yes")