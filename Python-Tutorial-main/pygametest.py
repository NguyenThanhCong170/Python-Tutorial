import pygame
import time
import random
from PIL import ImageGrab
img = ImageGrab.grab()
pygame.font.init()
WIDTH, HEIGHT = img.size
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Space Dogde')
BG = pygame.transform.scale(pygame.image.load('bg.jpeg'),(WIDTH,HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20

FONT = pygame.font.SysFont('Arial',30)
def draw(player,elapsed_time,stars):
    dangerous_test1 = FONT.render('FAST!',1,'Purple')
    dangerous_test2 = FONT.render('FASTERRRR!',1,'Purple')
    dangerous_test3 = FONT.render('FASTER AND MORE STARRR!',1,'Purple')
    
    WIN.blit(BG,(0,0))
    
    time_text = FONT.render(f'Time: {round(elapsed_time)}s',1,'white')
    WIN.blit(time_text,(10,10))
    pygame.draw.rect(WIN,'red',player)
    for star in stars:
        pygame.draw.rect(WIN,'white',star)
    if round(elapsed_time) >= 40:
        WIN.fill('black',((WIDTH/2 -dangerous_test1.get_width()/2,10),(2*dangerous_test1.get_width()/2,30)))
        WIN.blit(dangerous_test1,(WIDTH/2 -dangerous_test1.get_width()/2,10))

    if round(elapsed_time) >= 60:
        WIN.fill('black',((WIDTH/2 -dangerous_test2.get_width()/2,10),(2*dangerous_test2.get_width()/2,30)))
        WIN.blit(dangerous_test2,(WIDTH/2 -dangerous_test2.get_width()/2,10))
    if round(elapsed_time) >= 72:
        WIN.fill('black',((WIDTH/2 -dangerous_test3.get_width()/2,10),(2*dangerous_test3.get_width()/2,30)))
        WIN.blit(dangerous_test3,(WIDTH/2 -dangerous_test3.get_width()/2,10))
    
    


    pygame.display.update()




def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    hit = False
    STAR_VEL = 3
    star_add_increment = 2000
    star_count = 0
    stars=[]
    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        
        if star_count > star_add_increment:
            if round(elapsed_time) <= 70:
                for _ in range(3):
                    star_x = random.randint(0,WIDTH-STAR_WIDTH)
                    star = pygame.Rect(star_x,-STAR_HEIGHT,STAR_WIDTH,STAR_HEIGHT)
                    stars.append(star)
                STAR_VEL += 0.05
                star_add_increment = max(200,star_add_increment-50)
                star_count = 0 
            elif round(elapsed_time) >= 70:
                for _ in range(3):
                    star_x = random.randint(0,WIDTH-STAR_WIDTH)
                    star = pygame.Rect(star_x,-STAR_HEIGHT,STAR_WIDTH,STAR_HEIGHT)
                    stars.append(star)
                STAR_VEL += 0.05
                star_add_increment = max(100,star_add_increment-50)
                star_count = 0 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x - PLAYER_VEL >=0 :
            player.x -= PLAYER_VEL
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_w] and player.y - PLAYER_VEL >=0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_s] and player.y + PLAYER_VEL + player.height <= HEIGHT:
            player.y += PLAYER_VEL
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        
       
        if hit:
            lost_test = FONT.render('You Lost!',1,'white')
            WIN.blit(lost_test,(WIDTH/2 - lost_test.get_width()/2,HEIGHT/2 -lost_test.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break






        draw(player,elapsed_time,stars)

    pygame.quit()



if __name__ == '__main__':
    main()