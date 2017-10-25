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
char_y_change = 0

clock = pygame.time.Clock()

while not gameExit: #gameloop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN: #movement
			if event.key == pygame.K_LEFT: 
				char_x_change = -10
				char_y_change = 0
			elif event.key == pygame.K_RIGHT:
				char_x_change = 10
				char_y_change = 0
			elif event.key == pygame.K_UP:
				char_y_change = -10
				char_x_change = 0
			elif event.key == pygame.K_DOWN:
				char_y_change = 10
				char_x_change = 0
			'''elif means else-if. If one of these is true, then it's known
			that the rest are false. Saves processing power, because in snake
			you can't hold two directions at once and move diagonally,
			therefore it is redundant to check.'''
	char_x += char_x_change
	char_y += char_y_change
	'''remember this guy'''
	gameDisplay.fill(white) #bg
	pygame.draw.rect(gameDisplay, black, [char_x,char_y,10,10])
	pygame.display.update()
	
	clock.tick(10)
#LOOP END
pygame.quit()
quit()