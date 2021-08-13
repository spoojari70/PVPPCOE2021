import pygame

screenValue  = pygame.init()
#print(screenValue)
gameWindows  = pygame.display.set_mode((1000,800))
pygame.display.set_caption("My First game")
exit_game = False
game_Over = False

while not exit_game:
    for event in pygame.event.get():
        print(event)
        #checking Quit Event
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You pressed Right key ")

            if event.key == pygame.K_LEFT:
                print("You pressed left key ")