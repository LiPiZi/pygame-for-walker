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
'''pygame has a built in clock! Let's make a clock object, and call it clock.
	'''

while not gameExit: #gameloop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN: #movement
			if event.key == pygame.K_LEFT: 
				char_x_change = -10 
			if event.key == pygame.K_RIGHT:
				char_x_change = 10
				
	char_x += char_x_change 
	
	gameDisplay.fill(white) #bg
	pygame.draw.rect(gameDisplay, black, [char_x,char_y,10,10])
	pygame.display.update()
	
	clock.tick(10)
	'''This is the Frames-Per-Second variable. Since the original 
	documentation. I'm basing this off of is a snake game, it has very low 
	fps. You can also increase the char_x_change values under the if
	statements.	It's mildly hardcoded, we'll get to that.'''
#LOOP END
pygame.quit()
quit()