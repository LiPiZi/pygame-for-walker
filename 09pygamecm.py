import sys, pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Fun game!')

gameExit = False

char_x = 300
char_y = 300
char_x_change = 0

clock = pygame.time.Clock()
while not gameExit: #gameloop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN: #movement
			if event.key == pygame.K_LEFT: 
				char_x_change -= 4
			if event.key == pygame.K_RIGHT:
				char_x_change += 4
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				char_x_change += 4
			if event.key == pygame.K_RIGHT:
				char_x_change -= 4
		'''This is how you'd do it if you wanted to make a game with normal, game like 
		moving, stopping, etc. We're making a snake game, though.'''
	char_x += char_x_change 
	
	gameDisplay.fill(white) #bg
	pygame.draw.rect(gameDisplay, black, [char_x,char_y,10,10])
	pygame.display.update()
	
	clock.tick(30)
#LOOP END
pygame.quit()
quit()