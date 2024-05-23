from Game import Game
g=Game()
p=1
s:bool
inpt=input("player 1 choose x or o :")
p1=inpt[0].upper()
p2="O" if p1=="X" else "X"
print("player 1 you: "+p1+" player 2 you: "+p2)
game_over=False
while True:
    while p==1:
        g.print_background()
        print("player 1")
        print("entre pos :")
        x=int(input("enter x :"))
        y=int(input("enter y :"))
        s=g.play(x,y,p1)
        if s: p=2
        else: print("pos taken choose again")
        if g.check_Win(p1):
            game_over=True
            print("YOU WIN")
            break
        if g.check_draw():
            game_over=True
            print("DRAW")
            break
    if game_over:
        break
    while p==2:
        g.print_background()
        print("player 2")
        print("entre pos :")
        x=int(input("enter x :"))
        y=int(input("enter y :"))
        s=g.play(x,y,p2)
        if s: p=1
        else: print("pos taken choose again")
        if g.check_Win(p2):
            game_over=True
            print("YOU WIN")
            break
        if g.check_draw():
            game_over=True
            print("DRAW")
            break
    if game_over:
        break        
