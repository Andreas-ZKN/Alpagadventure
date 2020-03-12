import sys, pygame
pygame.init

size = width, height = 800, 600

screen = pygame.display.set_mode(size)

white = (255, 255, 255)
black = (0, 0, 0)
red = (243, 23, 23)

screen.fill(white)

font = pygame.font.init()
font1 = pygame.font.init()
font2 = pygame.font.init()
font = pygame.font.SysFont("Comicsansms", 50)
font1 = pygame.font.SysFont ("Comicsansms", 20)
font2 = pygame.font.SysFont("Comicsansms", 30)

#demander a andreas de faire les decors. la : scene avec perso de dos et plusieurs choix de chemins en face.
Question = font.render("Quel chemin veux tu emprunter?", 1, black)
Prop1 = font1.render("Foret maléfique", 1, black)
Prop2 = font1.render("lac enchanté", 1, black)
mort = font2.render("Vous avez choisi le mauvais chemin. Vous êtes mort!", 1, red)
Restart = font1.render("Recommencer?", 1, white)
oui = font1.render("oui", 1, white)
non = font1.render("non", 1, white)


screen.blit(Question, (0, 0))
screen.blit(Prop1, (100, 500))
screen.blit(Prop2, (600, 500))


pygame.display.flip()

play = 1

# je dois pas le faire avancer, je dois faire un questionnaire a choix multiple. en gros.

while play == 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
#est ce que partir sur Deux trucs differents ou est ce qu'on peut reunir?
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Square1 = pygame.draw.rect(screen, black, (90, 490, 165, 50), 1)
                Square2 = pygame.draw.rect(screen, white, (590, 490, 135, 50), 1)
                pygame.display.flip()

            if event.key == pygame.K_RIGHT:
                Square2 = pygame.draw.rect(screen, black, (590, 490, 135, 50), 1)
                Square1 = pygame.draw.rect(screen, white, (90, 490, 165, 50), 1)
                pygame.display.flip()
#a faire : tout bien placé.
            if event.key == pygame.K_RETURN:
                screen.fill(black)
                screen.blit(mort, (50, 250))
                screen.blit(Restart, (200, 300))
                screen.blit(oui, (150, 350))
                screen.blit(non, (400, 350))

                Square1 = pygame.draw.rect(screen, white, (145, 345, 100, 50), 1)
                Square2 = pygame.draw.rect(screen, white, (90, 490, 165, 50), 1)

                pygame.display.flip()
