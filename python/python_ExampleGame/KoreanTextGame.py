import pygame as game

#초기화
game.init()
screen = game.display.set_mode((800, 600))
game.display.set_caption("PYGAME!")
clock = game.time.Clock()

TIMER = game.USEREVENT + 1
game.time.set_timer(TIMER, 300)
img = game.image.load("pokemon.png")
#img = game.transform.scale(img, (300, 300))

FONT = game.font.SysFont("malgum gothic", 48)
text =FONT.render("Intel", True,(255, 255, 255))
x= 250
y = 150
while True :      
    screen.fill((0,0,0))

    for event in game.event.get():
        if event.type == TIMER:
            screen.blit(img, (x, y))
        elif event.type == game.KEYDOWN:
            if event.key == game.K_q:        
                game.quit()              
            elif event.key == game.K_UP:
                y -= 10
            elif event.key == game.K_DOWN:
                y += 10
            elif event.key == game.K_RIGHT:
                x += 10       
            elif event.key == game.K_LEFT:
                x -= 10                                       
    #y += 1 
    #if y > 600:
    #   y = 0

    game.display.update()

    clock.tick(30)       