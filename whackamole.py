import pygame
from random import randrange

#This works
def draw_grid(screen):
    for i in range(1,16):
        pygame.draw.line(screen, "purple", (0,i*32), (640, i*32), 3)

    for i in range(1, 20):
        pygame.draw.line(screen, "purple", (i*32,0), (i*32, 512), 3)




def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        screen.fill("light green")
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        mole_location = (0,0)
        draw_grid(screen)
        pygame.display.update()
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x,y) = event.pos
                    print(event.pos)
                    a = x//32
                    b = y//32
                    click_spot = (a,b)
                    if click_spot == mole_location:
                        x = randrange(0,21)
                        y = randrange(0,17)
                        screen.blit(mole_image, mole_image.get_rect(center=((x*32)+18,(y*32)+16)))
                        mole_location = (((x*32)+16)//32,((y*32)+16)//32)
                        pygame.display.update()

            screen.fill("light green")
            draw_grid(screen)
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
