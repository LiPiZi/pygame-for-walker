import sys, pygame

pygame.init()

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
	pygame.draw.rect(gameDisplay, black, [400,300,10,100]) 
	'''where to draw, color, [placex,placey,sizex,sizey]
	Note that on a computer, 0,0 is actually the top left corner, instead of
	the bottom left. In math it's the bottom right, but in computers they
	think down. Size fills out towards the bottom right.
	There's a way to do this with the fill function that's a little bit better
	optimised, but this should be fine. Google it if you want to use that 
	method.'''
	pygame.display.update();

pygame.quit()
quit()