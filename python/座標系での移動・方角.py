"""開始時点の y , x 座標 と移動の回数 N が与えられます。
続く N 行で移動の方角 d_1 ... d_N が与えられるので、与えられた順に移動をしたときの各移動後の y , x 座標 を答えてください。

ただし、図の通り、上側（ y 軸の負の向き）を北とします。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。"""




Y,X,MoveTimes=map(int,input().split())#初期位置、移動回数入力
MoveDir=[]
for i in range(MoveTimes):#移動方向入力
    MoveDir.append(input())
    if MoveDir[i]=="N":
        Y-=1 
    elif MoveDir[i]=="S":
        Y+=1 
    elif MoveDir[i]=="W":
        X-=1 
    elif MoveDir[i]=="E":
        X+=1 
    print(Y,X)