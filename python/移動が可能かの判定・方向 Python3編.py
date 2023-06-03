Row,Col,Y,X,Dir,MoveDir=input().split()
Row=int(Row)
Col=int(Col)
Y=int(Y)
X=int(X)
Board = [list(input()) for _ in range(Row)]
if MoveDir=="R":
    State=1 
elif MoveDir=="L":
    State=-1
if Dir=="N":
    X+=State
    if X<0 or X>Col-1 or Board[Y][X]=="#":
        print("No")
    else:
        print("Yes")
elif Dir=="S":
    X-=State
    if X<0 or X>Col-1 or Board[Y][X]=="#":
        print("No")
    else:
        print("Yes")
elif Dir=="W":
    Y-=State
    if Y<0 or Y>Row-1 or Board[Y][X]=="#":
        print("No")
    else:
        print("Yes")
elif Dir=="E":
    Y+=State
    if Y<0 or Y>Row-1 or Board[Y][X]=="#":
        print("No")
    else:
        print("Yes")    