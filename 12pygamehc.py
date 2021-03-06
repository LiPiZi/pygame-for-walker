import sys, pygame
'''now we're fixing the hardcoding. This is cleaning up the program, because
some things are a little bit bodged.
An important part of programming is making your program extensible - 
making it so that other people can re-program it. Right now, say, if you were
to try to change the size of our character, you would have to change the size
in draw.rect, under the event.key == direction (because it moves one body 
length), et cetera. We're gonna move a bunch of things to variables.'''
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

disp_width = 800
disp_height = 600

gameDisplay = pygame.display.set_mode((disp_width, disp_height))
pygame.display.set_caption('Fun game!')

gameExit = False

char_x = disp_width/2
char_y = disp_height/2

char_x_change = 0
char_y_change = 0

clock = pygame.time.Clock()

block_size = 10

fps = 10

while not gameExit: #gameloop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN: #movement
			if event.key == pygame.K_LEFT: 
				char_x_change = -block_size
				char_y_change = 0
			elif event.key == pygame.K_RIGHT:
				char_x_change = block_size
				char_y_change = 0
			elif event.key == pygame.K_UP:
				char_y_change = -block_size
				char_x_change = 0
			elif event.key == pygame.K_DOWN:
				char_y_change = block_size
				char_x_change = 0
	
	if char_x>=disp_width or char_x<0 or char_y>=disp_height or char_y<0:
		gameExit = True
	char_x += char_x_change
	char_y += char_y_change

	gameDisplay.fill(white) #bg
	pygame.draw.rect(gameDisplay,black,[char_x,char_y,block_size,block_size])
	'''find everywhere it says 10, it's can probably be replaced by block_size
	. Now the numbers that matter have variables on them. Make sure it
	complies with the PEP character limit of 79 characters.'''
	pygame.display.update()
	
	clock.tick(fps)
#LOOP END
pygame.quit()
quit()