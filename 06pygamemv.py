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
'''This is the location of the main character. If it's a top down shooting
	game or whatever, it's your character. If it's the snake game, then it's 
	your "head" block.'''

while not gameExit: #gameloop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		'''Below is testing whether a key is pressed, not whether if it's a 
		downward key. Keydown as in when you press the key into the keyboard.'''
		if event.type == pygame.KEYDOWN: 
			'''below is "if the key that was pressed is the left key"'''
			if event.key == pygame.K_LEFT: 
				'''Subtract 10 from char_x, which will move the character.
				Note that when you run the game, movement is very choppy.'''
				char_x -= 10 
			if event.key == pygame.K_RIGHT:
				char_x += 10
	gameDisplay.fill(white) #bg
	pygame.draw.rect(gameDisplay, black, [char_x,char_y,10,10])
	pygame.display.update() 
	'''Remember, this refreshes the window. Without it, we would not be able 
	to see the blocks move.'''
#LOOP END
pygame.quit()
quit()