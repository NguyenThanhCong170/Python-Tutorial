import pygame
import time
import random
from PIL import ImageGrab
img = ImageGrab.grab()
pygame.font.init()
# WIDTH, HEIGHT = img.size GET FULL SCREEN
WIDTH, HEIGHT = 800,620
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Caro GAME')
BG = pygame.transform.scale(pygame.image.load('Images/background.jpg'),(WIDTH,HEIGHT))


FONT = pygame.font.SysFont('Comic Sans',30)
FONT_caro = pygame.font.SysFont('Comic Sans',27)
FONT_player = pygame.font.SysFont('Arial',40)
FONT_lose = pygame.font.SysFont('Arial',25)

def draw(mx,my):
    WIN.blit(BG,(0,0))
    #Draw the title of the game
    title_text = FONT.render('CARO GAME !',1,'Purple')

    title_rect = pygame.Rect(WIDTH/2 - title_text.get_width()/2-9,20,title_text.get_width()+18,title_text.get_height()+10)
    WIN.fill((235, 101, 23),title_rect)
    pygame.draw.rect(WIN,(161, 82, 11),title_rect,width=2,border_radius=20)
    WIN.blit(title_text,(WIDTH/2 - title_text.get_width()/2,25))

    #COORDINATES OF RECT OF THE PLAYING PART
    xfirst,yfirst = 45,85
    rect_width,rect_height = 465,505
    xend,yend = rect_width + xfirst, rect_height+yfirst
    rect = pygame.Rect(xfirst,yfirst,rect_width,rect_height)
    pygame.draw.rect(WIN,(0, 0, 0),rect,width=4)

    #COORDINATES OF LINE FROM THE LEFT TO RIGHT #hang doc
    coordinates = []
    for i in range(1,12):
        xf,yf = ((xend-xfirst)*i)/12 +xfirst, yfirst
        xe,ye = ((xend-xfirst)*i)/12 +xfirst, yend -1 
        coordinates.append([(xf,yf),(xe,ye)])
    pygame.draw.line(WIN,(13, 13, 13),coordinates[0][0],coordinates[0][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[1][0],coordinates[1][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[2][0],coordinates[2][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[3][0],coordinates[3][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[4][0],coordinates[4][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[5][0],coordinates[5][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[6][0],coordinates[6][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[7][0],coordinates[7][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[8][0],coordinates[8][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[9][0],coordinates[9][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[10][0],coordinates[10][1],width=3)
    
    #COORDINATES OF LINE FROM THE TOP TO BOTTOME #hang ngang
    coordinates = []
    for i in range(1,12):
        xf,yf = xfirst, ((yend-yfirst)*i)/12 + yfirst
        xe,ye = xend-1, ((yend-yfirst)*i)/12 + yfirst
        coordinates.append([(xf,yf),(xe,ye)])
    pygame.draw.line(WIN,(13, 13, 13),coordinates[0][0],coordinates[0][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[1][0],coordinates[1][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[2][0],coordinates[2][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[3][0],coordinates[3][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[4][0],coordinates[4][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[5][0],coordinates[5][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[6][0],coordinates[6][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[7][0],coordinates[7][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[8][0],coordinates[8][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[9][0],coordinates[9][1],width=3)
    pygame.draw.line(WIN,(13, 13, 13),coordinates[10][0],coordinates[10][1],width=3)
    
    #Score Frame
    player_section_x_first = xend + 40
    player_section_y_first = 100
    player_section_width = 210
    player_section_height = 400
    player_section_x_end = player_section_x_first + player_section_width
    player_section_y_end = player_section_y_first + player_section_height
    frame = pygame.Rect(player_section_x_first,player_section_y_first,player_section_width,player_section_height)
    pygame.draw.rect(WIN,(28, 30, 31),frame,5,border_radius=10)
    pygame.draw.line(WIN,(28, 30, 31),(player_section_x_first + player_section_width/2,player_section_y_first),(player_section_x_end-player_section_width/2,player_section_y_end-1),5)
    pygame.draw.line(WIN,(28, 30, 31),(player_section_x_first,player_section_y_first+player_section_y_end/5),(player_section_x_end-1,player_section_y_first+player_section_y_end/5),5)
    pygame.draw.line(WIN,(28, 30, 31),(player_section_x_first,player_section_y_first+player_section_y_end/5 + 60),(player_section_x_end-1,player_section_y_first+player_section_y_end/5 + 60),5)
    
    
    # P1 and P2 player
    player1 = FONT_player.render('P1',1,(31, 11, 212))
    pos_player1_x = player_section_x_first + player_section_width/4 - player1.get_width()/2
    pos_player1_y = player_section_y_first+player_section_y_end/10 - player1.get_height()/2
    WIN.blit(player1,(pos_player1_x,pos_player1_y))

    player2 = FONT_player.render('P2',1,(31, 11, 212))
    pos_player2_x = player_section_x_first + player_section_width*3/4 - player1.get_width()/2
    pos_player2_y = player_section_y_first+player_section_y_end/10 - player1.get_height()/2
    WIN.blit(player2,(pos_player2_x,pos_player2_y))

    # Indicate the mark of each player
    X = FONT_player.render('X',1,(31, 11, 212))
    O = FONT_player.render('O',1,(31, 11, 212))

    pos_X_x = player_section_x_first + player_section_width/4 - X.get_width()/2
    pos_X_y = player_section_y_first + player_section_y_end/5 + 60/2 - X.get_height()/2
    
    pos_O_x = player_section_x_first + player_section_width*3/4 - O.get_width()/2
    pos_O_y = player_section_y_first + player_section_y_end/5 + 60/2 - O.get_height()/2

    WIN.blit(X,(pos_X_x,pos_X_y))
    WIN.blit(O,(pos_O_x,pos_O_y))

    # Indicate the score of each player


    ####


    # Indicate the button lose

    button_lose_player1 = pygame.Rect(player_section_x_first+15,player_section_y_end - 75,75, 60 )
    button_lose_player2 = pygame.Rect(player_section_x_first+ player_section_width/2 +15,player_section_y_end - 75,75, 60)
    
    lose_text = FONT_lose.render('LOSE',1,'black')

    lose_text_player1_x = button_lose_player1.x + button_lose_player1.width/2 - lose_text.get_width()/2
    lose_text_player1_y = button_lose_player1.y + button_lose_player1.height/2 - lose_text.get_height()/2

    lose_text_player2_x = button_lose_player2.x + button_lose_player2.width/2 - lose_text.get_width()/2
    lose_text_player2_y = button_lose_player2.y + button_lose_player2.height/2 - lose_text.get_height()/2


    if (player_section_x_first+15) <= mx <= (player_section_x_first+15 +75) and (player_section_y_end - 75) <=my <= (player_section_y_end - 75 +60):
        pygame.draw.rect(WIN,'white',button_lose_player1,border_radius=8)
    else:
        pygame.draw.rect(WIN,(224, 218, 218),button_lose_player1,border_radius=8)
    
    pygame.draw.rect(WIN,'black',button_lose_player1,width=3,border_radius=8)

    if (player_section_x_first+ player_section_width/2 +15) <= mx <= (player_section_x_first+ player_section_width/2 +15+75) and (player_section_y_end - 75) <=my <= (player_section_y_end - 75 +60):
        pygame.draw.rect(WIN,'white',button_lose_player2,border_radius=8)
    else:
        pygame.draw.rect(WIN,(224, 218, 218),button_lose_player2,border_radius=8)
    
    pygame.draw.rect(WIN,'black',button_lose_player1,width=3,border_radius=8)
    pygame.draw.rect(WIN,'black',button_lose_player2,width=3,border_radius=8)
    
    WIN.blit(lose_text,(lose_text_player1_x,lose_text_player1_y))
    WIN.blit(lose_text,(lose_text_player2_x,lose_text_player2_y))


    #  DRAW PART

    draw_button_x_first = player_section_x_first + 20
    draw_button_x_end = player_section_x_end - 20
    draw_button_x_width = draw_button_x_end - draw_button_x_first

    draw_button_y_first = player_section_y_end + 20
    draw_button_y_end = HEIGHT - 50
    draw_button_y_height = draw_button_y_end - draw_button_y_first

    draw_button = pygame.Rect(draw_button_x_first,draw_button_y_first,draw_button_x_width,draw_button_y_height)

    draw_word = FONT_lose.render('DRAW',1,(255, 0, 64))
    if (draw_button_x_first) <= mx <= (draw_button_x_end) and (draw_button_y_first) <= my <= draw_button_y_end:
        pygame.draw.rect(WIN,(166, 247, 239),draw_button,border_radius=10)
    else:
        pygame.draw.rect(WIN,(206, 245, 241),draw_button,border_radius=10)


    pygame.draw.rect(WIN,'black',draw_button,width=3,border_radius=10)
    WIN.blit(draw_word,(draw_button_x_first + draw_button_x_width/2 - draw_word.get_width()/2, draw_button_y_first + draw_button_y_height/2 - draw_word.get_height()/2))



    



#Coordinate of each rect 
xfirst,yfirst = 45,85
rect_width,rect_height = 465,505
xend,yend = rect_width + xfirst, rect_height+yfirst
rect = pygame.Rect(xfirst,yfirst,rect_width,rect_height)
Cor_Rect1 = []
Cor_Rect2 = []
Cor_Rect3 = []
Cor_Rect4 = []
Cor_Rect5 = []
Cor_Rect6 = []
Cor_Rect7 = []
Cor_Rect8 = []
Cor_Rect9 = []
Cor_Rect10 = []
Cor_Rect11 = []
Cor_Rect12 = []
Cor_Rect = []
for i in range(12):
    rect1 = pygame.Rect(xfirst+rect_width*i/12,yfirst,rect_width/12,rect_height/12) #Chi tinh phan hang
    Cor_Rect1.append(rect1)
    rect2 = pygame.Rect(xfirst+rect_width*i/12,yfirst+rect_height/12,rect_width/12,rect_height/12) 
    Cor_Rect2.append(rect2)
    rect3 = pygame.Rect(xfirst+rect_width*i/12,yfirst+rect_height*2/12,rect_width/12,rect_height/12) 
    Cor_Rect3.append(rect3)
    rect4 = pygame.Rect(xfirst+rect_width*i/12,yfirst+rect_height*3/12,rect_width/12,rect_height/12) 
    Cor_Rect4.append(rect4)
    rect5 = pygame.Rect(xfirst+rect_width*i/12,yfirst+rect_height*4/12,rect_width/12,rect_height/12) 
    Cor_Rect5.append(rect5)
    rect6 = pygame.Rect(xfirst+rect_width*i/12,yfirst+rect_height*5/12,rect_width/12,rect_height/12) 
    Cor_Rect6.append(rect6)
    rect7 = pygame.Rect(xfirst+rect_width*i/12,yfirst+rect_height*6/12,rect_width/12,rect_height/12) 
    Cor_Rect7.append(rect7)
    rect8 = pygame.Rect(xfirst+rect_width*i/12,yfirst+rect_height*7/12,rect_width/12,rect_height/12) 
    Cor_Rect8.append(rect8)
    rect9 = pygame.Rect(xfirst+rect_width*i/12,yfirst+rect_height*8/12,rect_width/12,rect_height/12) 
    Cor_Rect9.append(rect9)
    rect10 = pygame.Rect(xfirst+rect_width*i/12,yfirst+rect_height*9/12,rect_width/12,rect_height/12) 
    Cor_Rect10.append(rect10)
    rect11 = pygame.Rect(xfirst+rect_width*i/12,yfirst+rect_height*10/12,rect_width/12,rect_height/12) 
    Cor_Rect11.append(rect11)
    rect12 = pygame.Rect(xfirst+rect_width*i/12,yfirst+rect_height*11/12,rect_width/12,rect_height/12) 
    Cor_Rect12.append(rect12)
    Cor_Rect.append(rect1)
    Cor_Rect.append(rect2)
    Cor_Rect.append(rect3)
    Cor_Rect.append(rect4)
    Cor_Rect.append(rect5)
    Cor_Rect.append(rect6)
    Cor_Rect.append(rect7)
    Cor_Rect.append(rect8)
    Cor_Rect.append(rect9)
    Cor_Rect.append(rect10)
    Cor_Rect.append(rect11)
    Cor_Rect.append(rect12)
# def playing():
    

    
#     if i % 2 ==0: #luot choi cua P1
        
            

    
def main():
    run = True
    clock = pygame.time.Clock()
    markP1 = FONT_caro.render('X',1,'white')
    markP2 = FONT_caro.render('O',1,'white')
    xfirst,yfirst = 45,85
    rect_width,rect_height = 465,505
    xend,yend = rect_width + xfirst, rect_height+yfirst
    player_section_x_first = xend + 40
    player_section_y_first = 100
    player_section_width = 210
    player_section_height = 400
    player_section_x_end = player_section_x_first + player_section_width
    player_section_y_end = player_section_y_first + player_section_height
    button_lose_player1 = pygame.Rect(player_section_x_first+15,player_section_y_end - 75,75, 60 )
    button_lose_player2 = pygame.Rect(player_section_x_first+ player_section_width/2 +15,player_section_y_end - 75,75, 60)

    draw_button_x_first = player_section_x_first + 20
    draw_button_x_end = player_section_x_end - 20
    draw_button_x_width = draw_button_x_end - draw_button_x_first

    draw_button_y_first = player_section_y_end + 20
    draw_button_y_end = HEIGHT - 50
    draw_button_y_height = draw_button_y_end - draw_button_y_first

    draw_button = pygame.Rect(draw_button_x_first,draw_button_y_first,draw_button_x_width,draw_button_y_height)
    if True:

        dauhieuPfirst11 = False #hang truoc cot sau
        dauhieuPfirst12 = False
        dauhieuPfirst13 = False
        dauhieuPfirst14 = False
        dauhieuPfirst15 = False
        dauhieuPfirst16 = False
        dauhieuPfirst17 = False
        dauhieuPfirst18 = False
        dauhieuPfirst19 = False
        dauhieuPfirst110 = False
        dauhieuPfirst111= False
        dauhieuPfirst112= False
        dauhieuPfirst21= False
        dauhieuPfirst22 = False
        dauhieuPfirst23 = False
        dauhieuPfirst24 = False
        dauhieuPfirst25 = False
        dauhieuPfirst26 = False
        dauhieuPfirst27 = False
        dauhieuPfirst28 = False
        dauhieuPfirst29 = False
        dauhieuPfirst210 = False
        dauhieuPfirst211= False
        dauhieuPfirst212= False
        dauhieuPfirst31= False
        dauhieuPfirst32 = False
        dauhieuPfirst33 = False
        dauhieuPfirst34 = False
        dauhieuPfirst35 = False
        dauhieuPfirst36= False
        dauhieuPfirst37 = False
        dauhieuPfirst38 = False
        dauhieuPfirst39 = False
        dauhieuPfirst310 = False
        dauhieuPfirst311= False
        dauhieuPfirst312= False
        dauhieuPfirst41= False
        dauhieuPfirst42 = False
        dauhieuPfirst43 = False
        dauhieuPfirst44 = False
        dauhieuPfirst45 = False
        dauhieuPfirst46 = False
        dauhieuPfirst47 = False
        dauhieuPfirst48 = False
        dauhieuPfirst49 = False
        dauhieuPfirst410 = False
        dauhieuPfirst411= False
        dauhieuPfirst412= False
        dauhieuPfirst51= False
        dauhieuPfirst52 = False
        dauhieuPfirst53= False
        dauhieuPfirst54= False
        dauhieuPfirst55= False
        dauhieuPfirst56= False
        dauhieuPfirst57 = False
        dauhieuPfirst58 = False
        dauhieuPfirst59 = False
        dauhieuPfirst510 = False
        dauhieuPfirst511= False
        dauhieuPfirst512= False
        dauhieuPfirst61= False
        dauhieuPfirst62 = False
        dauhieuPfirst63 = False
        dauhieuPfirst64 = False
        dauhieuPfirst65 = False
        dauhieuPfirst66 = False
        dauhieuPfirst67 = False
        dauhieuPfirst68 = False
        dauhieuPfirst69 = False
        dauhieuPfirst610 = False
        dauhieuPfirst611= False
        dauhieuPfirst612= False
        dauhieuPfirst71= False
        dauhieuPfirst72 = False
        dauhieuPfirst73 = False
        dauhieuPfirst74 = False
        dauhieuPfirst75 = False
        dauhieuPfirst76= False
        dauhieuPfirst77= False
        dauhieuPfirst78= False
        dauhieuPfirst79 = False
        dauhieuPfirst710 = False
        dauhieuPfirst711= False
        dauhieuPfirst712= False
        dauhieuPfirst81= False
        dauhieuPfirst82 = False
        dauhieuPfirst83 = False
        dauhieuPfirst84 = False
        dauhieuPfirst85 = False
        dauhieuPfirst86= False
        dauhieuPfirst87= False
        dauhieuPfirst88= False
        dauhieuPfirst89 = False
        dauhieuPfirst810 = False
        dauhieuPfirst811= False
        dauhieuPfirst812= False
        dauhieuPfirst91= False
        dauhieuPfirst92= False
        dauhieuPfirst93= False
        dauhieuPfirst94 = False
        dauhieuPfirst95 = False
        dauhieuPfirst96 = False
        dauhieuPfirst97 = False
        dauhieuPfirst98 = False
        dauhieuPfirst99 = False
        dauhieuPfirst910 = False
        dauhieuPfirst911= False
        dauhieuPfirst912 = False
        dauhieuPfirst101= False
        dauhieuPfirst102= False
        dauhieuPfirst103= False
        dauhieuPfirst104= False
        dauhieuPfirst105= False
        dauhieuPfirst106= False
        dauhieuPfirst107= False
        dauhieuPfirst108= False
        dauhieuPfirst109= False
        dauhieuPfirst1010= False
        dauhieuPfirst1011= False
        dauhieuPfirst1012= False
        dauhieuPfirst111a= False
        dauhieuPfirst112a= False
        dauhieuPfirst113= False
        dauhieuPfirst114= False
        dauhieuPfirst115= False
        dauhieuPfirst116= False
        dauhieuPfirst117= False
        dauhieuPfirst118= False
        dauhieuPfirst119= False
        dauhieuPfirst1110= False
        dauhieuPfirst1111= False
        dauhieuPfirst1112= False
        dauhieuPfirst121= False
        dauhieuPfirst122= False
        dauhieuPfirst123= False
        dauhieuPfirst124= False
        dauhieuPfirst125= False
        dauhieuPfirst126= False
        dauhieuPfirst127= False
        dauhieuPfirst128= False
        dauhieuPfirst129= False
        dauhieuPfirst1210= False
        dauhieuPfirst1211= False
        dauhieuPfirst1212= False

        

        dauhieuPsecond11 = False #hang truoc cot sau
        dauhieuPsecond12 = False
        dauhieuPsecond13 = False
        dauhieuPsecond14 = False
        dauhieuPsecond15 = False
        dauhieuPsecond16 = False
        dauhieuPsecond17 = False
        dauhieuPsecond18 = False
        dauhieuPsecond19 = False
        dauhieuPsecond110 = False
        dauhieuPsecond111= False
        dauhieuPsecond112= False
        dauhieuPsecond21= False
        dauhieuPsecond22 = False
        dauhieuPsecond23 = False
        dauhieuPsecond24 = False
        dauhieuPsecond25 = False
        dauhieuPsecond26 = False
        dauhieuPsecond27 = False
        dauhieuPsecond28 = False
        dauhieuPsecond29 = False
        dauhieuPsecond210 = False
        dauhieuPsecond211= False
        dauhieuPsecond212= False
        dauhieuPsecond31= False
        dauhieuPsecond32 = False
        dauhieuPsecond33 = False
        dauhieuPsecond34 = False
        dauhieuPsecond35 = False
        dauhieuPsecond36= False
        dauhieuPsecond37 = False
        dauhieuPsecond38 = False
        dauhieuPsecond39 = False
        dauhieuPsecond310 = False
        dauhieuPsecond311= False
        dauhieuPsecond312= False
        dauhieuPsecond41= False
        dauhieuPsecond42 = False
        dauhieuPsecond43 = False
        dauhieuPsecond44 = False
        dauhieuPsecond45 = False
        dauhieuPsecond46 = False
        dauhieuPsecond47 = False
        dauhieuPsecond48 = False
        dauhieuPsecond49 = False
        dauhieuPsecond410 = False
        dauhieuPsecond411= False
        dauhieuPsecond412= False
        dauhieuPsecond51= False
        dauhieuPsecond52 = False
        dauhieuPsecond53= False
        dauhieuPsecond54= False
        dauhieuPsecond55= False
        dauhieuPsecond56= False
        dauhieuPsecond57 = False
        dauhieuPsecond58 = False
        dauhieuPsecond59 = False
        dauhieuPsecond510 = False
        dauhieuPsecond511= False
        dauhieuPsecond512= False
        dauhieuPsecond61= False
        dauhieuPsecond62 = False
        dauhieuPsecond63 = False
        dauhieuPsecond64 = False
        dauhieuPsecond65 = False
        dauhieuPsecond66 = False
        dauhieuPsecond67 = False
        dauhieuPsecond68 = False
        dauhieuPsecond69 = False
        dauhieuPsecond610 = False
        dauhieuPsecond611= False
        dauhieuPsecond612= False
        dauhieuPsecond71= False
        dauhieuPsecond72 = False
        dauhieuPsecond73 = False
        dauhieuPsecond74 = False
        dauhieuPsecond75 = False
        dauhieuPsecond76= False
        dauhieuPsecond77= False
        dauhieuPsecond78= False
        dauhieuPsecond79 = False
        dauhieuPsecond710 = False
        dauhieuPsecond711= False
        dauhieuPsecond712= False
        dauhieuPsecond81= False
        dauhieuPsecond82 = False
        dauhieuPsecond83 = False
        dauhieuPsecond84 = False
        dauhieuPsecond85 = False
        dauhieuPsecond86= False
        dauhieuPsecond87= False
        dauhieuPsecond88= False
        dauhieuPsecond89 = False
        dauhieuPsecond810 = False
        dauhieuPsecond811= False
        dauhieuPsecond812= False
        dauhieuPsecond91= False
        dauhieuPsecond92= False
        dauhieuPsecond93= False
        dauhieuPsecond94 = False
        dauhieuPsecond95 = False
        dauhieuPsecond96 = False
        dauhieuPsecond97 = False
        dauhieuPsecond98 = False
        dauhieuPsecond99 = False
        dauhieuPsecond910 = False
        dauhieuPsecond911= False
        dauhieuPsecond912 = False
        dauhieuPsecond101= False
        dauhieuPsecond102= False
        dauhieuPsecond103= False
        dauhieuPsecond104= False
        dauhieuPsecond105= False
        dauhieuPsecond106= False
        dauhieuPsecond107= False
        dauhieuPsecond108= False
        dauhieuPsecond109= False
        dauhieuPsecond1010= False
        dauhieuPsecond1011= False
        dauhieuPsecond1012= False
        dauhieuPsecond111a= False
        dauhieuPsecond112a= False
        dauhieuPsecond113= False
        dauhieuPsecond114= False
        dauhieuPsecond115= False
        dauhieuPsecond116= False
        dauhieuPsecond117= False
        dauhieuPsecond118= False
        dauhieuPsecond119= False
        dauhieuPsecond1110= False
        dauhieuPsecond1111= False
        dauhieuPsecond1112= False
        dauhieuPsecond121= False
        dauhieuPsecond122= False
        dauhieuPsecond123= False
        dauhieuPsecond124= False
        dauhieuPsecond125= False
        dauhieuPsecond126= False
        dauhieuPsecond127= False
        dauhieuPsecond128= False
        dauhieuPsecond129= False
        dauhieuPsecond1210= False
        dauhieuPsecond1211= False
        dauhieuPsecond1212= False


        dauhieu11 = [dauhieuPfirst11,dauhieuPsecond11]
        dauhieu12 = [dauhieuPfirst12,dauhieuPsecond12]
        dauhieu13 = [dauhieuPfirst13,dauhieuPsecond13]
        dauhieu14 = [dauhieuPfirst14,dauhieuPsecond14]
        dauhieu15 = [dauhieuPfirst15,dauhieuPsecond15]
        dauhieu16 = [dauhieuPfirst16,dauhieuPsecond16]
        dauhieu17 = [dauhieuPfirst17,dauhieuPsecond17]
        dauhieu18 = [dauhieuPfirst18,dauhieuPsecond18]
        dauhieu19 = [dauhieuPfirst19,dauhieuPsecond19]
        dauhieu110 = [dauhieuPfirst110,dauhieuPsecond110]
        dauhieu111 = [dauhieuPfirst111,dauhieuPsecond111]
        dauhieu112 = [dauhieuPfirst112,dauhieuPsecond112]
    
        dauhieu21 = [dauhieuPfirst21,dauhieuPsecond21]
        dauhieu22 = [dauhieuPfirst22,dauhieuPsecond22]
        dauhieu23 = [dauhieuPfirst23,dauhieuPsecond23]
        dauhieu24 = [dauhieuPfirst24,dauhieuPsecond24]
        dauhieu25 = [dauhieuPfirst25,dauhieuPsecond25]
        dauhieu26 = [dauhieuPfirst26,dauhieuPsecond26]
        dauhieu27 = [dauhieuPfirst27,dauhieuPsecond27]
        dauhieu28 = [dauhieuPfirst28,dauhieuPsecond28]
        dauhieu29 = [dauhieuPfirst29,dauhieuPsecond29]
        dauhieu210 = [dauhieuPfirst210,dauhieuPsecond210]
        dauhieu211 = [dauhieuPfirst211,dauhieuPsecond211]
        dauhieu212 = [dauhieuPfirst212,dauhieuPsecond212]
    
        dauhieu31 = [dauhieuPfirst31,dauhieuPsecond31]
        dauhieu32 = [dauhieuPfirst32,dauhieuPsecond32]
        dauhieu33 = [dauhieuPfirst33,dauhieuPsecond33]
        dauhieu34 = [dauhieuPfirst34,dauhieuPsecond34]
        dauhieu35 = [dauhieuPfirst35,dauhieuPsecond35]
        dauhieu36 = [dauhieuPfirst36,dauhieuPsecond36]
        dauhieu37 = [dauhieuPfirst37,dauhieuPsecond37]
        dauhieu38 = [dauhieuPfirst38,dauhieuPsecond38]
        dauhieu39 = [dauhieuPfirst39,dauhieuPsecond39]
        dauhieu310 = [dauhieuPfirst310,dauhieuPsecond310]
        dauhieu311 = [dauhieuPfirst311,dauhieuPsecond311]
        dauhieu312 = [dauhieuPfirst312,dauhieuPsecond312]
    
        dauhieu41 = [dauhieuPfirst41,dauhieuPsecond41]
        dauhieu42 = [dauhieuPfirst42,dauhieuPsecond42]
        dauhieu43 = [dauhieuPfirst43,dauhieuPsecond43]
        dauhieu44 = [dauhieuPfirst44,dauhieuPsecond44]
        dauhieu45 = [dauhieuPfirst45,dauhieuPsecond45]
        dauhieu46 = [dauhieuPfirst46,dauhieuPsecond46]
        dauhieu47 = [dauhieuPfirst47,dauhieuPsecond47]
        dauhieu48 = [dauhieuPfirst48,dauhieuPsecond48]
        dauhieu49 = [dauhieuPfirst49,dauhieuPsecond49]
        dauhieu410 = [dauhieuPfirst410,dauhieuPsecond410]
        dauhieu411 = [dauhieuPfirst411,dauhieuPsecond411]
        dauhieu412 = [dauhieuPfirst412,dauhieuPsecond412]
    
        dauhieu51 = [dauhieuPfirst51,dauhieuPsecond51]
        dauhieu52 = [dauhieuPfirst52,dauhieuPsecond52]
        dauhieu53 = [dauhieuPfirst53,dauhieuPsecond53]
        dauhieu54 = [dauhieuPfirst54,dauhieuPsecond54]
        dauhieu55 = [dauhieuPfirst55,dauhieuPsecond55]
        dauhieu56 = [dauhieuPfirst56,dauhieuPsecond56]
        dauhieu57 = [dauhieuPfirst57,dauhieuPsecond57]
        dauhieu58 = [dauhieuPfirst58,dauhieuPsecond58]
        dauhieu59 = [dauhieuPfirst59,dauhieuPsecond59]
        dauhieu510 = [dauhieuPfirst510,dauhieuPsecond510]
        dauhieu511 = [dauhieuPfirst511,dauhieuPsecond511]
        dauhieu512 = [dauhieuPfirst512,dauhieuPsecond512]
        
        dauhieu61 = [dauhieuPfirst61,dauhieuPsecond61]
        dauhieu62 = [dauhieuPfirst62,dauhieuPsecond62]
        dauhieu63 = [dauhieuPfirst63,dauhieuPsecond63]
        dauhieu64 = [dauhieuPfirst64,dauhieuPsecond64]
        dauhieu65 = [dauhieuPfirst65,dauhieuPsecond65]
        dauhieu66 = [dauhieuPfirst66,dauhieuPsecond66]
        dauhieu67 = [dauhieuPfirst67,dauhieuPsecond67]
        dauhieu68 = [dauhieuPfirst68,dauhieuPsecond68]
        dauhieu69 = [dauhieuPfirst69,dauhieuPsecond69]
        dauhieu610 = [dauhieuPfirst610,dauhieuPsecond610]
        dauhieu611 = [dauhieuPfirst611,dauhieuPsecond611]
        dauhieu612 = [dauhieuPfirst612,dauhieuPsecond612]
        
        dauhieu71 = [dauhieuPfirst71,dauhieuPsecond71]
        dauhieu72 = [dauhieuPfirst72,dauhieuPsecond72]
        dauhieu73 = [dauhieuPfirst73,dauhieuPsecond73]
        dauhieu74 = [dauhieuPfirst74,dauhieuPsecond74]
        dauhieu75 = [dauhieuPfirst75,dauhieuPsecond75]
        dauhieu76 = [dauhieuPfirst76,dauhieuPsecond76]
        dauhieu77 = [dauhieuPfirst77,dauhieuPsecond77]
        dauhieu78 = [dauhieuPfirst78,dauhieuPsecond78]
        dauhieu79 = [dauhieuPfirst79,dauhieuPsecond79]
        dauhieu710 = [dauhieuPfirst710,dauhieuPsecond710]
        dauhieu711 = [dauhieuPfirst711,dauhieuPsecond711]
        dauhieu712 = [dauhieuPfirst712,dauhieuPsecond712]

        dauhieu81 = [dauhieuPfirst81,dauhieuPsecond81]
        dauhieu82 = [dauhieuPfirst82,dauhieuPsecond82]
        dauhieu83 = [dauhieuPfirst83,dauhieuPsecond83]
        dauhieu84 = [dauhieuPfirst84,dauhieuPsecond84]
        dauhieu85 = [dauhieuPfirst85,dauhieuPsecond85]
        dauhieu86 = [dauhieuPfirst86,dauhieuPsecond86]
        dauhieu87 = [dauhieuPfirst87,dauhieuPsecond87]
        dauhieu88 = [dauhieuPfirst88,dauhieuPsecond88]
        dauhieu89 = [dauhieuPfirst89,dauhieuPsecond89]
        dauhieu810 = [dauhieuPfirst810,dauhieuPsecond810]
        dauhieu811 = [dauhieuPfirst811,dauhieuPsecond811]
        dauhieu812 = [dauhieuPfirst812,dauhieuPsecond812]
            
        dauhieu91 = [dauhieuPfirst91,dauhieuPsecond91]
        dauhieu92 = [dauhieuPfirst92,dauhieuPsecond92]
        dauhieu93 = [dauhieuPfirst93,dauhieuPsecond93]
        dauhieu94 = [dauhieuPfirst94,dauhieuPsecond94]
        dauhieu95 = [dauhieuPfirst95,dauhieuPsecond95]
        dauhieu96 = [dauhieuPfirst96,dauhieuPsecond96]
        dauhieu97 = [dauhieuPfirst97,dauhieuPsecond97]
        dauhieu98 = [dauhieuPfirst98,dauhieuPsecond98]
        dauhieu99 = [dauhieuPfirst99,dauhieuPsecond99]
        dauhieu910 = [dauhieuPfirst910,dauhieuPsecond910]
        dauhieu911 = [dauhieuPfirst911,dauhieuPsecond911]
        dauhieu912 = [dauhieuPfirst912,dauhieuPsecond912]
        
        dauhieu101 = [dauhieuPfirst101,dauhieuPsecond101]
        dauhieu102 = [dauhieuPfirst102,dauhieuPsecond102]
        dauhieu103 = [dauhieuPfirst103,dauhieuPsecond103]
        dauhieu104 = [dauhieuPfirst104,dauhieuPsecond104]
        dauhieu105 = [dauhieuPfirst105,dauhieuPsecond105]
        dauhieu106 = [dauhieuPfirst106,dauhieuPsecond106]
        dauhieu107 = [dauhieuPfirst107,dauhieuPsecond107]
        dauhieu108 = [dauhieuPfirst108,dauhieuPsecond108]
        dauhieu109 = [dauhieuPfirst109,dauhieuPsecond109]
        dauhieu1010 = [dauhieuPfirst1010,dauhieuPsecond1010]
        dauhieu1011 = [dauhieuPfirst1011,dauhieuPsecond1011]
        dauhieu1012 = [dauhieuPfirst1012,dauhieuPsecond1012]
        
        
        dauhieu111 = [dauhieuPfirst111a,dauhieuPsecond111a]
        dauhieu112 = [dauhieuPfirst112a,dauhieuPsecond112a]
        dauhieu113 = [dauhieuPfirst113,dauhieuPsecond113]
        dauhieu114 = [dauhieuPfirst114,dauhieuPsecond114]
        dauhieu115 = [dauhieuPfirst115,dauhieuPsecond115]
        dauhieu116 = [dauhieuPfirst116,dauhieuPsecond116]
        dauhieu117 = [dauhieuPfirst117,dauhieuPsecond117]
        dauhieu118 = [dauhieuPfirst118,dauhieuPsecond118]
        dauhieu119 = [dauhieuPfirst119,dauhieuPsecond119]
        dauhieu1110 = [dauhieuPfirst1110,dauhieuPsecond1110]
        dauhieu1111 = [dauhieuPfirst1111,dauhieuPsecond1111]
        dauhieu1112 = [dauhieuPfirst1112,dauhieuPsecond1112]
        
        dauhieu121 = [dauhieuPfirst121,dauhieuPsecond121]
        dauhieu122 = [dauhieuPfirst122,dauhieuPsecond122]
        dauhieu123 = [dauhieuPfirst123,dauhieuPsecond123]
        dauhieu124 = [dauhieuPfirst124,dauhieuPsecond124]
        dauhieu125 = [dauhieuPfirst125,dauhieuPsecond125]
        dauhieu126 = [dauhieuPfirst126,dauhieuPsecond126]
        dauhieu127 = [dauhieuPfirst127,dauhieuPsecond127]
        dauhieu128 = [dauhieuPfirst128,dauhieuPsecond128]
        dauhieu129 = [dauhieuPfirst129,dauhieuPsecond129]
        dauhieu1210 = [dauhieuPfirst1210,dauhieuPsecond1210]
        dauhieu1211 = [dauhieuPfirst1211,dauhieuPsecond1211]
        dauhieu1212 = [dauhieuPfirst1212,dauhieuPsecond1212]
        
        dauhieu = [dauhieu11,dauhieu12,dauhieu13,dauhieu14,dauhieu15,dauhieu16,dauhieu17,dauhieu18,dauhieu19,dauhieu110,dauhieu111,dauhieu112,dauhieu21,dauhieu22,dauhieu23,dauhieu24,dauhieu25,dauhieu26,dauhieu27,dauhieu28,dauhieu29,dauhieu210,dauhieu211,dauhieu212,dauhieu31,dauhieu32,dauhieu33,dauhieu34,dauhieu35,dauhieu36,dauhieu37,dauhieu38,dauhieu39,dauhieu310,dauhieu311,dauhieu312,dauhieu41,dauhieu42,dauhieu43,dauhieu44,dauhieu45,dauhieu46,dauhieu47,dauhieu48,dauhieu49,dauhieu410,dauhieu411,dauhieu412,dauhieu51,dauhieu52,dauhieu53,dauhieu54,dauhieu55,dauhieu56,dauhieu57,dauhieu58,dauhieu59,dauhieu510,dauhieu511,dauhieu512,dauhieu61,dauhieu62,dauhieu63,dauhieu64,dauhieu65,dauhieu66,dauhieu67,dauhieu68,dauhieu69,dauhieu610,dauhieu611,dauhieu612,dauhieu71,dauhieu72,dauhieu73,dauhieu74,dauhieu75,dauhieu76,dauhieu77,dauhieu78,dauhieu79,dauhieu710,dauhieu711,dauhieu712,dauhieu81,dauhieu82,dauhieu83,dauhieu84,dauhieu85,dauhieu86,dauhieu87,dauhieu88,dauhieu89,dauhieu810,dauhieu811,dauhieu812,dauhieu91,dauhieu92,dauhieu93,dauhieu94,dauhieu95,dauhieu96,dauhieu97,dauhieu98,dauhieu99,dauhieu910,dauhieu911,dauhieu912,dauhieu101,dauhieu102,dauhieu103,dauhieu104,dauhieu105,dauhieu106,dauhieu107,dauhieu108,dauhieu109,dauhieu1010,dauhieu1011,dauhieu1012,dauhieu111,dauhieu112,dauhieu113,dauhieu114,dauhieu115,dauhieu116,dauhieu117,dauhieu118,dauhieu119,dauhieu1110,dauhieu1111,dauhieu1112,dauhieu121,dauhieu122,dauhieu123,dauhieu124,dauhieu125,dauhieu126,dauhieu127,dauhieu128,dauhieu129,dauhieu1210,dauhieu1211,dauhieu1212]



    Mark_rect = []
    for j in range(12): #hang truoc cot sau
        for i in range(12):
            mark_rect = [xfirst + rect_width*i/12 + rect_width/24 - markP1.get_width()/2,yfirst + rect_height*j/12 + rect_height/24 - markP1.get_height()/2]
            Mark_rect.append(mark_rect)

    grid = [[" "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "]]

    i = 0 #luot choi
    while run:
        clock.tick(60)
        

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if i%2 == 0:
                    #hang 1
                        if Cor_Rect1[0].collidepoint(event.pos):
                            dauhieuPfirst11 = True    
                            i += 1 
                        if Cor_Rect1[1].collidepoint(event.pos):
                            dauhieuPfirst12 = True
                            i += 1 
                        if Cor_Rect1[2].collidepoint(event.pos):
                            dauhieuPfirst13 = True
                            i += 1 
                        if Cor_Rect1[3].collidepoint(event.pos):
                            dauhieuPfirst14 = True
                            i += 1 
                        if Cor_Rect1[4].collidepoint(event.pos):
                            dauhieuPfirst15 = True
                            i += 1 
                        if Cor_Rect1[5].collidepoint(event.pos):
                            dauhieuPfirst16 = True
                            i += 1 
                        if Cor_Rect1[6].collidepoint(event.pos):
                            dauhieuPfirst17 = True
                            i += 1 
                        if Cor_Rect1[7].collidepoint(event.pos):
                            dauhieuPfirst18 = True
                            i += 1 
                        if Cor_Rect1[8].collidepoint(event.pos):
                            dauhieuPfirst19 = True
                            i += 1 
                        if Cor_Rect1[9].collidepoint(event.pos):
                            dauhieuPfirst110 = True
                            i += 1 
                        if Cor_Rect1[10].collidepoint(event.pos):
                            dauhieuPfirst111 = True
                            i += 1 
                        if Cor_Rect1[11].collidepoint(event.pos):
                            dauhieuPfirst112 = True
                        #hang 2
                        if Cor_Rect2[0].collidepoint(event.pos):
                            dauhieuPfirst21 = True
                            i += 1 
                        if Cor_Rect2[1].collidepoint(event.pos):
                            dauhieuPfirst22 = True
                            i += 1 
                        if Cor_Rect2[2].collidepoint(event.pos):
                            dauhieuPfirst23 = True
                            i += 1 
                        if Cor_Rect2[3].collidepoint(event.pos):
                            dauhieuPfirst24 = True
                            i += 1 
                        if Cor_Rect2[4].collidepoint(event.pos):
                            dauhieuPfirst25 = True
                            i += 1 
                        if Cor_Rect2[5].collidepoint(event.pos):
                            dauhieuPfirst26 = True
                            i += 1 
                        if Cor_Rect2[6].collidepoint(event.pos):
                            dauhieuPfirst27 = True
                            i += 1 
                        if Cor_Rect2[7].collidepoint(event.pos):
                            dauhieuPfirst28 = True
                            i += 1 
                        if Cor_Rect2[8].collidepoint(event.pos):
                            dauhieuPfirst29 = True
                            i += 1 

                        if Cor_Rect2[9].collidepoint(event.pos):
                            dauhieuPfirst210 = True
                            i += 1 
                        if Cor_Rect2[10].collidepoint(event.pos):
                            dauhieuPfirst211 = True
                            i += 1 
                        if Cor_Rect2[11].collidepoint(event.pos):
                            dauhieuPfirst212 = True
                            i += 1 
                        #hang 3
                        if Cor_Rect3[0].collidepoint(event.pos):
                            dauhieuPfirst31 = True
                            i += 1 
                        if Cor_Rect3[1].collidepoint(event.pos):
                            dauhieuPfirst32 = True
                            i += 1 
                        if Cor_Rect3[2].collidepoint(event.pos):
                            dauhieuPfirst33 = True
                            i += 1 
                        if Cor_Rect3[3].collidepoint(event.pos):
                            dauhieuPfirst34 = True
                            i += 1 
                        if Cor_Rect3[4].collidepoint(event.pos):
                            dauhieuPfirst35 = True
                            i += 1 
                        if Cor_Rect3[5].collidepoint(event.pos):
                            dauhieuPfirst36 = True
                            i += 1 
                        if Cor_Rect3[6].collidepoint(event.pos):
                            dauhieuPfirst37 = True
                            i += 1 
                        if Cor_Rect3[7].collidepoint(event.pos):
                            dauhieuPfirst38 = True
                            i += 1 
                        if Cor_Rect3[8].collidepoint(event.pos):
                            dauhieuPfirst39 = True
                            i += 1 
                        if Cor_Rect3[9].collidepoint(event.pos):
                            dauhieuPfirst310 = True
                            i += 1 
                        if Cor_Rect3[10].collidepoint(event.pos):
                            dauhieuPfirst311 = True
                            i += 1 
                        if Cor_Rect3[11].collidepoint(event.pos):
                            dauhieuPfirst312 = True
                            i += 1 
                        #hang 4
                        if Cor_Rect4[0].collidepoint(event.pos):
                            dauhieuPfirst41 = True
                            i += 1 
                        if Cor_Rect4[1].collidepoint(event.pos):
                            dauhieuPfirst42 = True
                            i += 1 
                        if Cor_Rect4[2].collidepoint(event.pos):
                            dauhieuPfirst43 = True
                            i += 1 
                        if Cor_Rect4[3].collidepoint(event.pos):
                            dauhieuPfirst44 = True
                            i += 1 
                        if Cor_Rect4[4].collidepoint(event.pos):
                            dauhieuPfirst45 = True
                            i += 1 
                        if Cor_Rect4[5].collidepoint(event.pos):
                            dauhieuPfirst46 = True
                            i += 1 
                        if Cor_Rect4[6].collidepoint(event.pos):
                            dauhieuPfirst47 = True
                            i += 1 
                        if Cor_Rect4[7].collidepoint(event.pos):
                            dauhieuPfirst48 = True
                            i += 1 
                        if Cor_Rect4[8].collidepoint(event.pos):
                            dauhieuPfirst49 = True
                            i += 1 
                        if Cor_Rect4[9].collidepoint(event.pos):
                            dauhieuPfirst410 = True
                            i += 1 
                        if Cor_Rect4[10].collidepoint(event.pos):
                            dauhieuPfirst411 = True
                            i += 1 
                        if Cor_Rect4[11].collidepoint(event.pos):
                            dauhieuPfirst412 = True
                            i += 1 
                        #hang 5
                        if Cor_Rect5[0].collidepoint(event.pos):
                            dauhieuPfirst51 = True
                            i += 1 
                        if Cor_Rect5[1].collidepoint(event.pos):
                            dauhieuPfirst52 = True
                            i += 1 
                        if Cor_Rect5[2].collidepoint(event.pos):
                            dauhieuPfirst53 = True
                            i += 1 
                        if Cor_Rect5[3].collidepoint(event.pos):
                            dauhieuPfirst54 = True
                            i += 1 
                        if Cor_Rect5[4].collidepoint(event.pos):
                            dauhieuPfirst55 = True
                            i += 1 
                        if Cor_Rect5[5].collidepoint(event.pos):
                            dauhieuPfirst56 = True
                            i += 1 
                        if Cor_Rect5[6].collidepoint(event.pos):
                            dauhieuPfirst57 = True
                            i += 1 
                        if Cor_Rect5[7].collidepoint(event.pos):
                            dauhieuPfirst58 = True
                            i += 1 
                        if Cor_Rect5[8].collidepoint(event.pos):
                            dauhieuPfirst59 = True
                            i += 1 
                        if Cor_Rect5[9].collidepoint(event.pos):
                            dauhieuPfirst510 = True
                            i += 1 
                        if Cor_Rect5[10].collidepoint(event.pos):
                            dauhieuPfirst511 = True
                            i += 1 
                        if Cor_Rect5[11].collidepoint(event.pos):
                            dauhieuPfirst512 = True
                            i += 1 
                        #hang 6
                        if Cor_Rect6[0].collidepoint(event.pos):
                            dauhieuPfirst61 = True
                            i += 1 
                        if Cor_Rect6[1].collidepoint(event.pos):
                            dauhieuPfirst62 = True
                            i += 1 
                        if Cor_Rect6[2].collidepoint(event.pos):
                            dauhieuPfirst63 = True
                            i += 1 
                        if Cor_Rect6[3].collidepoint(event.pos):
                            dauhieuPfirst64 = True
                            i += 1 
                        if Cor_Rect6[4].collidepoint(event.pos):
                            dauhieuPfirst65 = True
                            i += 1 
                        if Cor_Rect6[5].collidepoint(event.pos):
                            dauhieuPfirst66 = True
                            i += 1 
                        if Cor_Rect6[6].collidepoint(event.pos):
                            dauhieuPfirst67 = True
                            i += 1 
                        if Cor_Rect6[7].collidepoint(event.pos):
                            dauhieuPfirst68 = True
                            i += 1 
                        if Cor_Rect6[8].collidepoint(event.pos):
                            dauhieuPfirst69 = True
                            i += 1 
                        if Cor_Rect6[9].collidepoint(event.pos):
                            dauhieuPfirst610 = True
                            i += 1 
                        if Cor_Rect6[10].collidepoint(event.pos):
                            dauhieuPfirst611 = True
                            i += 1 
                        if Cor_Rect6[11].collidepoint(event.pos):
                            dauhieuPfirst612 = True
                            i += 1 
                        #hang 7
                        if Cor_Rect7[0].collidepoint(event.pos):
                            dauhieuPfirst71 = True
                            i += 1 
                        if Cor_Rect7[1].collidepoint(event.pos):
                            dauhieuPfirst72 = True
                            i += 1 
                        if Cor_Rect7[2].collidepoint(event.pos):
                            dauhieuPfirst73 = True
                            i += 1 
                        if Cor_Rect7[3].collidepoint(event.pos):
                            dauhieuPfirst74 = True
                            i += 1 
                        if Cor_Rect7[4].collidepoint(event.pos):
                            dauhieuPfirst75 = True
                            i += 1 
                        if Cor_Rect7[5].collidepoint(event.pos):
                            dauhieuPfirst76 = True
                            i += 1          
                        if Cor_Rect7[6].collidepoint(event.pos):
                            dauhieuPfirst77 = True
                            i += 1 
                        if Cor_Rect7[7].collidepoint(event.pos):
                            dauhieuPfirst78 = True
                            i += 1 
                        if Cor_Rect7[8].collidepoint(event.pos):
                            dauhieuPfirst79 = True
                            i += 1 
                        if Cor_Rect7[9].collidepoint(event.pos):
                            dauhieuPfirst710 = True
                            i += 1 
                        if Cor_Rect7[10].collidepoint(event.pos):
                            dauhieuPfirst711 = True
                            i += 1 
                        if Cor_Rect7[11].collidepoint(event.pos):
                            dauhieuPfirst712 = True
                            i += 1 
                        #hang 8
                        if Cor_Rect8[0].collidepoint(event.pos):
                            dauhieuPfirst81 = True
                            i += 1 
                        if Cor_Rect8[1].collidepoint(event.pos):
                            dauhieuPfirst82 = True
                            i += 1 
                        if Cor_Rect8[2].collidepoint(event.pos):
                            dauhieuPfirst83 = True
                            i += 1 
                        if Cor_Rect8[3].collidepoint(event.pos):
                            dauhieuPfirst84 = True
                            i += 1 
                        if Cor_Rect8[4].collidepoint(event.pos):
                            dauhieuPfirst85 = True
                            i += 1 
                        if Cor_Rect8[5].collidepoint(event.pos):
                            dauhieuPfirst86 = True
                            i += 1 
                        if Cor_Rect8[6].collidepoint(event.pos):
                            dauhieuPfirst87 = True
                            i += 1 
                        if Cor_Rect8[7].collidepoint(event.pos):
                            dauhieuPfirst88 = True
                            i += 1 
                        if Cor_Rect8[8].collidepoint(event.pos):
                            dauhieuPfirst89 = True
                            i += 1 
                        if Cor_Rect8[9].collidepoint(event.pos):
                            dauhieuPfirst810 = True
                            i += 1 
                        if Cor_Rect8[10].collidepoint(event.pos):
                            dauhieuPfirst811 = True
                            i += 1 
                        if Cor_Rect8[11].collidepoint(event.pos):
                            dauhieuPfirst812 = True
                            i += 1 
                        #hang 9
                        if Cor_Rect9[0].collidepoint(event.pos):
                            dauhieuPfirst91 = True
                            i += 1 
                        if Cor_Rect9[1].collidepoint(event.pos):
                            dauhieuPfirst92 = True
                            i += 1 
                        if Cor_Rect9[2].collidepoint(event.pos):
                            dauhieuPfirst93 = True
                            i += 1 
                        if Cor_Rect9[3].collidepoint(event.pos):
                            dauhieuPfirst94 = True
                            i += 1 
                        if Cor_Rect9[4].collidepoint(event.pos):
                            dauhieuPfirst95 = True
                            i += 1 
                        if Cor_Rect9[5].collidepoint(event.pos):
                            dauhieuPfirst96 = True
                            i += 1 
                        if Cor_Rect9[6].collidepoint(event.pos):
                            dauhieuPfirst97 = True
                            i += 1 
                        if Cor_Rect9[7].collidepoint(event.pos):
                            dauhieuPfirst98 = True
                            i += 1 
                        if Cor_Rect9[8].collidepoint(event.pos):
                            dauhieuPfirst99 = True
                            i += 1 
                        if Cor_Rect9[9].collidepoint(event.pos):
                            dauhieuPfirst910 = True
                            i += 1 
                        if Cor_Rect9[10].collidepoint(event.pos):
                            dauhieuPfirst911 = True
                            i += 1 
                        if Cor_Rect9[11].collidepoint(event.pos):
                            dauhieuPfirst912 = True
                            i += 1 
                        #hang 10
                        if Cor_Rect10[0].collidepoint(event.pos):
                            dauhieuPfirst101 = True
                            i += 1 
                        if Cor_Rect10[1].collidepoint(event.pos):
                            dauhieuPfirst102 = True
                            i += 1 
                        if Cor_Rect10[2].collidepoint(event.pos):
                            dauhieuPfirst103 = True
                            i += 1 
                        if Cor_Rect10[3].collidepoint(event.pos):
                            dauhieuPfirst104 = True
                            i += 1 
                        if Cor_Rect10[4].collidepoint(event.pos):
                            dauhieuPfirst105 = True
                            i += 1 
                        if Cor_Rect10[5].collidepoint(event.pos):
                            dauhieuPfirst106 = True
                            i += 1 
                        if Cor_Rect10[6].collidepoint(event.pos):
                            dauhieuPfirst107 = True
                            i += 1 
                        if Cor_Rect10[7].collidepoint(event.pos):
                            dauhieuPfirst108 = True
                            i += 1 
                        if Cor_Rect10[8].collidepoint(event.pos):
                            dauhieuPfirst109 = True
                            i += 1 
                        if Cor_Rect10[9].collidepoint(event.pos):
                            dauhieuPfirst1010 = True
                            i += 1 
                        if Cor_Rect10[10].collidepoint(event.pos):
                            dauhieuPfirst1011 = True
                            i += 1 
                        if Cor_Rect10[11].collidepoint(event.pos):
                            dauhieuPfirst1012 = True
                            i += 1         
                        #hang 11
                        if Cor_Rect11[0].collidepoint(event.pos):
                            dauhieuPfirst111a = True
                            i += 1 
                        if Cor_Rect11[1].collidepoint(event.pos):
                            dauhieuPfirst112a = True
                            i += 1 
                        if Cor_Rect11[2].collidepoint(event.pos):
                            dauhieuPfirst113 = True
                            i += 1 
                        if Cor_Rect11[3].collidepoint(event.pos):
                            dauhieuPfirst114 = True
                            i += 1 
                        if Cor_Rect11[4].collidepoint(event.pos):
                            dauhieuPfirst115 = True
                            i += 1 
                        if Cor_Rect11[5].collidepoint(event.pos):
                            dauhieuPfirst116 = True
                            i += 1 
                        if Cor_Rect11[6].collidepoint(event.pos):
                            dauhieuPfirst117 = True
                            i += 1 
                        if Cor_Rect11[7].collidepoint(event.pos):
                            dauhieuPfirst118 = True
                            i += 1 
                        if Cor_Rect11[8].collidepoint(event.pos):
                            dauhieuPfirst119 = True
                            i += 1 
                        if Cor_Rect11[9].collidepoint(event.pos):
                            dauhieuPfirst1110 = True
                            i += 1 
                        if Cor_Rect11[10].collidepoint(event.pos):
                            dauhieuPfirst1111 = True
                            i += 1 
                        if Cor_Rect11[11].collidepoint(event.pos):
                            dauhieuPfirst1112 = True
                            i += 1 
                        #hang 12
                        if Cor_Rect12[0].collidepoint(event.pos):
                            dauhieuPfirst121 = True
                            i += 1 
                        if Cor_Rect12[1].collidepoint(event.pos):
                            dauhieuPfirst122 = True
                            i += 1 
                        if Cor_Rect12[2].collidepoint(event.pos):
                            dauhieuPfirst123 = True
                            i += 1 
                        if Cor_Rect12[3].collidepoint(event.pos):
                            dauhieuPfirst124 = True
                            i += 1 
                        if Cor_Rect12[4].collidepoint(event.pos):
                            dauhieuPfirst125 = True
                            i += 1 
                        if Cor_Rect12[5].collidepoint(event.pos):
                            dauhieuPfirst126 = True
                            i += 1 
                        if Cor_Rect12[6].collidepoint(event.pos):
                            dauhieuPfirst127 = True
                            i += 1 
                        if Cor_Rect12[7].collidepoint(event.pos):
                            dauhieuPfirst128 = True
                            i += 1 
                        if Cor_Rect12[8].collidepoint(event.pos):
                            dauhieuPfirst129 = True
                            i += 1 
                        if Cor_Rect12[9].collidepoint(event.pos):
                            dauhieuPfirst1210 = True
                            i += 1 
                        if Cor_Rect12[10].collidepoint(event.pos):
                            dauhieuPfirst1211 = True
                            i += 1 
                        if Cor_Rect12[11].collidepoint(event.pos):
                            dauhieuPfirst1212 = True
                            i += 1 

                        #Click the button lose
                        if button_lose_player1.collidepoint(event.pos):
                            print('')
                            print('P1 ACCEPTED TO LOSE')
                            run = False
                    else:
                    #hang 1
                        if Cor_Rect1[0].collidepoint(event.pos):
                            dauhieuPsecond11 = True    
                            i += 1 
                        if Cor_Rect1[1].collidepoint(event.pos):
                            dauhieuPsecond12 = True
                            i += 1 
                        if Cor_Rect1[2].collidepoint(event.pos):
                            dauhieuPsecond13 = True
                            i += 1 
                        if Cor_Rect1[3].collidepoint(event.pos):
                            dauhieuPsecond14 = True
                            i += 1 
                        if Cor_Rect1[4].collidepoint(event.pos):
                            dauhieuPsecond15 = True
                            i += 1 
                        if Cor_Rect1[5].collidepoint(event.pos):
                            dauhieuPsecond16 = True
                            i += 1 
                        if Cor_Rect1[6].collidepoint(event.pos):
                            dauhieuPsecond17 = True
                            i += 1 
                        if Cor_Rect1[7].collidepoint(event.pos):
                            dauhieuPsecond18 = True
                            i += 1 
                        if Cor_Rect1[8].collidepoint(event.pos):
                            dauhieuPsecond19 = True
                            i += 1 
                        if Cor_Rect1[9].collidepoint(event.pos):
                            dauhieuPsecond110 = True
                            i += 1 
                        if Cor_Rect1[10].collidepoint(event.pos):
                            dauhieuPsecond111 = True
                            i += 1 
                        if Cor_Rect1[11].collidepoint(event.pos):
                            dauhieuPsecond112 = True
                        #hang 2
                        if Cor_Rect2[0].collidepoint(event.pos):
                            dauhieuPsecond21 = True
                            i += 1 
                        if Cor_Rect2[1].collidepoint(event.pos):
                            dauhieuPsecond22 = True
                            i += 1 
                        if Cor_Rect2[2].collidepoint(event.pos):
                            dauhieuPsecond23 = True
                            i += 1 
                        if Cor_Rect2[3].collidepoint(event.pos):
                            dauhieuPsecond24 = True
                            i += 1 
                        if Cor_Rect2[4].collidepoint(event.pos):
                            dauhieuPsecond25 = True
                            i += 1 
                        if Cor_Rect2[5].collidepoint(event.pos):
                            dauhieuPsecond26 = True
                            i += 1 
                        if Cor_Rect2[6].collidepoint(event.pos):
                            dauhieuPsecond27 = True
                            i += 1 
                        if Cor_Rect2[7].collidepoint(event.pos):
                            dauhieuPsecond28 = True
                            i += 1 
                        if Cor_Rect2[8].collidepoint(event.pos):
                            dauhieuPsecond29 = True
                            i += 1 

                        if Cor_Rect2[9].collidepoint(event.pos):
                            dauhieuPsecond210 = True
                            i += 1 
                        if Cor_Rect2[10].collidepoint(event.pos):
                            dauhieuPsecond211 = True
                            i += 1 
                        if Cor_Rect2[11].collidepoint(event.pos):
                            dauhieuPsecond212 = True
                            i += 1 
                        #hang 3
                        if Cor_Rect3[0].collidepoint(event.pos):
                            dauhieuPsecond31 = True
                            i += 1 
                        if Cor_Rect3[1].collidepoint(event.pos):
                            dauhieuPsecond32 = True
                            i += 1 
                        if Cor_Rect3[2].collidepoint(event.pos):
                            dauhieuPsecond33 = True
                            i += 1 
                        if Cor_Rect3[3].collidepoint(event.pos):
                            dauhieuPsecond34 = True
                            i += 1 
                        if Cor_Rect3[4].collidepoint(event.pos):
                            dauhieuPsecond35 = True
                            i += 1 
                        if Cor_Rect3[5].collidepoint(event.pos):
                            dauhieuPsecond36 = True
                            i += 1 
                        if Cor_Rect3[6].collidepoint(event.pos):
                            dauhieuPsecond37 = True
                            i += 1 
                        if Cor_Rect3[7].collidepoint(event.pos):
                            dauhieuPsecond38 = True
                            i += 1 
                        if Cor_Rect3[8].collidepoint(event.pos):
                            dauhieuPsecond39 = True
                            i += 1 
                        if Cor_Rect3[9].collidepoint(event.pos):
                            dauhieuPsecond310 = True
                            i += 1 
                        if Cor_Rect3[10].collidepoint(event.pos):
                            dauhieuPsecond311 = True
                            i += 1 
                        if Cor_Rect3[11].collidepoint(event.pos):
                            dauhieuPsecond312 = True
                            i += 1 
                        #hang 4
                        if Cor_Rect4[0].collidepoint(event.pos):
                            dauhieuPsecond41 = True
                            i += 1 
                        if Cor_Rect4[1].collidepoint(event.pos):
                            dauhieuPsecond42 = True
                            i += 1 
                        if Cor_Rect4[2].collidepoint(event.pos):
                            dauhieuPsecond43 = True
                            i += 1 
                        if Cor_Rect4[3].collidepoint(event.pos):
                            dauhieuPsecond44 = True
                            i += 1 
                        if Cor_Rect4[4].collidepoint(event.pos):
                            dauhieuPsecond45 = True
                            i += 1 
                        if Cor_Rect4[5].collidepoint(event.pos):
                            dauhieuPsecond46 = True
                            i += 1 
                        if Cor_Rect4[6].collidepoint(event.pos):
                            dauhieuPsecond47 = True
                            i += 1 
                        if Cor_Rect4[7].collidepoint(event.pos):
                            dauhieuPsecond48 = True
                            i += 1 
                        if Cor_Rect4[8].collidepoint(event.pos):
                            dauhieuPsecond49 = True
                            i += 1 
                        if Cor_Rect4[9].collidepoint(event.pos):
                            dauhieuPsecond410 = True
                            i += 1 
                        if Cor_Rect4[10].collidepoint(event.pos):
                            dauhieuPsecond411 = True
                            i += 1 
                        if Cor_Rect4[11].collidepoint(event.pos):
                            dauhieuPsecond412 = True
                            i += 1 
                        #hang 5
                        if Cor_Rect5[0].collidepoint(event.pos):
                            dauhieuPsecond51 = True
                            i += 1 
                        if Cor_Rect5[1].collidepoint(event.pos):
                            dauhieuPsecond52 = True
                            i += 1 
                        if Cor_Rect5[2].collidepoint(event.pos):
                            dauhieuPsecond53 = True
                            i += 1 
                        if Cor_Rect5[3].collidepoint(event.pos):
                            dauhieuPsecond54 = True
                            i += 1 
                        if Cor_Rect5[4].collidepoint(event.pos):
                            dauhieuPsecond55 = True
                            i += 1 
                        if Cor_Rect5[5].collidepoint(event.pos):
                            dauhieuPsecond56 = True
                            i += 1 
                        if Cor_Rect5[6].collidepoint(event.pos):
                            dauhieuPsecond57 = True
                            i += 1 
                        if Cor_Rect5[7].collidepoint(event.pos):
                            dauhieuPsecond58 = True
                            i += 1 
                        if Cor_Rect5[8].collidepoint(event.pos):
                            dauhieuPsecond59 = True
                            i += 1 
                        if Cor_Rect5[9].collidepoint(event.pos):
                            dauhieuPsecond510 = True
                            i += 1 
                        if Cor_Rect5[10].collidepoint(event.pos):
                            dauhieuPsecond511 = True
                            i += 1 
                        if Cor_Rect5[11].collidepoint(event.pos):
                            dauhieuPsecond512 = True
                            i += 1 
                        #hang 6
                        if Cor_Rect6[0].collidepoint(event.pos):
                            dauhieuPsecond61 = True
                            i += 1 
                        if Cor_Rect6[1].collidepoint(event.pos):
                            dauhieuPsecond62 = True
                            i += 1 
                        if Cor_Rect6[2].collidepoint(event.pos):
                            dauhieuPsecond63 = True
                            i += 1 
                        if Cor_Rect6[3].collidepoint(event.pos):
                            dauhieuPsecond64 = True
                            i += 1 
                        if Cor_Rect6[4].collidepoint(event.pos):
                            dauhieuPsecond65 = True
                            i += 1 
                        if Cor_Rect6[5].collidepoint(event.pos):
                            dauhieuPsecond66 = True
                            i += 1 
                        if Cor_Rect6[6].collidepoint(event.pos):
                            dauhieuPsecond67 = True
                            i += 1 
                        if Cor_Rect6[7].collidepoint(event.pos):
                            dauhieuPsecond68 = True
                            i += 1 
                        if Cor_Rect6[8].collidepoint(event.pos):
                            dauhieuPsecond69 = True
                            i += 1 
                        if Cor_Rect6[9].collidepoint(event.pos):
                            dauhieuPsecond610 = True
                            i += 1 
                        if Cor_Rect6[10].collidepoint(event.pos):
                            dauhieuPsecond611 = True
                            i += 1 
                        if Cor_Rect6[11].collidepoint(event.pos):
                            dauhieuPsecond612 = True
                            i += 1 
                        #hang 7
                        if Cor_Rect7[0].collidepoint(event.pos):
                            dauhieuPsecond71 = True
                            i += 1 
                        if Cor_Rect7[1].collidepoint(event.pos):
                            dauhieuPsecond72 = True
                            i += 1 
                        if Cor_Rect7[2].collidepoint(event.pos):
                            dauhieuPsecond73 = True
                            i += 1 
                        if Cor_Rect7[3].collidepoint(event.pos):
                            dauhieuPsecond74 = True
                            i += 1 
                        if Cor_Rect7[4].collidepoint(event.pos):
                            dauhieuPsecond75 = True
                            i += 1 
                        if Cor_Rect7[5].collidepoint(event.pos):
                            dauhieuPsecond76 = True
                            i += 1          
                        if Cor_Rect7[6].collidepoint(event.pos):
                            dauhieuPsecond77 = True
                            i += 1 
                        if Cor_Rect7[7].collidepoint(event.pos):
                            dauhieuPsecond78 = True
                            i += 1 
                        if Cor_Rect7[8].collidepoint(event.pos):
                            dauhieuPsecond79 = True
                            i += 1 
                        if Cor_Rect7[9].collidepoint(event.pos):
                            dauhieuPsecond710 = True
                            i += 1 
                        if Cor_Rect7[10].collidepoint(event.pos):
                            dauhieuPsecond711 = True
                            i += 1 
                        if Cor_Rect7[11].collidepoint(event.pos):
                            dauhieuPsecond712 = True
                            i += 1 
                        #hang 8
                        if Cor_Rect8[0].collidepoint(event.pos):
                            dauhieuPsecond81 = True
                            i += 1 
                        if Cor_Rect8[1].collidepoint(event.pos):
                            dauhieuPsecond82 = True
                            i += 1 
                        if Cor_Rect8[2].collidepoint(event.pos):
                            dauhieuPsecond83 = True
                            i += 1 
                        if Cor_Rect8[3].collidepoint(event.pos):
                            dauhieuPsecond84 = True
                            i += 1 
                        if Cor_Rect8[4].collidepoint(event.pos):
                            dauhieuPsecond85 = True
                            i += 1 
                        if Cor_Rect8[5].collidepoint(event.pos):
                            dauhieuPsecond86 = True
                            i += 1 
                        if Cor_Rect8[6].collidepoint(event.pos):
                            dauhieuPsecond87 = True
                            i += 1 
                        if Cor_Rect8[7].collidepoint(event.pos):
                            dauhieuPsecond88 = True
                            i += 1 
                        if Cor_Rect8[8].collidepoint(event.pos):
                            dauhieuPsecond89 = True
                            i += 1 
                        if Cor_Rect8[9].collidepoint(event.pos):
                            dauhieuPsecond810 = True
                            i += 1 
                        if Cor_Rect8[10].collidepoint(event.pos):
                            dauhieuPsecond811 = True
                            i += 1 
                        if Cor_Rect8[11].collidepoint(event.pos):
                            dauhieuPsecond812 = True
                            i += 1 
                        #hang 9
                        if Cor_Rect9[0].collidepoint(event.pos):
                            dauhieuPsecond91 = True
                            i += 1 
                        if Cor_Rect9[1].collidepoint(event.pos):
                            dauhieuPsecond92 = True
                            i += 1 
                        if Cor_Rect9[2].collidepoint(event.pos):
                            dauhieuPsecond93 = True
                            i += 1 
                        if Cor_Rect9[3].collidepoint(event.pos):
                            dauhieuPsecond94 = True
                            i += 1 
                        if Cor_Rect9[4].collidepoint(event.pos):
                            dauhieuPsecond95 = True
                            i += 1 
                        if Cor_Rect9[5].collidepoint(event.pos):
                            dauhieuPsecond96 = True
                            i += 1 
                        if Cor_Rect9[6].collidepoint(event.pos):
                            dauhieuPsecond97 = True
                            i += 1 
                        if Cor_Rect9[7].collidepoint(event.pos):
                            dauhieuPsecond98 = True
                            i += 1 
                        if Cor_Rect9[8].collidepoint(event.pos):
                            dauhieuPsecond99 = True
                            i += 1 
                        if Cor_Rect9[9].collidepoint(event.pos):
                            dauhieuPsecond910 = True
                            i += 1 
                        if Cor_Rect9[10].collidepoint(event.pos):
                            dauhieuPsecond911 = True
                            i += 1 
                        if Cor_Rect9[11].collidepoint(event.pos):
                            dauhieuPsecond912 = True
                            i += 1 
                        #hang 10
                        if Cor_Rect10[0].collidepoint(event.pos):
                            dauhieuPsecond101 = True
                            i += 1 
                        if Cor_Rect10[1].collidepoint(event.pos):
                            dauhieuPsecond102 = True
                            i += 1 
                        if Cor_Rect10[2].collidepoint(event.pos):
                            dauhieuPsecond103 = True
                            i += 1 
                        if Cor_Rect10[3].collidepoint(event.pos):
                            dauhieuPsecond104 = True
                            i += 1 
                        if Cor_Rect10[4].collidepoint(event.pos):
                            dauhieuPsecond105 = True
                            i += 1 
                        if Cor_Rect10[5].collidepoint(event.pos):
                            dauhieuPsecond106 = True
                            i += 1 
                        if Cor_Rect10[6].collidepoint(event.pos):
                            dauhieuPsecond107 = True
                            i += 1 
                        if Cor_Rect10[7].collidepoint(event.pos):
                            dauhieuPsecond108 = True
                            i += 1 
                        if Cor_Rect10[8].collidepoint(event.pos):
                            dauhieuPsecond109 = True
                            i += 1 
                        if Cor_Rect10[9].collidepoint(event.pos):
                            dauhieuPsecond1010 = True
                            i += 1 
                        if Cor_Rect10[10].collidepoint(event.pos):
                            dauhieuPsecond1011 = True
                            i += 1 
                        if Cor_Rect10[11].collidepoint(event.pos):
                            dauhieuPsecond1012 = True
                            i += 1         
                        #hang 11
                        if Cor_Rect11[0].collidepoint(event.pos):
                            dauhieuPsecond111a = True
                            i += 1 
                        if Cor_Rect11[1].collidepoint(event.pos):
                            dauhieuPsecond112a = True
                            i += 1 
                        if Cor_Rect11[2].collidepoint(event.pos):
                            dauhieuPsecond113 = True
                            i += 1 
                        if Cor_Rect11[3].collidepoint(event.pos):
                            dauhieuPsecond114 = True
                            i += 1 
                        if Cor_Rect11[4].collidepoint(event.pos):
                            dauhieuPsecond115 = True
                            i += 1 
                        if Cor_Rect11[5].collidepoint(event.pos):
                            dauhieuPsecond116 = True
                            i += 1 
                        if Cor_Rect11[6].collidepoint(event.pos):
                            dauhieuPsecond117 = True
                            i += 1 
                        if Cor_Rect11[7].collidepoint(event.pos):
                            dauhieuPsecond118 = True
                            i += 1 
                        if Cor_Rect11[8].collidepoint(event.pos):
                            dauhieuPsecond119 = True
                            i += 1 
                        if Cor_Rect11[9].collidepoint(event.pos):
                            dauhieuPsecond1110 = True
                            i += 1 
                        if Cor_Rect11[10].collidepoint(event.pos):
                            dauhieuPsecond1111 = True
                            i += 1 
                        if Cor_Rect11[11].collidepoint(event.pos):
                            dauhieuPsecond1112 = True
                            i += 1 
                        #hang 12
                        if Cor_Rect12[0].collidepoint(event.pos):
                            dauhieuPsecond121 = True
                            i += 1 
                        if Cor_Rect12[1].collidepoint(event.pos):
                            dauhieuPsecond122 = True
                            i += 1 
                        if Cor_Rect12[2].collidepoint(event.pos):
                            dauhieuPsecond123 = True
                            i += 1 
                        if Cor_Rect12[3].collidepoint(event.pos):
                            dauhieuPsecond124 = True
                            i += 1 
                        if Cor_Rect12[4].collidepoint(event.pos):
                            dauhieuPsecond125 = True
                            i += 1 
                        if Cor_Rect12[5].collidepoint(event.pos):
                            dauhieuPsecond126 = True
                            i += 1 
                        if Cor_Rect12[6].collidepoint(event.pos):
                            dauhieuPsecond127 = True
                            i += 1 
                        if Cor_Rect12[7].collidepoint(event.pos):
                            dauhieuPsecond128 = True
                            i += 1 
                        if Cor_Rect12[8].collidepoint(event.pos):
                            dauhieuPsecond129 = True
                            i += 1 
                        if Cor_Rect12[9].collidepoint(event.pos):
                            dauhieuPsecond1210 = True
                            i += 1 
                        if Cor_Rect12[10].collidepoint(event.pos):
                            dauhieuPsecond1211 = True
                            i += 1 
                        if Cor_Rect12[11].collidepoint(event.pos):
                            dauhieuPsecond1212 = True
                            i += 1 
                    
                        #Click the button lose
                        if button_lose_player2.collidepoint(event.pos):
                            print('')
                            print('P2 ACCEPTED TO LOSE')
                            run = False
                    
                    if draw_button.collidepoint(event.pos):
                        print('')
                        print('DRAW')
                        run = False

                    
        

        mx,my=pygame.mouse.get_pos()
        # print(mx,my)
        
        
        draw(mx,my)
        # playing()

        for cor_rect in Cor_Rect:
            if cor_rect.x <= mx <= (cor_rect.x + cor_rect.width) and cor_rect.y <= my <= (cor_rect.y + cor_rect.height):
                cor_rect_fill = pygame.Rect(cor_rect.x +2, cor_rect.y +2,cor_rect.width-2, cor_rect.height-4)
                WIN.fill((245, 174, 108),cor_rect_fill)
        
        if True: 

            ###########
            if dauhieuPfirst11 == True:
                WIN.blit(markP1,Mark_rect[0])

                grid[0][0] = 'X'
                

            if dauhieuPfirst12 == True:
                WIN.blit(markP1,Mark_rect[1])
                grid[0][1] = 'X'

            if dauhieuPfirst13 == True:
                WIN.blit(markP1,Mark_rect[2])
                grid[0][2] = 'X'

            if dauhieuPfirst14 == True:
                WIN.blit(markP1,Mark_rect[3])
                grid[0][3] = 'X'

            if dauhieuPfirst15 == True:
                WIN.blit(markP1,Mark_rect[4])
                grid[0][4] = 'X'

            if dauhieuPfirst16 == True:
                WIN.blit(markP1,Mark_rect[5])
                grid[0][5] = 'X'

            if dauhieuPfirst17 == True:
                WIN.blit(markP1,Mark_rect[6])
                grid[0][6] = 'X'

            if dauhieuPfirst18 == True:
                WIN.blit(markP1,Mark_rect[7])
                grid[0][7] = 'X'

            if dauhieuPfirst19 == True:
                WIN.blit(markP1,Mark_rect[8])
                grid[0][8] = 'X'

            if dauhieuPfirst110 == True:
                WIN.blit(markP1,Mark_rect[9])
                grid[0][9] = 'X'

            if dauhieuPfirst111 == True:
                WIN.blit(markP1,Mark_rect[10])
                grid[0][10] = 'X'

            if dauhieuPfirst112 == True:
                WIN.blit(markP1,Mark_rect[11])
                grid[0][11] = 'X'
            #############
            if dauhieuPfirst21 == True:
                WIN.blit(markP1,Mark_rect[12])
                grid[1][0] = 'X'

            if dauhieuPfirst22 == True:
                WIN.blit(markP1,Mark_rect[13])
                grid[1][1] = 'X'

            if dauhieuPfirst23 == True:
                WIN.blit(markP1,Mark_rect[14])
                grid[1][2] = 'X'

            if dauhieuPfirst24 == True:
                WIN.blit(markP1,Mark_rect[15])
                grid[1][3] = 'X'

            if dauhieuPfirst25 == True:
                WIN.blit(markP1,Mark_rect[16])
                grid[1][4] = 'X'

            if dauhieuPfirst26 == True:
                WIN.blit(markP1,Mark_rect[17])
                grid[1][5] = 'X'

            if dauhieuPfirst27 == True:
                WIN.blit(markP1,Mark_rect[18])
                grid[1][6] = 'X'

            if dauhieuPfirst28 == True:
                WIN.blit(markP1,Mark_rect[19])
                grid[1][7] = 'X'

            if dauhieuPfirst29 == True:
                WIN.blit(markP1,Mark_rect[20])
                grid[1][8] = 'X'

            if dauhieuPfirst210 == True:
                WIN.blit(markP1,Mark_rect[21])
                grid[1][9] = 'X'

            if dauhieuPfirst211 == True:
                WIN.blit(markP1,Mark_rect[22])
                grid[1][10] = 'X'

            if dauhieuPfirst212 == True:
                WIN.blit(markP1,Mark_rect[23])
                grid[1][11] = 'X'

            #############
            if dauhieuPfirst31 == True:
                WIN.blit(markP1,Mark_rect[24])
                grid[2][0] = 'X'

            if dauhieuPfirst32 == True:
                WIN.blit(markP1,Mark_rect[25])
                grid[2][1] = 'X'

            if dauhieuPfirst33 == True:
                WIN.blit(markP1,Mark_rect[26])
                grid[2][2] = 'X'

            if dauhieuPfirst34 == True:
                WIN.blit(markP1,Mark_rect[27])
                grid[2][3] = 'X'

            if dauhieuPfirst35 == True:
                WIN.blit(markP1,Mark_rect[28])
                grid[2][4] = 'X'

            if dauhieuPfirst36 == True:
                WIN.blit(markP1,Mark_rect[29])
                grid[2][5] = 'X'

            if dauhieuPfirst37 == True:
                WIN.blit(markP1,Mark_rect[30])
                grid[2][6] = 'X'

            if dauhieuPfirst38 == True:
                WIN.blit(markP1,Mark_rect[31])
                grid[2][7] = 'X'

            if dauhieuPfirst39 == True:
                WIN.blit(markP1,Mark_rect[32])
                grid[2][8] = 'X'

            if dauhieuPfirst310 == True:
                WIN.blit(markP1,Mark_rect[33])
                grid[2][9] = 'X'

            if dauhieuPfirst311 == True:
                WIN.blit(markP1,Mark_rect[34])
                grid[2][10] = 'X'

            if dauhieuPfirst312 == True:
                WIN.blit(markP1,Mark_rect[35])
                grid[2][11] = 'X'
            
            #############
            if dauhieuPfirst41 == True:
                WIN.blit(markP1,Mark_rect[36])
                grid[3][0] = 'X'

            if dauhieuPfirst42 == True:
                WIN.blit(markP1,Mark_rect[37])
                grid[3][1] = 'X'

            if dauhieuPfirst43 == True:
                WIN.blit(markP1,Mark_rect[38])
                grid[3][2] = 'X'

            if dauhieuPfirst44 == True:
                WIN.blit(markP1,Mark_rect[39])
                grid[3][3] = 'X'

            if dauhieuPfirst45 == True:
                WIN.blit(markP1,Mark_rect[40])
                grid[3][4] = 'X'

            if dauhieuPfirst46 == True:
                WIN.blit(markP1,Mark_rect[41])
                grid[3][5] = 'X'

            if dauhieuPfirst47 == True:
                WIN.blit(markP1,Mark_rect[42])
                grid[3][6] = 'X'

            if dauhieuPfirst48 == True:
                WIN.blit(markP1,Mark_rect[43])
                grid[3][7] = 'X'

            if dauhieuPfirst49 == True:
                WIN.blit(markP1,Mark_rect[44])
                grid[3][8] = 'X'

            if dauhieuPfirst410 == True:
                WIN.blit(markP1,Mark_rect[45])
                grid[3][9] = 'X'

            if dauhieuPfirst411 == True:
                WIN.blit(markP1,Mark_rect[46])
                grid[3][10] = 'X'

            if dauhieuPfirst412 == True:
                WIN.blit(markP1,Mark_rect[47])
                grid[3][11] = 'X'

            #############
            if dauhieuPfirst51 == True:
                WIN.blit(markP1,Mark_rect[48])
                grid[4][0] = 'X'

            if dauhieuPfirst52 == True:
                WIN.blit(markP1,Mark_rect[49])
                grid[4][1] = 'X'

            if dauhieuPfirst53 == True:
                WIN.blit(markP1,Mark_rect[50])
                grid[4][2] = 'X'

            if dauhieuPfirst54 == True:
                WIN.blit(markP1,Mark_rect[51])
                grid[4][3] = 'X'

            if dauhieuPfirst55 == True:
                WIN.blit(markP1,Mark_rect[52])
                grid[4][4] = 'X'

            if dauhieuPfirst56 == True:
                WIN.blit(markP1,Mark_rect[53])
                grid[4][5] = 'X'

            if dauhieuPfirst57 == True:
                WIN.blit(markP1,Mark_rect[54])
                grid[4][6] = 'X'

            if dauhieuPfirst58 == True:
                WIN.blit(markP1,Mark_rect[55])
                grid[4][7] = 'X'

            if dauhieuPfirst59 == True:
                WIN.blit(markP1,Mark_rect[56])
                grid[4][8] = 'X'

            if dauhieuPfirst510 == True:
                WIN.blit(markP1,Mark_rect[57])
                grid[4][9] = 'X'

            if dauhieuPfirst511 == True:
                WIN.blit(markP1,Mark_rect[58])
                grid[4][10] = 'X'

            if dauhieuPfirst512 == True:
                WIN.blit(markP1,Mark_rect[59])
                grid[4][11] = 'X'
            #############
            if dauhieuPfirst61 == True:
                WIN.blit(markP1,Mark_rect[60])
                grid[5][0] = 'X'

            if dauhieuPfirst62 == True:
                WIN.blit(markP1,Mark_rect[61])
                grid[5][1] = 'X'

            if dauhieuPfirst63 == True:
                WIN.blit(markP1,Mark_rect[62])
                grid[5][2] = 'X'

            if dauhieuPfirst64 == True:
                WIN.blit(markP1,Mark_rect[63])
                grid[5][3] = 'X'

            if dauhieuPfirst65 == True:
                WIN.blit(markP1,Mark_rect[64])
                grid[5][4] = 'X'

            if dauhieuPfirst66 == True:
                WIN.blit(markP1,Mark_rect[65])
                grid[5][5] = 'X'

            if dauhieuPfirst67 == True:
                WIN.blit(markP1,Mark_rect[66])
                grid[5][6] = 'X'

            if dauhieuPfirst68 == True:
                WIN.blit(markP1,Mark_rect[67])
                grid[5][7] = 'X'

            if dauhieuPfirst69 == True:
                WIN.blit(markP1,Mark_rect[68])
                grid[5][8] = 'X'

            if dauhieuPfirst610 == True:
                WIN.blit(markP1,Mark_rect[69])
                grid[5][9] = 'X'

            if dauhieuPfirst611 == True:
                WIN.blit(markP1,Mark_rect[70])
                grid[5][10] = 'X'

            if dauhieuPfirst612 == True:
                WIN.blit(markP1,Mark_rect[71])
                grid[5][11] = 'X'
            ###########
            if dauhieuPfirst71 == True:
                WIN.blit(markP1,Mark_rect[72])
                grid[6][0] = 'X'

            if dauhieuPfirst72 == True:
                WIN.blit(markP1,Mark_rect[73])
                grid[6][1] = 'X'

            if dauhieuPfirst73 == True:
                WIN.blit(markP1,Mark_rect[74])
                grid[6][2] = 'X'

            if dauhieuPfirst74 == True:
                WIN.blit(markP1,Mark_rect[75])
                grid[6][3] = 'X'

            if dauhieuPfirst75 == True:
                WIN.blit(markP1,Mark_rect[76])
                grid[6][4] = 'X'

            if dauhieuPfirst76 == True:
                WIN.blit(markP1,Mark_rect[77])
                grid[6][5] = 'X'

            if dauhieuPfirst77 == True:
                WIN.blit(markP1,Mark_rect[78])
                grid[6][6] = 'X'

            if dauhieuPfirst78 == True:
                WIN.blit(markP1,Mark_rect[79])
                grid[6][7] = 'X'

            if dauhieuPfirst79 == True:
                WIN.blit(markP1,Mark_rect[80])
                grid[6][8] = 'X'

            if dauhieuPfirst710 == True:
                WIN.blit(markP1,Mark_rect[81])
                grid[6][9] = 'X'

            if dauhieuPfirst711 == True:
                WIN.blit(markP1,Mark_rect[82])
                grid[6][10] = 'X'

            if dauhieuPfirst712 == True:
                WIN.blit(markP1,Mark_rect[83])
                grid[6][11] = 'X'
            #############
            if dauhieuPfirst81 == True:
                WIN.blit(markP1,Mark_rect[84])
                grid[7][0] = 'X'

            if dauhieuPfirst82 == True:
                WIN.blit(markP1,Mark_rect[85])
                grid[7][1] = 'X'

            if dauhieuPfirst83 == True:
                WIN.blit(markP1,Mark_rect[86])
                grid[7][2] = 'X'

            if dauhieuPfirst84 == True:
                WIN.blit(markP1,Mark_rect[87])
                grid[7][3] = 'X'

            if dauhieuPfirst85 == True:
                WIN.blit(markP1,Mark_rect[88])
                grid[7][4] = 'X'

            if dauhieuPfirst86 == True:
                WIN.blit(markP1,Mark_rect[89])
                grid[7][5] = 'X'

            if dauhieuPfirst87 == True:
                WIN.blit(markP1,Mark_rect[90])
                grid[7][6] = 'X'

            if dauhieuPfirst88 == True:
                WIN.blit(markP1,Mark_rect[91])
                grid[7][7] = 'X'

            if dauhieuPfirst89 == True:
                WIN.blit(markP1,Mark_rect[92])
                grid[7][8] = 'X'

            if dauhieuPfirst810 == True:
                WIN.blit(markP1,Mark_rect[93])
                grid[7][9] = 'X'

            if dauhieuPfirst811 == True:
                WIN.blit(markP1,Mark_rect[94])
                grid[7][10] = 'X'

            if dauhieuPfirst812 == True:
                WIN.blit(markP1,Mark_rect[95])
                grid[7][11] = 'X'

            #############
            if dauhieuPfirst91 == True:
                WIN.blit(markP1,Mark_rect[96])
                grid[8][0] = 'X'

            if dauhieuPfirst92 == True:
                WIN.blit(markP1,Mark_rect[97])
                grid[8][1] = 'X'

            if dauhieuPfirst93 == True:
                WIN.blit(markP1,Mark_rect[98])
                grid[8][2] = 'X'

            if dauhieuPfirst94 == True:
                WIN.blit(markP1,Mark_rect[99])
                grid[8][3] = 'X'

            if dauhieuPfirst95 == True:
                WIN.blit(markP1,Mark_rect[100])
                grid[8][4] = 'X'

            if dauhieuPfirst96 == True:
                WIN.blit(markP1,Mark_rect[101])
                grid[8][5] = 'X'

            if dauhieuPfirst97 == True:
                WIN.blit(markP1,Mark_rect[102])
                grid[8][6] = 'X'

            if dauhieuPfirst98 == True:
                WIN.blit(markP1,Mark_rect[103])
                grid[8][7] = 'X'

            if dauhieuPfirst99 == True:
                WIN.blit(markP1,Mark_rect[104])
                grid[8][8] = 'X'

            if dauhieuPfirst910 == True:
                WIN.blit(markP1,Mark_rect[105])
                grid[8][9] = 'X'

            if dauhieuPfirst911 == True:
                WIN.blit(markP1,Mark_rect[106])
                grid[8][10] = 'X'

            if dauhieuPfirst912 == True:
                WIN.blit(markP1,Mark_rect[107])
                grid[8][11] = 'X'
            
            #############
            if dauhieuPfirst101 == True:
                WIN.blit(markP1,Mark_rect[108])
                grid[9][0] = 'X'

            if dauhieuPfirst102 == True:
                WIN.blit(markP1,Mark_rect[109])
                grid[9][1] = 'X'

            if dauhieuPfirst103 == True:
                WIN.blit(markP1,Mark_rect[110])
                grid[9][2] = 'X'

            if dauhieuPfirst104 == True:
                WIN.blit(markP1,Mark_rect[111])
                grid[9][3] = 'X'

            if dauhieuPfirst105 == True:
                WIN.blit(markP1,Mark_rect[112])
                grid[9][4] = 'X'

            if dauhieuPfirst106 == True:
                WIN.blit(markP1,Mark_rect[113])
                grid[9][5] = 'X'

            if dauhieuPfirst107 == True:
                WIN.blit(markP1,Mark_rect[114])
                grid[9][6] = 'X'

            if dauhieuPfirst108 == True:
                WIN.blit(markP1,Mark_rect[115])
                grid[9][7] = 'X'

            if dauhieuPfirst109 == True:
                WIN.blit(markP1,Mark_rect[116])
                grid[9][8] = 'X'

            if dauhieuPfirst1010 == True:
                WIN.blit(markP1,Mark_rect[117])
                grid[9][9] = 'X'

            if dauhieuPfirst1011 == True:
                WIN.blit(markP1,Mark_rect[118])
                grid[9][10] = 'X'

            if dauhieuPfirst1012 == True:
                WIN.blit(markP1,Mark_rect[119])
                grid[9][11] = 'X'

            #############
            if dauhieuPfirst111a == True:
                WIN.blit(markP1,Mark_rect[120])
                grid[10][0] = 'X'

            if dauhieuPfirst112a == True:
                WIN.blit(markP1,Mark_rect[121])
                grid[10][1] = 'X'

            if dauhieuPfirst113 == True:
                WIN.blit(markP1,Mark_rect[122])
                grid[10][2] = 'X'

            if dauhieuPfirst114 == True:
                WIN.blit(markP1,Mark_rect[123])
                grid[10][3] = 'X'

            if dauhieuPfirst115 == True:
                WIN.blit(markP1,Mark_rect[124])
                grid[10][4] = 'X'

            if dauhieuPfirst116 == True:
                WIN.blit(markP1,Mark_rect[125])
                grid[10][5] = 'X'

            if dauhieuPfirst117 == True:
                WIN.blit(markP1,Mark_rect[126])
                grid[10][6] = 'X'

            if dauhieuPfirst118 == True:
                WIN.blit(markP1,Mark_rect[127])
                grid[10][7] = 'X'

            if dauhieuPfirst119 == True:
                WIN.blit(markP1,Mark_rect[128])
                grid[10][8] = 'X'

            if dauhieuPfirst1110 == True:
                WIN.blit(markP1,Mark_rect[129])
                grid[10][9] = 'X'

            if dauhieuPfirst1111 == True:
                WIN.blit(markP1,Mark_rect[130])
                grid[10][10] = 'X'

            if dauhieuPfirst1112 == True:
                WIN.blit(markP1,Mark_rect[131])
                grid[10][11] = 'X'
            #############
            if dauhieuPfirst121 == True:
                WIN.blit(markP1,Mark_rect[132])
                grid[11][0] = 'X'

            if dauhieuPfirst122 == True:
                WIN.blit(markP1,Mark_rect[133])
                grid[11][1] = 'X'

            if dauhieuPfirst123 == True:
                WIN.blit(markP1,Mark_rect[134])
                grid[11][2] = 'X'

            if dauhieuPfirst124 == True:
                WIN.blit(markP1,Mark_rect[135])
                grid[11][3] = 'X'

            if dauhieuPfirst125 == True:
                WIN.blit(markP1,Mark_rect[136])
                grid[11][4] = 'X'

            if dauhieuPfirst126 == True:
                WIN.blit(markP1,Mark_rect[137])
                grid[11][5] = 'X'

            if dauhieuPfirst127 == True:
                WIN.blit(markP1,Mark_rect[138])
                grid[11][6] = 'X'

            if dauhieuPfirst128 == True:
                WIN.blit(markP1,Mark_rect[139])
                grid[11][7] = 'X'

            if dauhieuPfirst129 == True:
                WIN.blit(markP1,Mark_rect[140])
                grid[11][8] = 'X'

            if dauhieuPfirst1210 == True:
                WIN.blit(markP1,Mark_rect[141])
                grid[11][9] = 'X'

            if dauhieuPfirst1211 == True:
                WIN.blit(markP1,Mark_rect[142])
                grid[11][10] = 'X'

            if dauhieuPfirst1212 == True:
                WIN.blit(markP1,Mark_rect[143])
                grid[11][11] = 'X'




        if True: 

            ###########
            if dauhieuPsecond11 == True:
                WIN.blit(markP2,Mark_rect[0])

                grid[0][0] = 'O'
                

            if dauhieuPsecond12 == True:
                WIN.blit(markP2,Mark_rect[1])
                grid[0][1] = 'O'

            if dauhieuPsecond13 == True:
                WIN.blit(markP2,Mark_rect[2])
                grid[0][2] = 'O'

            if dauhieuPsecond14 == True:
                WIN.blit(markP2,Mark_rect[3])
                grid[0][3] = 'O'

            if dauhieuPsecond15 == True:
                WIN.blit(markP2,Mark_rect[4])
                grid[0][4] = 'O'

            if dauhieuPsecond16 == True:
                WIN.blit(markP2,Mark_rect[5])
                grid[0][5] = 'O'

            if dauhieuPsecond17 == True:
                WIN.blit(markP2,Mark_rect[6])
                grid[0][6] = 'O'

            if dauhieuPsecond18 == True:
                WIN.blit(markP2,Mark_rect[7])
                grid[0][7] = 'O'

            if dauhieuPsecond19 == True:
                WIN.blit(markP2,Mark_rect[8])
                grid[0][8] = 'O'

            if dauhieuPsecond110 == True:
                WIN.blit(markP2,Mark_rect[9])
                grid[0][9] = 'O'

            if dauhieuPsecond111 == True:
                WIN.blit(markP2,Mark_rect[10])
                grid[0][10] = 'O'

            if dauhieuPsecond112 == True:
                WIN.blit(markP2,Mark_rect[11])
                grid[0][11] = 'O'
            #############
            if dauhieuPsecond21 == True:
                WIN.blit(markP2,Mark_rect[12])
                grid[1][0] = 'O'

            if dauhieuPsecond22 == True:
                WIN.blit(markP2,Mark_rect[13])
                grid[1][1] = 'O'

            if dauhieuPsecond23 == True:
                WIN.blit(markP2,Mark_rect[14])
                grid[1][2] = 'O'

            if dauhieuPsecond24 == True:
                WIN.blit(markP2,Mark_rect[15])
                grid[1][3] = 'O'

            if dauhieuPsecond25 == True:
                WIN.blit(markP2,Mark_rect[16])
                grid[1][4] = 'O'

            if dauhieuPsecond26 == True:
                WIN.blit(markP2,Mark_rect[17])
                grid[1][5] = 'O'

            if dauhieuPsecond27 == True:
                WIN.blit(markP2,Mark_rect[18])
                grid[1][6] = 'O'

            if dauhieuPsecond28 == True:
                WIN.blit(markP2,Mark_rect[19])
                grid[1][7] = 'O'

            if dauhieuPsecond29 == True:
                WIN.blit(markP2,Mark_rect[20])
                grid[1][8] = 'O'

            if dauhieuPsecond210 == True:
                WIN.blit(markP2,Mark_rect[21])
                grid[1][9] = 'O'

            if dauhieuPsecond211 == True:
                WIN.blit(markP2,Mark_rect[22])
                grid[1][10] = 'O'

            if dauhieuPsecond212 == True:
                WIN.blit(markP2,Mark_rect[23])
                grid[1][11] = 'O'

            #############
            if dauhieuPsecond31 == True:
                WIN.blit(markP2,Mark_rect[24])
                grid[2][0] = 'O'

            if dauhieuPsecond32 == True:
                WIN.blit(markP2,Mark_rect[25])
                grid[2][1] = 'O'

            if dauhieuPsecond33 == True:
                WIN.blit(markP2,Mark_rect[26])
                grid[2][2] = 'O'

            if dauhieuPsecond34 == True:
                WIN.blit(markP2,Mark_rect[27])
                grid[2][3] = 'O'

            if dauhieuPsecond35 == True:
                WIN.blit(markP2,Mark_rect[28])
                grid[2][4] = 'O'

            if dauhieuPsecond36 == True:
                WIN.blit(markP2,Mark_rect[29])
                grid[2][5] = 'O'

            if dauhieuPsecond37 == True:
                WIN.blit(markP2,Mark_rect[30])
                grid[2][6] = 'O'

            if dauhieuPsecond38 == True:
                WIN.blit(markP2,Mark_rect[31])
                grid[2][7] = 'O'

            if dauhieuPsecond39 == True:
                WIN.blit(markP2,Mark_rect[32])
                grid[2][8] = 'O'

            if dauhieuPsecond310 == True:
                WIN.blit(markP2,Mark_rect[33])
                grid[2][9] = 'O'

            if dauhieuPsecond311 == True:
                WIN.blit(markP2,Mark_rect[34])
                grid[2][10] = 'O'

            if dauhieuPsecond312 == True:
                WIN.blit(markP2,Mark_rect[35])
                grid[2][11] = 'O'
            
            #############
            if dauhieuPsecond41 == True:
                WIN.blit(markP2,Mark_rect[36])
                grid[3][0] = 'O'

            if dauhieuPsecond42 == True:
                WIN.blit(markP2,Mark_rect[37])
                grid[3][1] = 'O'

            if dauhieuPsecond43 == True:
                WIN.blit(markP2,Mark_rect[38])
                grid[3][2] = 'O'

            if dauhieuPsecond44 == True:
                WIN.blit(markP2,Mark_rect[39])
                grid[3][3] = 'O'

            if dauhieuPsecond45 == True:
                WIN.blit(markP2,Mark_rect[40])
                grid[3][4] = 'O'

            if dauhieuPsecond46 == True:
                WIN.blit(markP2,Mark_rect[41])
                grid[3][5] = 'O'

            if dauhieuPsecond47 == True:
                WIN.blit(markP2,Mark_rect[42])
                grid[3][6] = 'O'

            if dauhieuPsecond48 == True:
                WIN.blit(markP2,Mark_rect[43])
                grid[3][7] = 'O'

            if dauhieuPsecond49 == True:
                WIN.blit(markP2,Mark_rect[44])
                grid[3][8] = 'O'

            if dauhieuPsecond410 == True:
                WIN.blit(markP2,Mark_rect[45])
                grid[3][9] = 'O'

            if dauhieuPsecond411 == True:
                WIN.blit(markP2,Mark_rect[46])
                grid[3][10] = 'O'

            if dauhieuPsecond412 == True:
                WIN.blit(markP2,Mark_rect[47])
                grid[3][11] = 'O'

            #############
            if dauhieuPsecond51 == True:
                WIN.blit(markP2,Mark_rect[48])
                grid[4][0] = 'O'

            if dauhieuPsecond52 == True:
                WIN.blit(markP2,Mark_rect[49])
                grid[4][1] = 'O'

            if dauhieuPsecond53 == True:
                WIN.blit(markP2,Mark_rect[50])
                grid[4][2] = 'O'

            if dauhieuPsecond54 == True:
                WIN.blit(markP2,Mark_rect[51])
                grid[4][3] = 'O'

            if dauhieuPsecond55 == True:
                WIN.blit(markP2,Mark_rect[52])
                grid[4][4] = 'O'

            if dauhieuPsecond56 == True:
                WIN.blit(markP2,Mark_rect[53])
                grid[4][5] = 'O'

            if dauhieuPsecond57 == True:
                WIN.blit(markP2,Mark_rect[54])
                grid[4][6] = 'O'

            if dauhieuPsecond58 == True:
                WIN.blit(markP2,Mark_rect[55])
                grid[4][7] = 'O'

            if dauhieuPsecond59 == True:
                WIN.blit(markP2,Mark_rect[56])
                grid[4][8] = 'O'

            if dauhieuPsecond510 == True:
                WIN.blit(markP2,Mark_rect[57])
                grid[4][9] = 'O'

            if dauhieuPsecond511 == True:
                WIN.blit(markP2,Mark_rect[58])
                grid[4][10] = 'O'

            if dauhieuPsecond512 == True:
                WIN.blit(markP2,Mark_rect[59])
                grid[4][11] = 'O'
            #############
            if dauhieuPsecond61 == True:
                WIN.blit(markP2,Mark_rect[60])
                grid[5][0] = 'O'

            if dauhieuPsecond62 == True:
                WIN.blit(markP2,Mark_rect[61])
                grid[5][1] = 'O'

            if dauhieuPsecond63 == True:
                WIN.blit(markP2,Mark_rect[62])
                grid[5][2] = 'O'

            if dauhieuPsecond64 == True:
                WIN.blit(markP2,Mark_rect[63])
                grid[5][3] = 'O'

            if dauhieuPsecond65 == True:
                WIN.blit(markP2,Mark_rect[64])
                grid[5][4] = 'O'

            if dauhieuPsecond66 == True:
                WIN.blit(markP2,Mark_rect[65])
                grid[5][5] = 'O'

            if dauhieuPsecond67 == True:
                WIN.blit(markP2,Mark_rect[66])
                grid[5][6] = 'O'

            if dauhieuPsecond68 == True:
                WIN.blit(markP2,Mark_rect[67])
                grid[5][7] = 'O'

            if dauhieuPsecond69 == True:
                WIN.blit(markP2,Mark_rect[68])
                grid[5][8] = 'O'

            if dauhieuPsecond610 == True:
                WIN.blit(markP2,Mark_rect[69])
                grid[5][9] = 'O'

            if dauhieuPsecond611 == True:
                WIN.blit(markP2,Mark_rect[70])
                grid[5][10] = 'O'

            if dauhieuPsecond612 == True:
                WIN.blit(markP2,Mark_rect[71])
                grid[5][11] = 'O'
            ###########
            if dauhieuPsecond71 == True:
                WIN.blit(markP2,Mark_rect[72])
                grid[6][0] = 'O'

            if dauhieuPsecond72 == True:
                WIN.blit(markP2,Mark_rect[73])
                grid[6][1] = 'O'

            if dauhieuPsecond73 == True:
                WIN.blit(markP2,Mark_rect[74])
                grid[6][2] = 'O'

            if dauhieuPsecond74 == True:
                WIN.blit(markP2,Mark_rect[75])
                grid[6][3] = 'O'

            if dauhieuPsecond75 == True:
                WIN.blit(markP2,Mark_rect[76])
                grid[6][4] = 'O'

            if dauhieuPsecond76 == True:
                WIN.blit(markP2,Mark_rect[77])
                grid[6][5] = 'O'

            if dauhieuPsecond77 == True:
                WIN.blit(markP2,Mark_rect[78])
                grid[6][6] = 'O'

            if dauhieuPsecond78 == True:
                WIN.blit(markP2,Mark_rect[79])
                grid[6][7] = 'O'

            if dauhieuPsecond79 == True:
                WIN.blit(markP2,Mark_rect[80])
                grid[6][8] = 'O'

            if dauhieuPsecond710 == True:
                WIN.blit(markP2,Mark_rect[81])
                grid[6][9] = 'O'

            if dauhieuPsecond711 == True:
                WIN.blit(markP2,Mark_rect[82])
                grid[6][10] = 'O'

            if dauhieuPsecond712 == True:
                WIN.blit(markP2,Mark_rect[83])
                grid[6][11] = 'O'
            #############
            if dauhieuPsecond81 == True:
                WIN.blit(markP2,Mark_rect[84])
                grid[7][0] = 'O'

            if dauhieuPsecond82 == True:
                WIN.blit(markP2,Mark_rect[85])
                grid[7][1] = 'O'

            if dauhieuPsecond83 == True:
                WIN.blit(markP2,Mark_rect[86])
                grid[7][2] = 'O'

            if dauhieuPsecond84 == True:
                WIN.blit(markP2,Mark_rect[87])
                grid[7][3] = 'O'

            if dauhieuPsecond85 == True:
                WIN.blit(markP2,Mark_rect[88])
                grid[7][4] = 'O'

            if dauhieuPsecond86 == True:
                WIN.blit(markP2,Mark_rect[89])
                grid[7][5] = 'O'

            if dauhieuPsecond87 == True:
                WIN.blit(markP2,Mark_rect[90])
                grid[7][6] = 'O'

            if dauhieuPsecond88 == True:
                WIN.blit(markP2,Mark_rect[91])
                grid[7][7] = 'O'

            if dauhieuPsecond89 == True:
                WIN.blit(markP2,Mark_rect[92])
                grid[7][8] = 'O'

            if dauhieuPsecond810 == True:
                WIN.blit(markP2,Mark_rect[93])
                grid[7][9] = 'O'

            if dauhieuPsecond811 == True:
                WIN.blit(markP2,Mark_rect[94])
                grid[7][10] = 'O'

            if dauhieuPsecond812 == True:
                WIN.blit(markP2,Mark_rect[95])
                grid[7][11] = 'O'

            #############
            if dauhieuPsecond91 == True:
                WIN.blit(markP2,Mark_rect[96])
                grid[8][0] = 'O'

            if dauhieuPsecond92 == True:
                WIN.blit(markP2,Mark_rect[97])
                grid[8][1] = 'O'

            if dauhieuPsecond93 == True:
                WIN.blit(markP2,Mark_rect[98])
                grid[8][2] = 'O'

            if dauhieuPsecond94 == True:
                WIN.blit(markP2,Mark_rect[99])
                grid[8][3] = 'O'

            if dauhieuPsecond95 == True:
                WIN.blit(markP2,Mark_rect[100])
                grid[8][4] = 'O'

            if dauhieuPsecond96 == True:
                WIN.blit(markP2,Mark_rect[101])
                grid[8][5] = 'O'

            if dauhieuPsecond97 == True:
                WIN.blit(markP2,Mark_rect[102])
                grid[8][6] = 'O'

            if dauhieuPsecond98 == True:
                WIN.blit(markP2,Mark_rect[103])
                grid[8][7] = 'O'

            if dauhieuPsecond99 == True:
                WIN.blit(markP2,Mark_rect[104])
                grid[8][8] = 'O'

            if dauhieuPsecond910 == True:
                WIN.blit(markP2,Mark_rect[105])
                grid[8][9] = 'O'

            if dauhieuPsecond911 == True:
                WIN.blit(markP2,Mark_rect[106])
                grid[8][10] = 'O'

            if dauhieuPsecond912 == True:
                WIN.blit(markP2,Mark_rect[107])
                grid[8][11] = 'O'
            
            #############
            if dauhieuPsecond101 == True:
                WIN.blit(markP2,Mark_rect[108])
                grid[9][0] = 'O'

            if dauhieuPsecond102 == True:
                WIN.blit(markP2,Mark_rect[109])
                grid[9][1] = 'O'

            if dauhieuPsecond103 == True:
                WIN.blit(markP2,Mark_rect[110])
                grid[9][2] = 'O'

            if dauhieuPsecond104 == True:
                WIN.blit(markP2,Mark_rect[111])
                grid[9][3] = 'O'

            if dauhieuPsecond105 == True:
                WIN.blit(markP2,Mark_rect[112])
                grid[9][4] = 'O'

            if dauhieuPsecond106 == True:
                WIN.blit(markP2,Mark_rect[113])
                grid[9][5] = 'O'

            if dauhieuPsecond107 == True:
                WIN.blit(markP2,Mark_rect[114])
                grid[9][6] = 'O'

            if dauhieuPsecond108 == True:
                WIN.blit(markP2,Mark_rect[115])
                grid[9][7] = 'O'

            if dauhieuPsecond109 == True:
                WIN.blit(markP2,Mark_rect[116])
                grid[9][8] = 'O'

            if dauhieuPsecond1010 == True:
                WIN.blit(markP2,Mark_rect[117])
                grid[9][9] = 'O'

            if dauhieuPsecond1011 == True:
                WIN.blit(markP2,Mark_rect[118])
                grid[9][10] = 'O'

            if dauhieuPsecond1012 == True:
                WIN.blit(markP2,Mark_rect[119])
                grid[9][11] = 'O'

            #############
            if dauhieuPsecond111a == True:
                WIN.blit(markP2,Mark_rect[120])
                grid[10][0] = 'O'

            if dauhieuPsecond112a == True:
                WIN.blit(markP2,Mark_rect[121])
                grid[10][1] = 'O'

            if dauhieuPsecond113 == True:
                WIN.blit(markP2,Mark_rect[122])
                grid[10][2] = 'O'

            if dauhieuPsecond114 == True:
                WIN.blit(markP2,Mark_rect[123])
                grid[10][3] = 'O'

            if dauhieuPsecond115 == True:
                WIN.blit(markP2,Mark_rect[124])
                grid[10][4] = 'O'

            if dauhieuPsecond116 == True:
                WIN.blit(markP2,Mark_rect[125])
                grid[10][5] = 'O'

            if dauhieuPsecond117 == True:
                WIN.blit(markP2,Mark_rect[126])
                grid[10][6] = 'O'

            if dauhieuPsecond118 == True:
                WIN.blit(markP2,Mark_rect[127])
                grid[10][7] = 'O'

            if dauhieuPsecond119 == True:
                WIN.blit(markP2,Mark_rect[128])
                grid[10][8] = 'O'

            if dauhieuPsecond1110 == True:
                WIN.blit(markP2,Mark_rect[129])
                grid[10][9] = 'O'

            if dauhieuPsecond1111 == True:
                WIN.blit(markP2,Mark_rect[130])
                grid[10][10] = 'O'

            if dauhieuPsecond1112 == True:
                WIN.blit(markP2,Mark_rect[131])
                grid[10][11] = 'O'
            #############
            if dauhieuPsecond121 == True:
                WIN.blit(markP2,Mark_rect[132])
                grid[11][0] = 'O'

            if dauhieuPsecond122 == True:
                WIN.blit(markP2,Mark_rect[133])
                grid[11][1] = 'O'

            if dauhieuPsecond123 == True:
                WIN.blit(markP2,Mark_rect[134])
                grid[11][2] = 'O'

            if dauhieuPsecond124 == True:
                WIN.blit(markP2,Mark_rect[135])
                grid[11][3] = 'O'

            if dauhieuPsecond125 == True:
                WIN.blit(markP2,Mark_rect[136])
                grid[11][4] = 'O'

            if dauhieuPsecond126 == True:
                WIN.blit(markP2,Mark_rect[137])
                grid[11][5] = 'O'

            if dauhieuPsecond127 == True:
                WIN.blit(markP2,Mark_rect[138])
                grid[11][6] = 'O'

            if dauhieuPsecond128 == True:
                WIN.blit(markP2,Mark_rect[139])
                grid[11][7] = 'O'

            if dauhieuPsecond129 == True:
                WIN.blit(markP2,Mark_rect[140])
                grid[11][8] = 'O'

            if dauhieuPsecond1210 == True:
                WIN.blit(markP2,Mark_rect[141])
                grid[11][9] = 'O'

            if dauhieuPsecond1211 == True:
                WIN.blit(markP2,Mark_rect[142])
                grid[11][10] = 'O'

            if dauhieuPsecond1212 == True:
                WIN.blit(markP2,Mark_rect[143])
                grid[11][11] = 'O'



        if i %2 == 0:
            playerTurn = markP1

            Announce_Turn = FONT.render("Player 1 'turn", 1 , 'red')
            Announce_rect = pygame.Rect(xfirst+10,25,Announce_Turn.get_width() + 20,Announce_Turn.get_height()+10)
            if (xfirst+10) <= mx <= (xfirst+10 +Announce_Turn.get_width() + 20) and 25 <= my <= 25 + Announce_Turn.get_height()+10:
                pygame.draw.rect(WIN,(162, 242, 240),Announce_rect,border_radius=10)
            else:
                pygame.draw.rect(WIN,(195, 235, 234),Announce_rect,border_radius=10)
            pygame.draw.rect(WIN,'black',Announce_rect,width=2,border_radius=10)
            WIN.blit(Announce_Turn,(xfirst+20,30))
            

            # Check WINNER 
            # Win by rows
            for row in grid:
                for index in range(8):
                    if row[index] == row[index+1] and row[index] == row[index+2] and row[index] == row[index+3] and row[index] == row[index+4] and row[index] == 'O':
                        print()
                        print(f'PLAYER 2 IS THE WINNER')
                        print()
                        print('GAME OVER')
                        run = False
                        
            # Win by columns
            for index in range(12):
                for row in range(8):
                    if grid[row][index] == grid[row+1][index] and grid[row][index] == grid[row+2][index] and grid[row][index] == grid[row+3][index] and grid[row][index] == grid[row+4][index] and grid[row][index] == 'O':
                        print()
                        print(f'PLAYER 2 IS THE WINNER')
                        print()
                        print('GAME OVER')
                        run = False
            # Win by right diagonal line
            for x in range(8):
                for y in range(8):
                    if grid[x][y] == grid[x+1][y+1] and grid[x][y] == grid[x+2][y+2] and grid[x][y] == grid[x+3][y+3] and grid[x][y] == grid[x+4][y+4] and grid[x][y] == 'O':
                        print()
                        print(f'PLAYER 2 IS THE WINNER')
                        print()
                        print('GAME OVER')
                        run = False
                        
            # Win by left diagonal line
            for x in range(8):
                for y in range(4,12):
                    if grid[x][y] == grid[x+1][y-1] and grid[x][y] == grid[x+2][y-2] and grid[x][y] == grid[x+3][y-3] and grid[x][y] == grid[x+4][y-4] and grid[x][y] == 'O':
                        print()
                        print(f'PLAYER 2 IS THE WINNER')
                        print()
                        print('GAME OVER')
                        run = False
                        
              

        if i %2 == 1:
            playerTurn = markP2

            Announce_Turn = FONT.render("Player 2'turn", 1 , 'red')
            Announce_rect = pygame.Rect(xfirst+10,25,Announce_Turn.get_width() + 20,Announce_Turn.get_height()+10)
            if (xfirst+10) <= mx <= (xfirst+10 +Announce_Turn.get_width() + 20) and 25 <= my <= 25 + Announce_Turn.get_height()+10:
                pygame.draw.rect(WIN,(162, 242, 240),Announce_rect,border_radius=10)
            else:
                pygame.draw.rect(WIN,(195, 235, 234),Announce_rect,border_radius=10)
            pygame.draw.rect(WIN,'black',Announce_rect,width=2,border_radius=10)
            WIN.blit(Announce_Turn,(xfirst+20,30))
            

            # Check WINNER 
            # Win by rows
            for row in grid:
                for index in range(8):
                    if row[index] == row[index+1] and row[index] == row[index+2] and row[index] == row[index+3] and row[index] == row[index+4] and row[index] == 'X':
                        print()
                        print(f'PLAYER 1 IS THE WINNER')
                        print()
                        print('GAME OVER')
                        run = False
                        
                        
            # Win by columns
            for index in range(12):
                for row in range(8):
                    if grid[row][index] == grid[row+1][index] and grid[row][index] == grid[row+2][index] and grid[row][index] == grid[row+3][index] and grid[row][index] == grid[row+4][index] and grid[row][index] == 'X':
                        print()
                        print(f'PLAYER 1 IS THE WINNER')
                        print()
                        print('GAME OVER')
                        run = False
                        
            # Win by right diagonal line
            for x in range(8):
                for y in range(8):
                    if grid[x][y] == grid[x+1][y+1] and grid[x][y] == grid[x+2][y+2] and grid[x][y] == grid[x+3][y+3] and grid[x][y] == grid[x+4][y+4] and grid[x][y] == 'X':
                        print()
                        print(f'PLAYER 1 IS THE WINNER')
                        print()
                        print('GAME OVER')
                        run = False
                        
            # Win by left diagonal line
            for x in range(8):
                for y in range(4,12):
                    if grid[x][y] == grid[x+1][y-1] and grid[x][y] == grid[x+2][y-2] and grid[x][y] == grid[x+3][y-3] and grid[x][y] == grid[x+4][y-4] and grid[x][y] == 'X':
                        print()
                        print(f'PLAYER 1 IS THE WINNER')
                        print()
                        print('GAME OVER')
                        run = False
                        
            
        
        
                
              
  
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:   
                if rect.collidepoint(event.pos):
                    print()
                    print('     1   2   3   4   5   6   7   8   9   10  11  12')
                    print('   +---+---+---+---+---+---+---+---+---+---+---+---+')
                    z=1
                    for x in grid:
                        if z<10:
                            print(z,end='  ')
                            print('|',end='')
                            for y in x:
                                print(' ' + y + ' |',end="")
                            print()
                            print('   +---+---+---+---+---+---+---+---+---+---+---+---+')
                            z+=1
                        else: 
                            print(z,end=' ')
                            print('|',end='')
                            for y in x:
                                print(' ' + y + ' |',end="")
                            print()
                            print('   +---+---+---+---+---+---+---+---+---+---+---+---+')
                            z+=1


        

        
        

        pygame.display.update()

    pygame.quit()



if __name__ == '__main__':
    main()




#dauhieu11,dauhieu12,dauhieu13,dauhieu14,dauhieu15,dauhieu16,dauhieu17,dauhieu18,dauhieu19,dauhieu110,dauhieu111,dauhieu112,dauhieu21,dauhieu22,dauhieu23,dauhieu24,dauhieu25,dauhieu26,dauhieu27,dauhieu28,dauhieu29,dauhieu210,dauhieu211,dauhieu212,dauhieu31,dauhieu32,dauhieu33,dauhieu34,dauhieu35,dauhieu36,dauhieu37,dauhieu38,dauhieu39,dauhieu310,dauhieu311,dauhieu312,dauhieu41,dauhieu42,dauhieu43,dauhieu44,dauhieu45,dauhieu46,dauhieu47,dauhieu48,dauhieu49,dauhieu410,dauhieu411,dauhieu412,dauhieu51,dauhieu52,dauhieu53,dauhieu54,dauhieu55,dauhieu56,dauhieu57,dauhieu58,dauhieu59,dauhieu510,dauhieu511,dauhieu512,dauhieu61,dauhieu62,dauhieu63,dauhieu64,dauhieu65,dauhieu66,dauhieu67,dauhieu68,dauhieu69,dauhieu610,dauhieu611,dauhieu612,dauhieu71,dauhieu72,dauhieu73,dauhieu74,dauhieu75,dauhieu76,dauhieu77,dauhieu78,dauhieu79,dauhieu710,dauhieu711,dauhieu712,dauhieu81,dauhieu82,dauhieu83,dauhieu84,dauhieu85,dauhieu86,dauhieu87,dauhieu88,dauhieu89,dauhieu810,dauhieu811,dauhieu812,dauhieu91,dauhieu92,dauhieu93,dauhieu94,dauhieu95,dauhieu96,dauhieu97,dauhieu98,dauhieu99,dauhieu910,dauhieu911,dauhieu912,dauhieu101,dauhieu102,dauhieu103,dauhieu104,dauhieu105,dauhieu106,dauhieu107,dauhieu108,dauhieu109,dauhieu1010,dauhieu1011,dauhieu1012,dauhieu111,dauhieu112,dauhieu113,dauhieu114,dauhieu115,dauhieu116,dauhieu117,dauhieu118,dauhieu119,dauhieu1110,dauhieu1111,dauhieu1112,dauhieu121,dauhieu122,dauhieu123,dauhieu124,dauhieu125,dauhieu126,dauhieu127,dauhieu128,dauhieu129,dauhieu1210,dauhieu1211,dauhieu1212