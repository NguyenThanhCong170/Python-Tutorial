import turtle
import random
s=turtle.getscreen
#player1
player1=turtle.Turtle()
player1.speed(3)
player1.shape('turtle')
player1.color('red','red')
player1.penup()
player1.goto(-200,100)
player1.goto(300,60)
player1.pendown()
player1.circle(40)
player1.penup()
player1.goto(-200,100)
#player2
player2=player1.clone()
player2.color('blue','blue')
player2.penup()
player2.goto(-200,-100)
player2.goto(300,-140)
player2.pendown()
player2.circle(40)
player2.penup()
player2.goto(-200,-100)
# xucxac
die = [1,2,3,4,5,6]
for i in range(20):
    if player1.pos() >= (261,98):
        print('nguoi choi so 1 thang')
        break
    elif player2.pos()>=(261,-102):
        print('nguoi choi so 2 thang')
        break
    elif player1.pos() >= (261,98) and player2.pos()>=(261,-102):
        print('ca hai deu thang')
    else:
        role1 = input('player 1: nhan chu bat ki de quay: ')
        xucxac1 = random.choice(die)
        print('so cua xuc xac: ', xucxac1)
        player1.pendown()
        player1.fd(xucxac1*20)
        role2 = input('player 2: nhan chu bat ki de quay: ')
        xucxac2 = random.choice(die)
        print('so cua xuc xac: ',xucxac2)
        player2.pendown()
        player2.fd(20*xucxac2)

 
# # self defined function to print coordinate
# def buttonclick(x,y):
#     print("You clicked at this coordinate({0},{1})".format(x,y))
 
#  #onscreen function to send coordinate
# turtle.onscreenclick(buttonclick,1)
# turtle.listen()  # listen to incoming connections
# turtle.speed(10) # set the speed
# turtle.done()    # hold the screen
