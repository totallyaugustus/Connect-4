def s(a,b,c,d,e):
    if a[b][c]==d:
        if c>=(8-e):
            if b>=(7-e):
                f0=0
                if f0==e:
                    return d
            else:
                f3=0
                f4=0
                for q in range(0,e):
                    if a[b][c]==a[b+q][c]:
                        f3=f3+1
                    if a[b][c]==a[b+q][c-q]:
                        f4=f4+1
                if f3==e or f4==e:
                    return d
        elif c<=(6-e):
            if b>=(7-e):
                f1=0
                for q in range(0,e):
                    if a[b][c]==a[b][c+q]:
                        f1=f1+1
                if f1==e:
                    return d
            else:
                f1=0
                f2=0
                f3=0
                for q in range(0,e):
                    if a[b][c]==a[b][c+q]:
                        f1=f1+1
                    if a[b][c]==a[b+q][c+q]:
                        f2=f2+1
                    if a[b][c]==a[b+q][c]:
                        f3=f3+1
                if f1==e or f2==e or f3==e:
                    return d
        else:
            if b>=(7-e):
                f1=0
                for q in range(0,e):
                    if a[b][c]==a[b][c+q]:
                        f1=f1+1
                if f1==e:
                    return d
            else:
                f1=0
                f2=0
                f3=0
                f4=0
                for q in range(0,e):
                    if a[b][c]==a[b][c+q]:
                        f1=f1+1
                    if a[b][c]==a[b+q][c+q]:
                        f2=f2+1
                    if a[b][c]==a[b+q][c]:
                        f3=f3+1
                    if a[b][c]==a[b+q][c-q]:
                        f4=f4+1
                if f1==e or f2==e or f3==e or f4==e:
                    return d
alist=[[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],["1","2","3","4","5","6","7"]]
for q in range(7):
    for w in range(7):
        if w==6:
            print(alist[q][w])
        else:
            print(alist[q][w],end=" ")
g=int(input("0=One Win, 1=Most Wins"))
l=int(input("Connect Amount?"))
xw=0
ow=0
turn=0
while turn<42:
    if turn%2==0:
        i=int(input("X"))
    else:
        i=int(input("O"))
    i=i-1
    for q in range(5,-1,-1):
        if q==0:
            if alist[q][i]!=" ":
                print("invalid")
                turn=turn-1
            else:
                if turn%2==0:
                    alist[q][i]="X"
                else:
                    alist[q][i]="O"
        else:
            if alist[q][i]==" ":
                if turn%2==0:
                    alist[q][i]="X"
                else:
                    alist[q][i]="O"
                break
    for q in range(0,6):
        for w in range(0,7):
            if turn%2==0:
                if s(alist,q,w,"X",l)=="X":
                    if g==0:
                        print("Player X Wins!")
                        turn=turn+100
                    else:
                        xw=xw+1
            else:
                if s(alist,q,w,"O",l)=="O":
                    if g==0:
                        print("Player O Wins!")
                        turn=turn+100
                    else:
                        ow=ow+1
    turn=turn+1
    if turn<100:
        print(turn)
    else:
        print(turn-100)
    for q in range(7):
        for w in range(7):
            if w==6:
                print(alist[q][w])
            else:
                print(alist[q][w],end=" ")
if g==1:
    if xw>ow:
        print("Player X Wins "+str(xw)+"-"+str(ow))
    elif ow>xw:
        print("Player O Wins "+str(ow)+"-"+str(xw))
    else:
        print("Tie "+str(xw)+"-"+str(ow))
