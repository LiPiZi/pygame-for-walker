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
'''Look up there'''
while not gameExit: #gameloop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN: #movement
			if event.key == pygame.K_LEFT: 
				char_x_change = -10 
				'''Choppy movement was because you only press the key down,
				moving it once. Let's work on that. First, we'll change
				the value/rate of change (calculus, anybody?)'''
			if event.key == pygame.K_RIGHT:
				char_x_change = 10
				'''note that it is no longer +=, instead set equal.'''
	char_x += char_x_change 
	'''+= moved here. Where the actual movement takes place.'''
	gameDisplay.fill(white) #bg
	pygame.draw.rect(gameDisplay, black, [char_x,char_y,10,10])
	pygame.display.update()
#LOOP END
pygame.quit()
quit()
'''note that the block moves really fast. that's because the framerate is not 
defined, and since the game is very simple, it runs very fast.'''