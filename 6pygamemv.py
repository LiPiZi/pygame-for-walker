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
'''in snake game, this is the main block'''

while not gameExit: #gameloop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		'''if a button is pressed down'''
		if event.type == pygame.KEYDOWN: 
			'''if the key that was pressed is the left key'''
			if event.key == pygame.K_LEFT: 
				'''add 10 to char_x, which will move the character. note
				that movement is very choppy.'''
				char_x -= 10 
			if event.key == pygame.K_RIGHT:
				char_x += 10
	gameDisplay.fill(white) #bg
	pygame.draw.rect(gameDisplay, black, [char_x,char_y,10,10])
	pygame.display.update() 
	'''remember, this refreshes the window. Without it, we would not be able to see the blocks move.'''
#LOOP END
pygame.quit()
quit()