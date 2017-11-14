'''two ways of putting images on the screen, sprites and drawing.
	I removed some of the old documentation.'''
import sys, pygame

pygame.init()

'''Defining colors in a tuple. If you don't know RGB, I'd look it up and get
	a feel for it.'''
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Fun game!')

gameExit = False

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
			
	gameDisplay.fill(white)
	'''Make entire screen white. That means use it as a background. Remember
	we defined white earlier.'''
	pygame.display.update();
	'''This refreshes the screen. If you draw something and don't refresh the
	the loop repeats 30 times a second at 30fps.'''
	screen at the end of the frame, then it will not be shown. Remember that

pygame.quit()
quit()