#マップの行数 H と列数 W とマップを表す H 行 W 列の文字列 S_1 ... S_H が与えられるので、
#上下のマスがどちらも '#' であるようなマスの y , x 座標 を答えてください。

#ただし、上端のマスの場合は「下のマスが '#'」であれば、下端のマスの場合は「上のマスが '#'」であれば条件を満たすものとします。

#なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
#下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

Row,Col=map(int,input().split())#行と列の数値を格納
Board = [list(input()) for _ in range(Row)]#盤面の状態を格納
for i in range(Row):
    
    for j in range(Col):
        if i==0:#下隣判別
            if Board[i+1][j]=="#":
                print(i,j)
            
        elif i==Row-1:#上隣判別
            if Board[i-1][j]=="#":
                print(i,j)
        else:#上下判別
            if Board[i+1][j]=="#" and Board[i-1][j]=="#":
                print(i,j)