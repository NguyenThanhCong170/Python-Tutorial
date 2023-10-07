import pygame
import time
import random
from PIL import ImageGrab
import sys
from button import Button

pygame.display.init()
img = ImageGrab.grab()
pygame.font.init()
WIDTH, HEIGHT = img.size
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
BG1 = pygame.transform.scale(pygame.image.load('assets/Background.png'),(WIDTH,HEIGHT))
BG = pygame.transform.scale(pygame.image.load('a.jpg'),(WIDTH,HEIGHT))
pic1 = pygame.transform.scale(pygame.image.load('1.jpg'),(200,200))
pic2 = pygame.transform.scale(pygame.image.load('2.jpg'),(200,200))
t1 = pygame.transform.scale(pygame.image.load('t1.png'),(200,200))
t2 = pygame.transform.scale(pygame.image.load('t2.webp'),(100,100))
hinhslide= pygame.transform.scale(pygame.image.load('ab.png'),(WIDTH,HEIGHT))

FONT2 = pygame.font.SysFont('Under Station.ttf',33)
FONT = pygame.font.SysFont('Under Station.ttf',100)
FONT1 = pygame.font.SysFont('Quahon.otf',40)
FONT3 = pygame.font.SysFont('Quahon.otf',50)
FONT4 = pygame.font.SysFont('Quahon.otf',70)
FONT5 = pygame.font.SysFont('Quahon.otf',40)
FONT6 = pygame.font.SysFont('Quahon.otf',55)
FONT7 = pygame.font.SysFont('Quahon.otf',120)

clock = pygame.time.Clock()
    

pygame.display.set_caption('Turtle Racing')
title = FONT.render('Turtle Racing',True,'brown3')
#time







pygame.display.update()

