'''two ways of drawing to the screen, sprites and drawing.
I removed the comments. Should be known by now, and nothing is
complex enough to really be commented on.'''
import sys, pygame

pygame.init()

'''Defining colors in a tuple. Learn RGB.'''
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
	'''Make entire screen white. That means use it as a background.'''
	pygame.display.update();
	'''put after everything you want to draw. Will make it.'''

pygame.quit()
quit()