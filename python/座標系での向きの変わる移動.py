"""開始時点の x , y 座標、移動の回数 N が与えられます。
続くN行で移動の向き d1 ... dN が与えられるので、与えられた順に移動をしたときの各移動後の x , y 座標 を答えてください。
移動者ははじめ北を向いています。

なお、マスの座標系は下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

・ 移動をするごとに向く方角が変わること
・ 移動前に向いている方角によって同じ移動の向きでも座標の変化が違うこと
の 2 点に気をつけてください。"""

X,Y,MoveTimes=map(int,input().split()) #初期位置、移動回数入力
DirState=0 #向いている方向:北=0、東=1、南=2、西=3
for i in range(MoveTimes):
    dx=input()
    if dx=="R":
        State=1 
    elif dx=="L":
        State=-1
    if DirState%4==0: #北
        X+=State
    elif DirState%4==1: #東
        Y+=State
    elif DirState%4==2: #南
        X-=State
    elif DirState%4==3: #西
        Y-=State
    DirState+=State
    print(X,Y) 