def draw(elapsed_time,Time,slide,active):
    #ban kinh
    bankinh = 20
    #toa do hinh tron
    toado1 = 198
    toado2 = 120
    #khoang cach
    khoangcach = 60

    # hinh tron
    hinhtron = [(toado1,toado2)]
    # toa do so
    
    toadoso1 = 186
    toadoso2 = 106
    toadoso = [(toadoso1,toadoso2)]
    
    
    for _ in range(1,17):
        m = khoangcach*(_)
        hinhtron.append((toado1+m,toado2))
        toadoso.append((toadoso1+khoangcach*(_),toadoso2))
    
    if slide == 0 :  
        WIN.blit(BG,(0,0))
        WIN.blit(title,(WIDTH/2 - title.get_width()/2,10))
        WIN.blit(Time,(0,50))
        time_text = FONT1.render(f'Time: {round(elapsed_time)}s',1,'orangered2')
        WIN.blit(time_text,(0,80))
        WIN.blit(pic1,(1100,300))
        WIN.blit(pic2,(1100,530))
        WIN.blit(t1,(173,420))
        WIN.blit(t2,(173,647))
        for i in range(1,17):
            pygame.draw.circle(WIN,'black',hinhtron[i],bankinh,3)
        for m in range(1,17):
            so = FONT2.render(f'{m}',1,'orangered2')
            WIN.blit(so,toadoso[m])
    
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)
def play():
    tx1 = 173
    ty1 = 380
    tx2 = 173
    ty2 = 600
    dauhieu1 = False
    dauhieu2 = False
    dauhieu3 = False
    dauhieu4 = False
    slide = 0
    abc = pygame.Rect(1058,514,290,232)
    #ban kinh
    bankinh = 20
    #toa do hinh tron
    toado1 = 198
    toado2 = 120
    
    #khoang cach
    khoangcach = 60
    toado3 = toado1+3*khoangcach
    toado4 = 180
    # hinh tron
    hinhtron = [(toado1,toado2)]
    # toa do so
    
    toadoso1 = 186
    toadoso2 = 106
    toadoso = [(toadoso1,toadoso2)]
    hinhtron1 = [(toado3,toado4)]
    toadoso1 = [(186+khoangcach*3,166)]
    
    for _ in range(1,11):
        m = khoangcach*(_)
        hinhtron.append((toado1+m,toado2))
        toadoso.append((186+m,toadoso2))
        hinhtron1.append((toado3+m,toado4))
        toadoso1.append((186+khoangcach*3+m,166))
    ovuong = [pygame.Rect(toado1-bankinh,toado2-bankinh,2*bankinh,2*bankinh)]
    ovuong1 =[pygame.Rect(toado3-bankinh,toado4-bankinh,2*bankinh,2*bankinh)]
    for _ in range(1,11):
        m = khoangcach*(_)
        ovuong.append(pygame.Rect(toado1+m-bankinh,toado2-bankinh,2*bankinh,2*bankinh))
        ovuong1.append(pygame.Rect(toado3-bankinh+m,toado4-bankinh,2*bankinh,2*bankinh))
    active = False
    start_time = time.time()
    elapsed_time = 0
    while True:
        c=time.asctime(time.localtime(time.time()))
        Time = FONT1.render(c,True,'orangered3')
        elapsed_time = time.time()-start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            
        if slide == 0 :  
            
            WIN.blit(BG,(0,0))
            WIN.blit(title,(WIDTH/2 - title.get_width()/2,10))
            WIN.blit(Time,(0,50))
            time_text = FONT1.render(f'Time: {round(elapsed_time)}s',1,'orangered2')
            WIN.blit(time_text,(0,80))
            WIN.blit(pic1,(1100,300))
            WIN.blit(pic2,(1100,530))
            WIN.blit(t1,(tx1,ty1))
            WIN.blit(t2,(tx2,ty2))
            for i in range(1,11):
                pygame.draw.circle(WIN,'black',hinhtron[i],bankinh,3)
                pygame.draw.circle(WIN,'black',hinhtron1[i],bankinh,3)
            for m in range(1,11):
                so = FONT2.render(f'{m}',1,'orangered2')
                WIN.blit(so,toadoso[m])
                so1 = FONT2.render(f'{m+10}',1,'orangered2')
                WIN.blit(so1,toadoso1[m])
            #103 494
            # 103 676
            #105 504
            #105 690
            kkk1 = FONT3.render('1',1,'red')
            kkk2 = FONT3.render('2',1,'red')
            pygame.draw.circle(WIN,'green',(113,514),30)
            pygame.draw.circle(WIN,'green',(113,694),30)
            WIN.blit(kkk1,(105,504))
            WIN.blit(kkk2,(105,680))
            kkk3 = pygame.Rect(113-30,514-30,2*30,2*30)
            kkk4 = pygame.Rect(113-30,694-30,2*30,2*30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for x in range(len(ovuong)):
                        if ovuong[x].collidepoint(event.pos):
                            slide = x+1
                        if ovuong1[x].collidepoint(event.pos):
                            slide = x+11
                        if kkk3.collidepoint(event.pos):
                            tx1 += 10
                        if kkk4.collidepoint(event.pos):
                            tx2 += 10
                if tx1 >= 1100:
                    slide = 50
                if tx2 >= 1100:
                    slide = 51
            
            pygame.display.update()
            

        
        if slide == 21:
            
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT4.render('Which activity below causes',1,'red')
            cauhoi_1 = FONT4.render('global warming ?',1,'red')
            WIN.blit(cauhoi1,(222,239))
            WIN.blit(cauhoi_1,(454,309))
            traloi1 = FONT3.render(f"Saying Hello",1,'chocolate3')
            traloi2 = FONT3.render('Smoking',1,'chocolate3')
            traloi3 = FONT3.render(f"Saying Hi",1,'chocolate3')
            traloi4 = FONT3.render(f"Saying Bye",1,'chocolate3')
            chucaia = FONT3.render('A',1,'brown3')
            chucaib = FONT3.render('B',1,'brown3')
            chucaic = FONT3.render('C',1,'brown3')
            chucaid = FONT3.render('D',1,'brown3')
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            c1 = list(traloi1.get_rect())
            c2 = list(traloi2.get_rect())
            c3 = list(traloi3.get_rect())
            c4 = list(traloi4.get_rect())
            dapan1 = pygame.Rect(220,557,c1[2],c1[3])
            dapan2 = pygame.Rect(676,557,c2[2],c2[3])
            dapan3 = pygame.Rect(220,647,c3[2],c3[3])
            dapan4 = pygame.Rect(676,647,c4[2],c4[3])
            pygame.draw.rect(WIN,'cadetblue',dapan2,2)
            pygame.draw.rect(WIN,'cadetblue',dapan3,2)
            pygame.draw.rect(WIN,'cadetblue',dapan4,2)
            pygame.draw.rect(WIN,'cadetblue',dapan1,2)
            WIN.blit(chucaia,(180,557))
            WIN.blit(chucaib,(636,557))
            WIN.blit(chucaic,(180,647))
            WIN.blit(chucaid,(636,647))
            WIN.blit(traloi1,(220,557))
            WIN.blit(traloi2,(676,557))
            WIN.blit(traloi3,(220,647))
            WIN.blit(traloi4,(676,647))
            # x,y = pygame.mouse.get_pos() #lay dia chi x,y
            # print(x,y)
            
            d1 = list(chucaia.get_rect())
            d2 = list(chucaib.get_rect())
            d3 = list(chucaic.get_rect())
            d4 = list(chucaid.get_rect())
            chondapan1 = pygame.Rect(180,557,d1[2],d1[3])
            chondapan2 = pygame.Rect(636,557,d2[2],d2[3])
            chondapan3 = pygame.Rect(180,647,d3[2],d3[3])
            chondapan4 = pygame.Rect(636,647,d4[2],d4[3])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chondapan1.collidepoint(event.pos):
                    dauhieu1 = True
                if chondapan2.collidepoint(event.pos):
                    dauhieu2 = True
                if chondapan3.collidepoint(event.pos):
                    dauhieu3 = True
                if chondapan4.collidepoint(event.pos):
                    dauhieu4 = True
                
                if event.button == 3:
                    slide = 0 
                    dauhieu1 = False
                    dauhieu2 = False
                    dauhieu3 = False
                    dauhieu4 = False
            if dauhieu1 == True:
                pygame.draw.line(WIN,'red',(180,557),(205,591),3)
                
            if dauhieu2 == True:
                pygame.draw.circle(WIN,'blue',(646,570),20,4)
            if dauhieu3 == True:
                pygame.draw.line(WIN,'red',(180,647),(205,681),3)
            if dauhieu4 == True:
                pygame.draw.line(WIN,'red',(636,647),(661,681),3)
            
            pygame.display.update()
                
        if slide == 2:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT4.render('Should we plant more tree?',1,'red')
            
            WIN.blit(cauhoi1,(222,239))
            
            traloi1 = FONT3.render('No',1,'chocolate3')
            traloi2 = FONT3.render('Yes',1,'chocolate3')
            traloi3 = FONT3.render('Nice to meet you',1,'chocolate3')
            traloi4 = FONT3.render('Good',1,'chocolate3')
            chucaia = FONT3.render('A',1,'brown3')
            chucaib = FONT3.render('B',1,'brown3')
            chucaic = FONT3.render('C',1,'brown3')
            chucaid = FONT3.render('D',1,'brown3')
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            c1 = list(traloi1.get_rect())
            c2 = list(traloi2.get_rect())
            c3 = list(traloi3.get_rect())
            c4 = list(traloi4.get_rect())
            dapan1 = pygame.Rect(220,557,c1[2],c1[3])
            dapan2 = pygame.Rect(676,557,c2[2],c2[3])
            dapan3 = pygame.Rect(220,647,c3[2],c3[3])
            dapan4 = pygame.Rect(676,647,c4[2],c4[3])
            pygame.draw.rect(WIN,'cadetblue',dapan2,2)
            pygame.draw.rect(WIN,'cadetblue',dapan3,2)
            pygame.draw.rect(WIN,'cadetblue',dapan4,2)
            pygame.draw.rect(WIN,'cadetblue',dapan1,2)
            WIN.blit(chucaia,(180,557))
            WIN.blit(chucaib,(636,557))
            WIN.blit(chucaic,(180,647))
            WIN.blit(chucaid,(636,647))
            WIN.blit(traloi1,(220,557))
            WIN.blit(traloi2,(676,557))
            WIN.blit(traloi3,(220,647))
            WIN.blit(traloi4,(676,647))
            # x,y = pygame.mouse.get_pos() #lay dia chi x,y
            # print(x,y)
            
            d1 = list(chucaia.get_rect())
            d2 = list(chucaib.get_rect())
            d3 = list(chucaic.get_rect())
            d4 = list(chucaid.get_rect())
            chondapan1 = pygame.Rect(180,557,d1[2],d1[3])
            chondapan2 = pygame.Rect(636,557,d2[2],d2[3])
            chondapan3 = pygame.Rect(180,647,d3[2],d3[3])
            chondapan4 = pygame.Rect(636,647,d4[2],d4[3])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chondapan1.collidepoint(event.pos):
                    dauhieu1 = True
                if chondapan2.collidepoint(event.pos):
                    dauhieu2 = True
                if chondapan3.collidepoint(event.pos):
                    dauhieu3 = True
                if chondapan4.collidepoint(event.pos):
                    dauhieu4 = True
                
                if event.button == 3:
                    slide = 0 
                    dauhieu1 = False
                    dauhieu2 = False
                    dauhieu3 = False
                    dauhieu4 = False
            if dauhieu1 == True:
                pygame.draw.line(WIN,'red',(180,557),(205,591),3)
                
            if dauhieu2 == True:
                pygame.draw.circle(WIN,'blue',(646,570),20,4)
            if dauhieu3 == True:
                pygame.draw.line(WIN,'red',(180,647),(205,681),3)
            if dauhieu4 == True:
                pygame.draw.line(WIN,'red',(636,647),(661,681),3)
            
            pygame.display.update()

        if slide == 3:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT4.render('How much human-made carbon could be',1,'red')
            cauhoi_1 = FONT4.render('removed by letting all forests regrow?',1,'red')
            WIN.blit(cauhoi1,(190,239))
            WIN.blit(cauhoi_1,(220,309))
            traloi1 = FONT3.render('One-third',1,'chocolate3')
            traloi2 = FONT3.render('Half',1,'chocolate3')
            traloi3 = FONT3.render('Two-thirds',1,'chocolate3')
            traloi4 = FONT3.render("Three-quarters",1,'chocolate3')
            chucaia = FONT3.render('A',1,'brown3')
            chucaib = FONT3.render('B',1,'brown3')
            chucaic = FONT3.render('C',1,'brown3')
            chucaid = FONT3.render('D',1,'brown3')
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            c1 = list(traloi1.get_rect())
            c2 = list(traloi2.get_rect())
            c3 = list(traloi3.get_rect())
            c4 = list(traloi4.get_rect())
            dapan1 = pygame.Rect(220,557,c1[2],c1[3])
            dapan2 = pygame.Rect(676,557,c2[2],c2[3])
            dapan3 = pygame.Rect(220,647,c3[2],c3[3])
            dapan4 = pygame.Rect(676,647,c4[2],c4[3])
            pygame.draw.rect(WIN,'cadetblue',dapan2,2)
            pygame.draw.rect(WIN,'cadetblue',dapan3,2)
            pygame.draw.rect(WIN,'cadetblue',dapan4,2)
            pygame.draw.rect(WIN,'cadetblue',dapan1,2)
            WIN.blit(chucaia,(180,557))
            WIN.blit(chucaib,(636,557))
            WIN.blit(chucaic,(180,647))
            WIN.blit(chucaid,(636,647))
            WIN.blit(traloi1,(220,557))
            WIN.blit(traloi2,(676,557))
            WIN.blit(traloi3,(220,647))
            WIN.blit(traloi4,(676,647))
            # x,y = pygame.mouse.get_pos() #lay dia chi x,y
            # print(x,y)
            
            d1 = list(chucaia.get_rect())
            d2 = list(chucaib.get_rect())
            d3 = list(chucaic.get_rect())
            d4 = list(chucaid.get_rect())
            chondapan1 = pygame.Rect(180,557,d1[2],d1[3])
            chondapan2 = pygame.Rect(636,557,d2[2],d2[3])
            chondapan3 = pygame.Rect(180,647,d3[2],d3[3])
            chondapan4 = pygame.Rect(636,647,d4[2],d4[3])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chondapan1.collidepoint(event.pos):
                    dauhieu1 = True
                if chondapan2.collidepoint(event.pos):
                    dauhieu2 = True
                if chondapan3.collidepoint(event.pos):
                    dauhieu3 = True
                if chondapan4.collidepoint(event.pos):
                    dauhieu4 = True
                
                if event.button == 3:
                    slide = 0 
                    dauhieu1 = False
                    dauhieu2 = False
                    dauhieu3 = False
                    dauhieu4 = False
            if dauhieu1 == True:
                pygame.draw.line(WIN,'red',(180,557),(205,591),3)
                
            if dauhieu2 == True:
                pygame.draw.line(WIN,'red',(636,557),(661,591),3)
            if dauhieu3 == True:
                pygame.draw.circle(WIN,'blue',(190,667),20,4)
            if dauhieu4 == True:
                pygame.draw.line(WIN,'red',(636,647),(661,681),3)
            
            pygame.display.update()
        if slide == 4:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT6.render('Why is cutting automotive transportation ',1,'red')
            cauhoi_1 = FONT6.render('completely out of your life not',1,'red')
            cauhoi__1 = FONT6.render('feasible for most people, as per the paragraph?',1,'red')
            WIN.blit(cauhoi__1,(250,379))
            
            WIN.blit(cauhoi1,(220,239))
            WIN.blit(cauhoi_1,(250,309))
            traloi1 = FONT3.render('Lack of public transportation options',1,'red')
            traloi2 = FONT3.render('High cost of alternative transportation',1,'red')
            traloi3 = FONT3.render('Geographic limitations',1,'red')
            traloi4 = FONT3.render('All of the above',1,'red')
            chucaia = FONT3.render('A',1,'brown3')
            chucaib = FONT3.render('B',1,'brown3')
            chucaic = FONT3.render('C',1,'brown3')
            chucaid = FONT3.render('D',1,'brown3')
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            c1 = list(traloi1.get_rect())
            c2 = list(traloi2.get_rect())
            c3 = list(traloi3.get_rect())
            c4 = list(traloi4.get_rect())
            dapan1 = pygame.Rect(300,550,c1[2],c1[3])
            dapan2 = pygame.Rect(300,600,c2[2],c2[3])
            dapan3 = pygame.Rect(300,650,c3[2],c3[3])
            dapan4 = pygame.Rect(300,700,c4[2],c4[3])
            pygame.draw.rect(WIN,'cadetblue',dapan2,2)
            pygame.draw.rect(WIN,'cadetblue',dapan3,2)
            pygame.draw.rect(WIN,'cadetblue',dapan4,2)
            pygame.draw.rect(WIN,'cadetblue',dapan1,2)
            WIN.blit(chucaia,(260,550))
            WIN.blit(chucaib,(260,600))
            WIN.blit(chucaic,(260,650))
            WIN.blit(chucaid,(260,700))
            WIN.blit(traloi1,(300,550))
            WIN.blit(traloi2,(300,600))
            WIN.blit(traloi3,(300,650))
            WIN.blit(traloi4,(300,700))
            # x,y = pygame.mouse.get_pos() #lay dia chi x,y
            # print(x,y)
            
            d1 = list(chucaia.get_rect())
            d2 = list(chucaib.get_rect())
            d3 = list(chucaic.get_rect())
            d4 = list(chucaid.get_rect())
            chondapan1 = pygame.Rect(260,550,d1[2],d1[3])
            chondapan2 = pygame.Rect(260,600,d2[2],d2[3])
            chondapan3 = pygame.Rect(260,650,d3[2],d3[3])
            chondapan4 = pygame.Rect(260,700,d4[2],d4[3])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chondapan1.collidepoint(event.pos):
                    dauhieu1 = True
                if chondapan2.collidepoint(event.pos):
                    dauhieu2 = True
                if chondapan3.collidepoint(event.pos):
                    dauhieu3 = True
                if chondapan4.collidepoint(event.pos):
                    dauhieu4 = True
                
                if event.button == 3:
                    slide = 0 
                    dauhieu1 = False
                    dauhieu2 = False
                    dauhieu3 = False
                    dauhieu4 = False
            if dauhieu1 == True:
                pygame.draw.line(WIN,'red',(260,550),(285,584),3)
                
            if dauhieu2 == True:
                pygame.draw.line(WIN,'red',(260,600),(285,634),3)
            if dauhieu3 == True:
                pygame.draw.line(WIN,'red',(260,650),(285,684),3)
            if dauhieu4 == True:
                pygame.draw.circle(WIN,'blue',(270,720),20,4)
            
            pygame.display.update()
        if slide == 5:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT6.render('Besides monitoring your thermostat,',1,'red')
            cauhoi_1 = FONT6.render('what is suggested as a way to prevent heat',1,'red')
            cauhoi__1 = FONT6.render('from escaping your home?',1,'red')
            WIN.blit(cauhoi__1,(250,379))
            
            WIN.blit(cauhoi1,(220,239))
            WIN.blit(cauhoi_1,(250,309))
            traloi1 = FONT3.render('Reducing electricity usage',1,'red')
            traloi2 = FONT3.render('Using more lighting',1,'red')
            traloi3 = FONT3.render('Increasing the size of windows',1,'red')
            traloi4 = FONT3.render('Improving insulation and airtightness',1,'red')
            chucaia = FONT3.render('A',1,'brown3')
            chucaib = FONT3.render('B',1,'brown3')
            chucaic = FONT3.render('C',1,'brown3')
            chucaid = FONT3.render('D',1,'brown3')
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            c1 = list(traloi1.get_rect())
            c2 = list(traloi2.get_rect())
            c3 = list(traloi3.get_rect())
            c4 = list(traloi4.get_rect())
            dapan1 = pygame.Rect(300,550,c1[2],c1[3])
            dapan2 = pygame.Rect(300,600,c2[2],c2[3])
            dapan3 = pygame.Rect(300,650,c3[2],c3[3])
            dapan4 = pygame.Rect(300,700,c4[2],c4[3])
            pygame.draw.rect(WIN,'cadetblue',dapan2,2)
            pygame.draw.rect(WIN,'cadetblue',dapan3,2)
            pygame.draw.rect(WIN,'cadetblue',dapan4,2)
            pygame.draw.rect(WIN,'cadetblue',dapan1,2)
            WIN.blit(chucaia,(260,550))
            WIN.blit(chucaib,(260,600))
            WIN.blit(chucaic,(260,650))
            WIN.blit(chucaid,(260,700))
            WIN.blit(traloi1,(300,550))
            WIN.blit(traloi2,(300,600))
            WIN.blit(traloi3,(300,650))
            WIN.blit(traloi4,(300,700))
            # x,y = pygame.mouse.get_pos() #lay dia chi x,y
            # print(x,y)
            
            d1 = list(chucaia.get_rect())
            d2 = list(chucaib.get_rect())
            d3 = list(chucaic.get_rect())
            d4 = list(chucaid.get_rect())
            chondapan1 = pygame.Rect(260,550,d1[2],d1[3])
            chondapan2 = pygame.Rect(260,600,d2[2],d2[3])
            chondapan3 = pygame.Rect(260,650,d3[2],d3[3])
            chondapan4 = pygame.Rect(260,700,d4[2],d4[3])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chondapan1.collidepoint(event.pos):
                    dauhieu1 = True
                if chondapan2.collidepoint(event.pos):
                    dauhieu2 = True
                if chondapan3.collidepoint(event.pos):
                    dauhieu3 = True
                if chondapan4.collidepoint(event.pos):
                    dauhieu4 = True
                
                if event.button == 3:
                    slide = 0 
                    dauhieu1 = False
                    dauhieu2 = False
                    dauhieu3 = False
                    dauhieu4 = False
            if dauhieu1 == True:
                pygame.draw.line(WIN,'red',(260,550),(285,584),3)
                
            if dauhieu2 == True:
                pygame.draw.line(WIN,'red',(260,600),(285,634),3)
            if dauhieu3 == True:
                pygame.draw.line(WIN,'red',(260,650),(285,684),3)
            if dauhieu4 == True:
                pygame.draw.circle(WIN,'blue',(270,720),20,4)
            
            pygame.display.update()
        if slide == 6:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT4.render('Root systems help to absorb',1,'red')
            cauhoi_1 = FONT4.render('and ….. water',1,'red')
            WIN.blit(cauhoi1,(222,239))
            WIN.blit(cauhoi_1,(454,309))
            traloi1 = FONT3.render('release',1,'chocolate3')
            traloi2 = FONT3.render('retain',1,'chocolate3')
            traloi3 = FONT3.render('emit',1,'chocolate3')
            traloi4 = FONT3.render('evaporate',1,'chocolate3')
            chucaia = FONT3.render('A',1,'brown3')
            chucaib = FONT3.render('B',1,'brown3')
            chucaic = FONT3.render('C',1,'brown3')
            chucaid = FONT3.render('D',1,'brown3')
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            c1 = list(traloi1.get_rect())
            c2 = list(traloi2.get_rect())
            c3 = list(traloi3.get_rect())
            c4 = list(traloi4.get_rect())
            dapan1 = pygame.Rect(220,557,c1[2],c1[3])
            dapan2 = pygame.Rect(676,557,c2[2],c2[3])
            dapan3 = pygame.Rect(220,647,c3[2],c3[3])
            dapan4 = pygame.Rect(676,647,c4[2],c4[3])
            pygame.draw.rect(WIN,'cadetblue',dapan2,2)
            pygame.draw.rect(WIN,'cadetblue',dapan3,2)
            pygame.draw.rect(WIN,'cadetblue',dapan4,2)
            pygame.draw.rect(WIN,'cadetblue',dapan1,2)
            WIN.blit(chucaia,(180,557))
            WIN.blit(chucaib,(636,557))
            WIN.blit(chucaic,(180,647))
            WIN.blit(chucaid,(636,647))
            WIN.blit(traloi1,(220,557))
            WIN.blit(traloi2,(676,557))
            WIN.blit(traloi3,(220,647))
            WIN.blit(traloi4,(676,647))
            # x,y = pygame.mouse.get_pos() #lay dia chi x,y
            # print(x,y)
            
            d1 = list(chucaia.get_rect())
            d2 = list(chucaib.get_rect())
            d3 = list(chucaic.get_rect())
            d4 = list(chucaid.get_rect())
            chondapan1 = pygame.Rect(180,557,d1[2],d1[3])
            chondapan2 = pygame.Rect(636,557,d2[2],d2[3])
            chondapan3 = pygame.Rect(180,647,d3[2],d3[3])
            chondapan4 = pygame.Rect(636,647,d4[2],d4[3])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chondapan1.collidepoint(event.pos):
                    dauhieu1 = True
                if chondapan2.collidepoint(event.pos):
                    dauhieu2 = True
                if chondapan3.collidepoint(event.pos):
                    dauhieu3 = True
                if chondapan4.collidepoint(event.pos):
                    dauhieu4 = True
                
                if event.button == 3:
                    slide = 0 
                    dauhieu1 = False
                    dauhieu2 = False
                    dauhieu3 = False
                    dauhieu4 = False
            if dauhieu1 == True:
                pygame.draw.line(WIN,'red',(180,557),(205,591),3)
                
            if dauhieu2 == True:
                pygame.draw.circle(WIN,'blue',(646,570),20,4)
            if dauhieu3 == True:
                pygame.draw.line(WIN,'red',(180,647),(205,681),3)
            if dauhieu4 == True:
                pygame.draw.line(WIN,'red',(636,647),(661,681),3)
            
            pygame.display.update()
        if slide == 7:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT4.render('As temperature rises, forests',1,'red')
            cauhoi_1 = FONT4.render('become more susceptible to....',1,'red')
            WIN.blit(cauhoi1,(222,239))
            WIN.blit(cauhoi_1,(454,309))
            traloi1 = FONT3.render('frost',1,'chocolate3')
            traloi2 = FONT3.render('erosion',1,'chocolate3')
            traloi3 = FONT3.render('disease',1,'chocolate3')
            traloi4 = FONT3.render('wildfire',1,'chocolate3')
            chucaia = FONT3.render('A',1,'brown3')
            chucaib = FONT3.render('B',1,'brown3')
            chucaic = FONT3.render('C',1,'brown3')
            chucaid = FONT3.render('D',1,'brown3')
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            c1 = list(traloi1.get_rect())
            c2 = list(traloi2.get_rect())
            c3 = list(traloi3.get_rect())
            c4 = list(traloi4.get_rect())
            dapan1 = pygame.Rect(220,557,c1[2],c1[3])
            dapan2 = pygame.Rect(676,557,c2[2],c2[3])
            dapan3 = pygame.Rect(220,647,c3[2],c3[3])
            dapan4 = pygame.Rect(676,647,c4[2],c4[3])
            pygame.draw.rect(WIN,'cadetblue',dapan2,2)
            pygame.draw.rect(WIN,'cadetblue',dapan3,2)
            pygame.draw.rect(WIN,'cadetblue',dapan4,2)
            pygame.draw.rect(WIN,'cadetblue',dapan1,2)
            WIN.blit(chucaia,(180,557))
            WIN.blit(chucaib,(636,557))
            WIN.blit(chucaic,(180,647))
            WIN.blit(chucaid,(636,647))
            WIN.blit(traloi1,(220,557))
            WIN.blit(traloi2,(676,557))
            WIN.blit(traloi3,(220,647))
            WIN.blit(traloi4,(676,647))
            # x,y = pygame.mouse.get_pos() #lay dia chi x,y
            # print(x,y)
            
            d1 = list(chucaia.get_rect())
            d2 = list(chucaib.get_rect())
            d3 = list(chucaic.get_rect())
            d4 = list(chucaid.get_rect())
            chondapan1 = pygame.Rect(180,557,d1[2],d1[3])
            chondapan2 = pygame.Rect(636,557,d2[2],d2[3])
            chondapan3 = pygame.Rect(180,647,d3[2],d3[3])
            chondapan4 = pygame.Rect(636,647,d4[2],d4[3])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chondapan1.collidepoint(event.pos):
                    dauhieu1 = True
                if chondapan2.collidepoint(event.pos):
                    dauhieu2 = True
                if chondapan3.collidepoint(event.pos):
                    dauhieu3 = True
                if chondapan4.collidepoint(event.pos):
                    dauhieu4 = True
                
                if event.button == 3:
                    slide = 0 
                    dauhieu1 = False
                    dauhieu2 = False
                    dauhieu3 = False
                    dauhieu4 = False
            if dauhieu1 == True:
                pygame.draw.line(WIN,'red',(180,557),(205,591),3)
                
            if dauhieu2 == True:
                pygame.draw.line(WIN,'red',(636,557),(661,591),3)
            if dauhieu3 == True:
                pygame.draw.line(WIN,'red',(180,647),(205,681),3)
            if dauhieu4 == True:
                pygame.draw.circle(WIN,'blue',(646,667),20,4)
            
            pygame.display.update()
        if slide == 8:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT4.render('Forests have a lower albedo',1,'red')
            cauhoi_1 = FONT4.render(', which means they reflect ',1,'red')
            cauhoi__1 = FONT4.render('… sunlight and absorb …. heat',1,'red')
            WIN.blit(cauhoi__1,(250,379))
            
            WIN.blit(cauhoi1,(220,239))
            WIN.blit(cauhoi_1,(250,309))
            traloi1 = FONT3.render('less, more',1,'chocolate3')
            traloi2 = FONT3.render('more, more',1,'chocolate3')
            traloi3 = FONT3.render('less, less',1,'chocolate3')
            traloi4 = FONT3.render('more, less',1,'chocolate3')
            chucaia = FONT3.render('A',1,'brown3')
            chucaib = FONT3.render('B',1,'brown3')
            chucaic = FONT3.render('C',1,'brown3')
            chucaid = FONT3.render('D',1,'brown3')
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            c1 = list(traloi1.get_rect())
            c2 = list(traloi2.get_rect())
            c3 = list(traloi3.get_rect())
            c4 = list(traloi4.get_rect())
            dapan1 = pygame.Rect(220,557,c1[2],c1[3])
            dapan2 = pygame.Rect(676,557,c2[2],c2[3])
            dapan3 = pygame.Rect(220,647,c3[2],c3[3])
            dapan4 = pygame.Rect(676,647,c4[2],c4[3])
            pygame.draw.rect(WIN,'cadetblue',dapan2,2)
            pygame.draw.rect(WIN,'cadetblue',dapan3,2)
            pygame.draw.rect(WIN,'cadetblue',dapan4,2)
            pygame.draw.rect(WIN,'cadetblue',dapan1,2)
            WIN.blit(chucaia,(180,557))
            WIN.blit(chucaib,(636,557))
            WIN.blit(chucaic,(180,647))
            WIN.blit(chucaid,(636,647))
            WIN.blit(traloi1,(220,557))
            WIN.blit(traloi2,(676,557))
            WIN.blit(traloi3,(220,647))
            WIN.blit(traloi4,(676,647))
            # x,y = pygame.mouse.get_pos() #lay dia chi x,y
            # print(x,y)
            
            d1 = list(chucaia.get_rect())
            d2 = list(chucaib.get_rect())
            d3 = list(chucaic.get_rect())
            d4 = list(chucaid.get_rect())
            chondapan1 = pygame.Rect(180,557,d1[2],d1[3])
            chondapan2 = pygame.Rect(636,557,d2[2],d2[3])
            chondapan3 = pygame.Rect(180,647,d3[2],d3[3])
            chondapan4 = pygame.Rect(636,647,d4[2],d4[3])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chondapan1.collidepoint(event.pos):
                    dauhieu1 = True
                if chondapan2.collidepoint(event.pos):
                    dauhieu2 = True
                if chondapan3.collidepoint(event.pos):
                    dauhieu3 = True
                if chondapan4.collidepoint(event.pos):
                    dauhieu4 = True
                
                if event.button == 3:
                    slide = 0 
                    dauhieu1 = False
                    dauhieu2 = False
                    dauhieu3 = False
                    dauhieu4 = False
            if dauhieu1 == True:
                pygame.draw.circle(WIN,'blue',(190,577),20,3)
                
            if dauhieu2 == True:
                pygame.draw.line(WIN,'red',(636,557),(661,591),3)
            if dauhieu3 == True:
                pygame.draw.line(WIN,'red',(180,647),(205,681),3)
            if dauhieu4 == True:
                pygame.draw.line(WIN,'red',(636,647),(661,681),3)
            
            pygame.display.update()


        if slide == 9:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT4.render('Climate change leads to ',1,'red')
            cauhoi_1 = FONT4.render('global warming',1,'red')
            WIN.blit(cauhoi1,(222,239))
            WIN.blit(cauhoi_1,(454,309))
            traloi1 = FONT3.render('True',1,'chocolate3')
            traloi2 = FONT3.render('False',1,'chocolate3')
            traloi3 = FONT3.render('i dont know',1,'chocolate3')
            traloi4 = FONT3.render('nobody asked',1,'chocolate3')
            chucaia = FONT3.render('A',1,'brown3')
            chucaib = FONT3.render('B',1,'brown3')
            chucaic = FONT3.render('C',1,'brown3')
            chucaid = FONT3.render('D',1,'brown3')
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            c1 = list(traloi1.get_rect())
            c2 = list(traloi2.get_rect())
            c3 = list(traloi3.get_rect())
            c4 = list(traloi4.get_rect())
            dapan1 = pygame.Rect(220,557,c1[2],c1[3])
            dapan2 = pygame.Rect(676,557,c2[2],c2[3])
            dapan3 = pygame.Rect(220,647,c3[2],c3[3])
            dapan4 = pygame.Rect(676,647,c4[2],c4[3])
            pygame.draw.rect(WIN,'cadetblue',dapan2,2)
            pygame.draw.rect(WIN,'cadetblue',dapan3,2)
            pygame.draw.rect(WIN,'cadetblue',dapan4,2)
            pygame.draw.rect(WIN,'cadetblue',dapan1,2)
            WIN.blit(chucaia,(180,557))
            WIN.blit(chucaib,(636,557))
            WIN.blit(chucaic,(180,647))
            WIN.blit(chucaid,(636,647))
            WIN.blit(traloi1,(220,557))
            WIN.blit(traloi2,(676,557))
            WIN.blit(traloi3,(220,647))
            WIN.blit(traloi4,(676,647))
            # x,y = pygame.mouse.get_pos() #lay dia chi x,y
            # print(x,y)
            
            d1 = list(chucaia.get_rect())
            d2 = list(chucaib.get_rect())
            d3 = list(chucaic.get_rect())
            d4 = list(chucaid.get_rect())
            chondapan1 = pygame.Rect(180,557,d1[2],d1[3])
            chondapan2 = pygame.Rect(636,557,d2[2],d2[3])
            chondapan3 = pygame.Rect(180,647,d3[2],d3[3])
            chondapan4 = pygame.Rect(636,647,d4[2],d4[3])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chondapan1.collidepoint(event.pos):
                    dauhieu1 = True
                if chondapan2.collidepoint(event.pos):
                    dauhieu2 = True
                if chondapan3.collidepoint(event.pos):
                    dauhieu3 = True
                if chondapan4.collidepoint(event.pos):
                    dauhieu4 = True
                
                if event.button == 3:
                    slide = 0 
                    dauhieu1 = False
                    dauhieu2 = False
                    dauhieu3 = False
                    dauhieu4 = False
            if dauhieu1 == True:
                pygame.draw.line(WIN,'red',(180,557),(205,591),3)
                
            if dauhieu2 == True:
                pygame.draw.circle(WIN,'blue',(646,570),20,4)
            if dauhieu3 == True:
                pygame.draw.line(WIN,'red',(180,647),(205,681),3)
            if dauhieu4 == True:
                pygame.draw.line(WIN,'red',(636,647),(661,681),3)
            
            pygame.display.update()


        if slide == 10:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT4.render('Why is global warming pace increased',1,'red')
            cauhoi_1 = FONT4.render('significantly fast in the last century?',1,'red')
            dapan = FONT4.render('burning coal, oil or gas',1,'chocolate3')
            WIN.blit(cauhoi1,(222,239))
            WIN.blit(cauhoi_1,(250,309))
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if abc.collidepoint(event.pos):
                    active = True
                
                if event.button == 3:
                    slide = 0 
                    active = False
            if active == True:
                WIN.blit(dapan,(350,577))
            
            pygame.display.update()


        if slide == 11:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT4.render('Which is a sign of global warming?',1,'red')
            
            WIN.blit(cauhoi1,(190,239))
        
            traloi1 = FONT3.render('Melting glaciers',1,'chocolate3')
            traloi2 = FONT3.render('Volcanic eruptions',1,'chocolate3')
            traloi3 = FONT3.render('Hurricane',1,'chocolate3')
            traloi4 = FONT3.render('Landslides',1,'chocolate3')
            chucaia = FONT3.render('A',1,'brown3')
            chucaib = FONT3.render('B',1,'brown3')
            chucaic = FONT3.render('C',1,'brown3')
            chucaid = FONT3.render('D',1,'brown3')
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            c1 = list(traloi1.get_rect())
            c2 = list(traloi2.get_rect())
            c3 = list(traloi3.get_rect())
            c4 = list(traloi4.get_rect())
            dapan1 = pygame.Rect(220,557,c1[2],c1[3])
            dapan2 = pygame.Rect(676,557,c2[2],c2[3])
            dapan3 = pygame.Rect(220,647,c3[2],c3[3])
            dapan4 = pygame.Rect(676,647,c4[2],c4[3])
            pygame.draw.rect(WIN,'cadetblue',dapan2,2)
            pygame.draw.rect(WIN,'cadetblue',dapan3,2)
            pygame.draw.rect(WIN,'cadetblue',dapan4,2)
            pygame.draw.rect(WIN,'cadetblue',dapan1,2)
            WIN.blit(chucaia,(180,557))
            WIN.blit(chucaib,(636,557))
            WIN.blit(chucaic,(180,647))
            WIN.blit(chucaid,(636,647))
            WIN.blit(traloi1,(220,557))
            WIN.blit(traloi2,(676,557))
            WIN.blit(traloi3,(220,647))
            WIN.blit(traloi4,(676,647))
            # x,y = pygame.mouse.get_pos() #lay dia chi x,y
            # print(x,y)
            
            d1 = list(chucaia.get_rect())
            d2 = list(chucaib.get_rect())
            d3 = list(chucaic.get_rect())
            d4 = list(chucaid.get_rect())
            chondapan1 = pygame.Rect(180,557,d1[2],d1[3])
            chondapan2 = pygame.Rect(636,557,d2[2],d2[3])
            chondapan3 = pygame.Rect(180,647,d3[2],d3[3])
            chondapan4 = pygame.Rect(636,647,d4[2],d4[3])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chondapan1.collidepoint(event.pos):
                    dauhieu1 = True
                if chondapan2.collidepoint(event.pos):
                    dauhieu2 = True
                if chondapan3.collidepoint(event.pos):
                    dauhieu3 = True
                if chondapan4.collidepoint(event.pos):
                    dauhieu4 = True
                
                if event.button == 3:
                    slide = 0 
                    dauhieu1 = False
                    dauhieu2 = False
                    dauhieu3 = False
                    dauhieu4 = False
            if dauhieu1 == True:
                pygame.draw.circle(WIN,'blue',(190,577),20,3)
                
            if dauhieu2 == True:
                pygame.draw.line(WIN,'red',(636,557),(661,591),3)
            if dauhieu3 == True:
                pygame.draw.line(WIN,'red',(180,647),(205,681),3)
            if dauhieu4 == True:
                pygame.draw.line(WIN,'red',(636,647),(661,681),3)
            
            pygame.display.update()


        if slide == 12:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT4.render('Why is glacial melt a concern?',1,'red')
            
            WIN.blit(cauhoi1,(190,239))
            
            traloi1 = FONT3.render('Sea level rise',1,'chocolate3')
            traloi2 = FONT3.render('Impact on the climate',1,'chocolate3')
            traloi3 = FONT3.render('extinction of numerous species',1,'chocolate3')
            traloi4 = FONT3.render('A,B,C',1,'chocolate3')
            chucaia = FONT3.render('A',1,'brown3')
            chucaib = FONT3.render('B',1,'brown3')
            chucaic = FONT3.render('C',1,'brown3')
            chucaid = FONT3.render('D',1,'brown3')
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            c1 = list(traloi1.get_rect())
            c2 = list(traloi2.get_rect())
            c3 = list(traloi3.get_rect())
            c4 = list(traloi4.get_rect())
            dapan1 = pygame.Rect(220,557,c1[2],c1[3])
            dapan2 = pygame.Rect(676,557,c2[2],c2[3])
            dapan3 = pygame.Rect(220,647,c3[2],c3[3])
            dapan4 = pygame.Rect(676,647,c4[2],c4[3])
            pygame.draw.rect(WIN,'cadetblue',dapan2,2)
            pygame.draw.rect(WIN,'cadetblue',dapan3,2)
            pygame.draw.rect(WIN,'cadetblue',dapan4,2)
            pygame.draw.rect(WIN,'cadetblue',dapan1,2)
            WIN.blit(chucaia,(180,557))
            WIN.blit(chucaib,(636,557))
            WIN.blit(chucaic,(180,647))
            WIN.blit(chucaid,(810,647))
            WIN.blit(traloi1,(220,557))
            WIN.blit(traloi2,(676,557))
            WIN.blit(traloi3,(220,647))
            WIN.blit(traloi4,(850,647))
            # x,y = pygame.mouse.get_pos() #lay dia chi x,y
            # print(x,y)
            
            d1 = list(chucaia.get_rect())
            d2 = list(chucaib.get_rect())
            d3 = list(chucaic.get_rect())
            d4 = list(chucaid.get_rect())
            chondapan1 = pygame.Rect(180,557,d1[2],d1[3])
            chondapan2 = pygame.Rect(636,557,d2[2],d2[3])
            chondapan3 = pygame.Rect(180,647,d3[2],d3[3])
            chondapan4 = pygame.Rect(810,647,d4[2],d4[3])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chondapan1.collidepoint(event.pos):
                    dauhieu1 = True
                if chondapan2.collidepoint(event.pos):
                    dauhieu2 = True
                if chondapan3.collidepoint(event.pos):
                    dauhieu3 = True
                if chondapan4.collidepoint(event.pos):
                    dauhieu4 = True
                
                if event.button == 3:
                    slide = 0 
                    dauhieu1 = False
                    dauhieu2 = False
                    dauhieu3 = False
                    dauhieu4 = False
            if dauhieu1 == True:
                pygame.draw.circle(WIN,'blue',(190,577),20,3)
                
            if dauhieu2 == True:
                pygame.draw.line(WIN,'red',(636,557),(661,591),3)
            if dauhieu3 == True:
                pygame.draw.line(WIN,'red',(180,647),(205,681),3)
            if dauhieu4 == True:
                pygame.draw.line(WIN,'red',(810,647),(835,681),3)
            
            pygame.display.update()


        if slide == 13:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT4.render('Is it too late to prevent',1,'red')
            cauhoi_1 = FONT4.render('global warming?',1,'red')
            WIN.blit(cauhoi1,(222,239))
            WIN.blit(cauhoi_1,(454,309))
            traloi1 = FONT3.render('Yes, no hope',1,'red')
            traloi2 = FONT3.render('No, we can still change the situation in few years',1,'red')
            traloi3 = FONT5.render('Not too late, but high temperatures still remain well-elevated for many, many centuries',1,'red')
            
            chucaia = FONT3.render('A',1,'brown3')
            chucaib = FONT3.render('B',1,'brown3')
            chucaic = FONT3.render('C',1,'brown3')
            
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            c1 = list(traloi1.get_rect())
            c2 = list(traloi2.get_rect())
            c3 = list(traloi3.get_rect())
            
            dapan1 = pygame.Rect(100,550,c1[2],c1[3])
            dapan2 = pygame.Rect(100,600,c2[2],c2[3])
            dapan3 = pygame.Rect(100,650,c3[2],c3[3])
            
            pygame.draw.rect(WIN,'cadetblue',dapan2,2)
            pygame.draw.rect(WIN,'cadetblue',dapan3,2)
            
            pygame.draw.rect(WIN,'cadetblue',dapan1,2)
            WIN.blit(chucaia,(60,550))
            WIN.blit(chucaib,(60,600))
            WIN.blit(chucaic,(60,650))
            
            WIN.blit(traloi1,(100,550))
            WIN.blit(traloi2,(100,600))
            WIN.blit(traloi3,(100,650))
            
            # x,y = pygame.mouse.get_pos() #lay dia chi x,y
            # print(x,y)
            
            d1 = list(chucaia.get_rect())
            d2 = list(chucaib.get_rect())
            d3 = list(chucaic.get_rect())
            
            chondapan1 = pygame.Rect(60,550,d1[2],d1[3])
            chondapan2 = pygame.Rect(60,600,d2[2],d2[3])
            chondapan3 = pygame.Rect(60,650,d3[2],d3[3])
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chondapan1.collidepoint(event.pos):
                    dauhieu1 = True
                if chondapan2.collidepoint(event.pos):
                    dauhieu2 = True
                if chondapan3.collidepoint(event.pos):
                    dauhieu3 = True
                
                
                if event.button == 3:
                    slide = 0 
                    dauhieu1 = False
                    dauhieu2 = False
                    dauhieu3 = False
                    
            if dauhieu1 == True:
                pygame.draw.line(WIN,'red',(60,550),(85,591),3)
                
            if dauhieu2 == True:
                pygame.draw.line(WIN,'red',(60,600),(85,634),3)
            if dauhieu3 == True:
                pygame.draw.circle(WIN,'red',(70,667),20,4)
            
            
            pygame.display.update()


        if slide == 14:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT4.render('Who is at risk from the impacts',1,'red')
            cauhoi_1 = FONT4.render('of climate change?',1,'red')
            WIN.blit(cauhoi1,(222,239))
            WIN.blit(cauhoi_1,(454,309))
            traloi1 = FONT3.render('Every species including human',1,'chocolate3')
            traloi2 = FONT3.render('Dinosaurs',1,'chocolate3')
            traloi3 = FONT3.render('Animals',1,'chocolate3')
            traloi4 = FONT3.render('Human',1,'chocolate3')
            chucaia = FONT3.render('A',1,'brown3')
            chucaib = FONT3.render('B',1,'brown3')
            chucaic = FONT3.render('C',1,'brown3')
            chucaid = FONT3.render('D',1,'brown3')
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            c1 = list(traloi1.get_rect())
            c2 = list(traloi2.get_rect())
            c3 = list(traloi3.get_rect())
            c4 = list(traloi4.get_rect())
            dapan1 = pygame.Rect(220,557,c1[2],c1[3])
            dapan2 = pygame.Rect(850,557,c2[2],c2[3])
            dapan3 = pygame.Rect(220,647,c3[2],c3[3])
            dapan4 = pygame.Rect(676,647,c4[2],c4[3])
            pygame.draw.rect(WIN,'cadetblue',dapan2,2)
            pygame.draw.rect(WIN,'cadetblue',dapan3,2)
            pygame.draw.rect(WIN,'cadetblue',dapan4,2)
            pygame.draw.rect(WIN,'cadetblue',dapan1,2)
            WIN.blit(chucaia,(180,557))
            WIN.blit(chucaib,(810,557))
            WIN.blit(chucaic,(180,647))
            WIN.blit(chucaid,(636,647))
            WIN.blit(traloi1,(220,557))
            WIN.blit(traloi2,(850,557))
            WIN.blit(traloi3,(220,647))
            WIN.blit(traloi4,(676,647))
            # x,y = pygame.mouse.get_pos() #lay dia chi x,y
            # print(x,y)
            
            d1 = list(chucaia.get_rect())
            d2 = list(chucaib.get_rect())
            d3 = list(chucaic.get_rect())
            d4 = list(chucaid.get_rect())
            chondapan1 = pygame.Rect(180,557,d1[2],d1[3])
            chondapan2 = pygame.Rect(810,557,d2[2],d2[3])
            chondapan3 = pygame.Rect(180,647,d3[2],d3[3])
            chondapan4 = pygame.Rect(636,647,d4[2],d4[3])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chondapan1.collidepoint(event.pos):
                    dauhieu1 = True
                if chondapan2.collidepoint(event.pos):
                    dauhieu2 = True
                if chondapan3.collidepoint(event.pos):
                    dauhieu3 = True
                if chondapan4.collidepoint(event.pos):
                    dauhieu4 = True
                
                if event.button == 3:
                    slide = 0 
                    dauhieu1 = False
                    dauhieu2 = False
                    dauhieu3 = False
                    dauhieu4 = False
            if dauhieu1 == True:
                pygame.draw.circle(WIN,'blue',(190,577),20,3)
                
            if dauhieu2 == True:
                pygame.draw.line(WIN,'red',(810,557),(835,591),3)
            if dauhieu3 == True:
                pygame.draw.line(WIN,'red',(180,647),(205,681),3)
            if dauhieu4 == True:
                pygame.draw.line(WIN,'red',(636,647),(661,681),3)
            
            pygame.display.update()


        if slide == 15:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT4.render('How many species are expected to',1,'red')
            cauhoi_1 = FONT4.render('become extinct in the next few decades?',1,'red')
            WIN.blit(cauhoi1,(190,239))
            WIN.blit(cauhoi_1,(190,309))
            traloi1 = FONT3.render('1 hundred',1,'chocolate3')
            traloi2 = FONT3.render('1 thousand',1,'chocolate3')
            traloi3 = FONT3.render('1 million',1,'chocolate3')
            traloi4 = FONT3.render('10 thousand',1,'chocolate3')
            chucaia = FONT3.render('A',1,'brown3')
            chucaib = FONT3.render('B',1,'brown3')
            chucaic = FONT3.render('C',1,'brown3')
            chucaid = FONT3.render('D',1,'brown3')
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            c1 = list(traloi1.get_rect())
            c2 = list(traloi2.get_rect())
            c3 = list(traloi3.get_rect())
            c4 = list(traloi4.get_rect())
            dapan1 = pygame.Rect(220,557,c1[2],c1[3])
            dapan2 = pygame.Rect(676,557,c2[2],c2[3])
            dapan3 = pygame.Rect(220,647,c3[2],c3[3])
            dapan4 = pygame.Rect(676,647,c4[2],c4[3])
            pygame.draw.rect(WIN,'cadetblue',dapan2,2)
            pygame.draw.rect(WIN,'cadetblue',dapan3,2)
            pygame.draw.rect(WIN,'cadetblue',dapan4,2)
            pygame.draw.rect(WIN,'cadetblue',dapan1,2)
            WIN.blit(chucaia,(180,557))
            WIN.blit(chucaib,(636,557))
            WIN.blit(chucaic,(180,647))
            WIN.blit(chucaid,(636,647))
            WIN.blit(traloi1,(220,557))
            WIN.blit(traloi2,(676,557))
            WIN.blit(traloi3,(220,647))
            WIN.blit(traloi4,(676,647))
            # x,y = pygame.mouse.get_pos() #lay dia chi x,y
            # print(x,y)
            
            d1 = list(chucaia.get_rect())
            d2 = list(chucaib.get_rect())
            d3 = list(chucaic.get_rect())
            d4 = list(chucaid.get_rect())
            chondapan1 = pygame.Rect(180,557,d1[2],d1[3])
            chondapan2 = pygame.Rect(636,557,d2[2],d2[3])
            chondapan3 = pygame.Rect(180,647,d3[2],d3[3])
            chondapan4 = pygame.Rect(636,647,d4[2],d4[3])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chondapan1.collidepoint(event.pos):
                    dauhieu1 = True
                if chondapan2.collidepoint(event.pos):
                    dauhieu2 = True
                if chondapan3.collidepoint(event.pos):
                    dauhieu3 = True
                if chondapan4.collidepoint(event.pos):
                    dauhieu4 = True
                
                if event.button == 3:
                    slide = 0 
                    dauhieu1 = False
                    dauhieu2 = False
                    dauhieu3 = False
                    dauhieu4 = False
            if dauhieu1 == True:
                pygame.draw.line(WIN,'red',(180,557),(205,591),3)
                
            if dauhieu2 == True:
                pygame.draw.line(WIN,'red',(636,557),(661,591),3)
            if dauhieu3 == True:
                pygame.draw.circle(WIN,'blue',(190,667),20,4)
            if dauhieu4 == True:
                pygame.draw.line(WIN,'red',(636,647),(661,681),3)
            
            pygame.display.update()

  
        if slide == 16:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT6.render('………  is the loss of life on Earth at various levels,',1,'red')
            cauhoi_1 = FONT6.render('ranging from reductions in the genetic',1,'red')
            cauhoi__1 = FONT6.render(' diversity to the collapse of entire ecosystems',1,'red')
            WIN.blit(cauhoi1,(222,239))
            WIN.blit(cauhoi_1,(250,309))
            WIN.blit(cauhoi__1,(250,379))
            traloi1 = FONT3.render('Biodiversity loss',1,'chocolate3')
            traloi2 = FONT3.render('Extinction',1,'chocolate3')
            traloi3 = FONT3.render('Ecological imbalance',1,'chocolate3')
            traloi4 = FONT3.render('Habitat disruption',1,'chocolate3')
            chucaia = FONT3.render('A',1,'brown3')
            chucaib = FONT3.render('B',1,'brown3')
            chucaic = FONT3.render('C',1,'brown3')
            chucaid = FONT3.render('D',1,'brown3')
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            c1 = list(traloi1.get_rect())
            c2 = list(traloi2.get_rect())
            c3 = list(traloi3.get_rect())
            c4 = list(traloi4.get_rect())
            dapan1 = pygame.Rect(220,557,c1[2],c1[3])
            dapan2 = pygame.Rect(676,557,c2[2],c2[3])
            dapan3 = pygame.Rect(220,647,c3[2],c3[3])
            dapan4 = pygame.Rect(676,647,c4[2],c4[3])
            pygame.draw.rect(WIN,'cadetblue',dapan2,2)
            pygame.draw.rect(WIN,'cadetblue',dapan3,2)
            pygame.draw.rect(WIN,'cadetblue',dapan4,2)
            pygame.draw.rect(WIN,'cadetblue',dapan1,2)
            WIN.blit(chucaia,(180,557))
            WIN.blit(chucaib,(636,557))
            WIN.blit(chucaic,(180,647))
            WIN.blit(chucaid,(636,647))
            WIN.blit(traloi1,(220,557))
            WIN.blit(traloi2,(676,557))
            WIN.blit(traloi3,(220,647))
            WIN.blit(traloi4,(676,647))
            # x,y = pygame.mouse.get_pos() #lay dia chi x,y
            # print(x,y)
            
            d1 = list(chucaia.get_rect())
            d2 = list(chucaib.get_rect())
            d3 = list(chucaic.get_rect())
            d4 = list(chucaid.get_rect())
            chondapan1 = pygame.Rect(180,557,d1[2],d1[3])
            chondapan2 = pygame.Rect(636,557,d2[2],d2[3])
            chondapan3 = pygame.Rect(180,647,d3[2],d3[3])
            chondapan4 = pygame.Rect(636,647,d4[2],d4[3])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chondapan1.collidepoint(event.pos):
                    dauhieu1 = True
                if chondapan2.collidepoint(event.pos):
                    dauhieu2 = True
                if chondapan3.collidepoint(event.pos):
                    dauhieu3 = True
                if chondapan4.collidepoint(event.pos):
                    dauhieu4 = True
                
                if event.button == 3:
                    slide = 0 
                    dauhieu1 = False
                    dauhieu2 = False
                    dauhieu3 = False
                    dauhieu4 = False
            if dauhieu1 == True:
                pygame.draw.circle(WIN,'blue',(190,577),20,3)
                
            if dauhieu2 == True:
                pygame.draw.line(WIN,'red',(636,557),(661,591),3)
            if dauhieu3 == True:
                pygame.draw.line(WIN,'red',(180,647),(205,681),3)
            if dauhieu4 == True:
                pygame.draw.line(WIN,'red',(636,647),(661,681),3)
            pygame.display.update()


        if slide == 17:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT4.render('Which job is severely affected by ',1,'red')
            cauhoi_1 = FONT4.render('global warming?',1,'red')
            dapan = FONT4.render('Construction worker',1,'chocolate3')
            WIN.blit(cauhoi1,(222,239))
            WIN.blit(cauhoi_1,(450,309))
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if abc.collidepoint(event.pos):
                    active = True
                
                if event.button == 3:
                    slide = 0 
                    active = False
            if active == True:
                WIN.blit(dapan,(450,577))
            
            pygame.display.update()
        if slide == 18:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT6.render('What percentage of emissions released from ',1,'red')
            cauhoi_1 = FONT6.render('to emissions from all vehicles cars compared?',1,'red')
           
            WIN.blit(cauhoi1,(222,239))
            WIN.blit(cauhoi_1,(250,309))
            
            traloi1 = FONT3.render('7%',1,'chocolate3')
            traloi2 = FONT3.render('23%',1,'chocolate3')
            traloi3 = FONT3.render('20%',1,'chocolate3')
            traloi4 = FONT3.render('82%',1,'chocolate3')
            chucaia = FONT3.render('A',1,'brown3')
            chucaib = FONT3.render('B',1,'brown3')
            chucaic = FONT3.render('C',1,'brown3')
            chucaid = FONT3.render('D',1,'brown3')
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            c1 = list(traloi1.get_rect())
            c2 = list(traloi2.get_rect())
            c3 = list(traloi3.get_rect())
            c4 = list(traloi4.get_rect())
            dapan1 = pygame.Rect(220,557,c1[2],c1[3])
            dapan2 = pygame.Rect(676,557,c2[2],c2[3])
            dapan3 = pygame.Rect(220,647,c3[2],c3[3])
            dapan4 = pygame.Rect(676,647,c4[2],c4[3])
            pygame.draw.rect(WIN,'cadetblue',dapan2,2)
            pygame.draw.rect(WIN,'cadetblue',dapan3,2)
            pygame.draw.rect(WIN,'cadetblue',dapan4,2)
            pygame.draw.rect(WIN,'cadetblue',dapan1,2)
            WIN.blit(chucaia,(180,557))
            WIN.blit(chucaib,(636,557))
            WIN.blit(chucaic,(180,647))
            WIN.blit(chucaid,(636,647))
            WIN.blit(traloi1,(220,557))
            WIN.blit(traloi2,(676,557))
            WIN.blit(traloi3,(220,647))
            WIN.blit(traloi4,(676,647))
            # x,y = pygame.mouse.get_pos() #lay dia chi x,y
            # print(x,y)
            
            d1 = list(chucaia.get_rect())
            d2 = list(chucaib.get_rect())
            d3 = list(chucaic.get_rect())
            d4 = list(chucaid.get_rect())
            chondapan1 = pygame.Rect(180,557,d1[2],d1[3])
            chondapan2 = pygame.Rect(636,557,d2[2],d2[3])
            chondapan3 = pygame.Rect(180,647,d3[2],d3[3])
            chondapan4 = pygame.Rect(636,647,d4[2],d4[3])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chondapan1.collidepoint(event.pos):
                    dauhieu1 = True
                if chondapan2.collidepoint(event.pos):
                    dauhieu2 = True
                if chondapan3.collidepoint(event.pos):
                    dauhieu3 = True
                if chondapan4.collidepoint(event.pos):
                    dauhieu4 = True
                
                if event.button == 3:
                    slide = 0 
                    dauhieu1 = False
                    dauhieu2 = False
                    dauhieu3 = False
                    dauhieu4 = False
            if dauhieu1 == True:
                pygame.draw.line(WIN,'red',(180,557),(205,591),3)
                
            if dauhieu2 == True:
                pygame.draw.line(WIN,'red',(636,557),(661,591),3)
            if dauhieu3 == True:
                pygame.draw.line(WIN,'red',(180,647),(205,681),3)
            if dauhieu4 == True:
                pygame.draw.circle(WIN,'blue',(646,667),20,4)
            pygame.display.update()
        if slide == 19:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT4.render('_____ are the single biggest energy ',1,'red')
            cauhoi_1 = FONT4.render('expense in the home.',1,'red')
            dapan = FONT4.render('Heating systems',1,'chocolate3')
            WIN.blit(cauhoi1,(222,239))
            WIN.blit(cauhoi_1,(450,309))
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if abc.collidepoint(event.pos):
                    active = True
                
                if event.button == 3:
                    slide = 0 
                    active = False
            if active == True:
                WIN.blit(dapan,(450,577))
            
            pygame.display.update()  
        if slide ==20:
            WIN.blit(hinhslide,(0,0))
            # 
            cauhoi1 = FONT6.render('What is the advantage of coal divestment?',1,'red')
            
           
            
            WIN.blit(cauhoi1,(220,239))
            
            traloi1 = FONT3.render('Absorb Co2',1,'red')
            traloi2 = FONT3.render('Reduce methane emission',1,'red')
            traloi3 = FONT3.render('promote ethical and environmentally conscious financial decisions',1,'red')
            traloi4 = FONT3.render('cut down on fuel consumption',1,'red')
            chucaia = FONT3.render('A',1,'brown3')
            chucaib = FONT3.render('B',1,'brown3')
            chucaic = FONT3.render('C',1,'brown3')
            chucaid = FONT3.render('D',1,'brown3')
            
            # pygame.draw.rect(WIN,'orangered2',traloi1.get_rect(),3)
            # 
            c1 = list(traloi1.get_rect())
            c2 = list(traloi2.get_rect())
            c3 = list(traloi3.get_rect())
            c4 = list(traloi4.get_rect())
            dapan1 = pygame.Rect(140,550,c1[2],c1[3])
            dapan2 = pygame.Rect(140,600,c2[2],c2[3])
            dapan3 = pygame.Rect(140,650,c3[2],c3[3])
            dapan4 = pygame.Rect(140,700,c4[2],c4[3])
            pygame.draw.rect(WIN,'cadetblue',dapan2,2)
            pygame.draw.rect(WIN,'cadetblue',dapan3,2)
            pygame.draw.rect(WIN,'cadetblue',dapan4,2)
            pygame.draw.rect(WIN,'cadetblue',dapan1,2)
            WIN.blit(chucaia,(100,550))
            WIN.blit(chucaib,(100,600))
            WIN.blit(chucaic,(100,650))
            WIN.blit(chucaid,(100,700))
            WIN.blit(traloi1,(140,550))
            WIN.blit(traloi2,(140,600))
            WIN.blit(traloi3,(140,650))
            WIN.blit(traloi4,(140,700))
            # x,y = pygame.mouse.get_pos() #lay dia chi x,y
            # print(x,y)
            
            d1 = list(chucaia.get_rect())
            d2 = list(chucaib.get_rect())
            d3 = list(chucaic.get_rect())
            d4 = list(chucaid.get_rect())
            chondapan1 = pygame.Rect(100,550,d1[2],d1[3])
            chondapan2 = pygame.Rect(100,600,d2[2],d2[3])
            chondapan3 = pygame.Rect(100,650,d3[2],d3[3])
            chondapan4 = pygame.Rect(100,700,d4[2],d4[3])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chondapan1.collidepoint(event.pos):
                    dauhieu1 = True
                if chondapan2.collidepoint(event.pos):
                    dauhieu2 = True
                if chondapan3.collidepoint(event.pos):
                    dauhieu3 = True
                if chondapan4.collidepoint(event.pos):
                    dauhieu4 = True
                
                if event.button == 3:
                    slide = 0 
                    dauhieu1 = False
                    dauhieu2 = False
                    dauhieu3 = False
                    dauhieu4 = False
            if dauhieu1 == True:
                pygame.draw.line(WIN,'red',(100,550),(125,584),3)
                
            if dauhieu2 == True:
                pygame.draw.line(WIN,'red',(100,600),(125,634),3)
            if dauhieu3 == True:
                pygame.draw.circle(WIN,'blue',(110,670),20,4)
            if dauhieu4 == True:
                pygame.draw.line(WIN,'red',(100,700),(125,734),3)
            
            pygame.display.update()
        if slide == 50:
           WIN.fill('black')
           chucai1 = FONT7.render('TEAM1 WIN',1,'white')
           WIN.blit(chucai1,(WIDTH/2 -chucai1.get_width()/2,HEIGHT/2 - chucai1.get_height()/2))
           
        if slide == 51:
            WIN.fill('black')
            chucai2 = FONT7.render('TEAM2 WIN',1,'white')
            WIN.blit(chucai2,(WIDTH/2 -chucai2.get_width()/2,HEIGHT/2 - chucai2.get_height()/2))
            


        pygame.display.update()
def rule():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        WIN.fill("white")

        # OPTIONS_TEXT = get_font(20).render("This is the turtle racing game. Before we get started, we want to divide this class into 2 teams.", True, "Black")
        # OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(WIDTH/2,50))
        # OPTIONS_TEXT1 = get_font(20).render("There are 20 questions and we will go into each question. Which team has the answer first and", True, "Black")
        # OPTIONS_TEXT2 = get_font(20).render(" hand will prioritise in answer. Then we roll a dice and the turtle will move.", True, "Black")
        # OPTIONS_TEXT3 = get_font(20).render(" Which team has their turtle comes home first will win and have a gift from us",True,"Black")
        # OPTIONS_RECT1 = OPTIONS_TEXT1.get_rect(center=(WIDTH/2,100))
        # OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(WIDTH/2,150))
        # OPTIONS_RECT3 = OPTIONS_TEXT3.get_rect(center=(WIDTH/2,200))
        # WIN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        # WIN.blit(OPTIONS_TEXT1, OPTIONS_RECT1)
        # WIN.blit(OPTIONS_TEXT2, OPTIONS_RECT2)
        # WIN.blit(OPTIONS_TEXT3, OPTIONS_RECT3)
        OPTIONS_TEXT = get_font(20).render("This is the turtle racing game.", True, "Black")
        OPTIONS_TEXT1 = get_font(20).render("Before we get started, we want ", True, "Black")
        OPTIONS_TEXT2 = get_font(20).render("to divide this class into 2 teams.",True,"Black")
        OPTIONS_TEXT3 = get_font(20).render("There are 20 questions and we will ", True, "Black")
        OPTIONS_TEXT4 = get_font(20).render("go into each question. Which team ", True, "Black")
        OPTIONS_TEXT5 = get_font(20).render("has the answer first and raise their", True, "Black")
        OPTIONS_TEXT6 = get_font(20).render("hand will prioritise in answering. Then", True, "Black")
        OPTIONS_TEXT7 = get_font(20).render("we roll a dice and the turtle will move.", True, "Black")
        OPTIONS_TEXT8 = get_font(20).render("Which team has their turtle comes home ",True,"Black")
        OPTIONS_TEXT9 = get_font(20).render("first will win and have a gift from us",True,"Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(WIDTH/2,50))
        OPTIONS_RECT1 = OPTIONS_TEXT1.get_rect(center=(WIDTH/2,100))
        OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(WIDTH/2,150))
        OPTIONS_RECT3 = OPTIONS_TEXT3.get_rect(center=(WIDTH/2,200))
        OPTIONS_RECT4 = OPTIONS_TEXT4.get_rect(center=(WIDTH/2,250))
        OPTIONS_RECT5 = OPTIONS_TEXT5.get_rect(center=(WIDTH/2,300))
        OPTIONS_RECT6 = OPTIONS_TEXT6.get_rect(center=(WIDTH/2,350))
        OPTIONS_RECT7 = OPTIONS_TEXT7.get_rect(center=(WIDTH/2,400))
        OPTIONS_RECT8 = OPTIONS_TEXT8.get_rect(center=(WIDTH/2,450))
        OPTIONS_RECT9 = OPTIONS_TEXT9.get_rect(center=(WIDTH/2,500))
        WIN.blit(OPTIONS_TEXT1, OPTIONS_RECT1)
        WIN.blit(OPTIONS_TEXT2, OPTIONS_RECT2)
        WIN.blit(OPTIONS_TEXT3, OPTIONS_RECT3)
        WIN.blit(OPTIONS_TEXT4, OPTIONS_RECT4)
        WIN.blit(OPTIONS_TEXT5, OPTIONS_RECT5)
        WIN.blit(OPTIONS_TEXT6, OPTIONS_RECT6)
        WIN.blit(OPTIONS_TEXT7, OPTIONS_RECT7)
        WIN.blit(OPTIONS_TEXT8, OPTIONS_RECT8)
        WIN.blit(OPTIONS_TEXT9, OPTIONS_RECT9)
        WIN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(WIDTH/2 , 600), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main()

        pygame.display.update()

def main():
    slide = -1
    while True:
        
        
        if slide == -1:
            WIN.blit(BG1, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                                text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                                text_input="RULE", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                                text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

            WIN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(WIN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        slide = 0
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        rule()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
        else:
            play()
       
            
        
            
                
            

         



        # draw(elapsed_time,Time,slide,active)




        x,y = pygame.mouse.get_pos() #lay dia chi x,y
        print(x,y)
if __name__ == '__main__':
    main()





        




    
    
    
    






    



