import sys, pygame

pygame.init() #initialize pygame

gameDisplay = pygame.display.set_mode((800, 600)) #make window
pygame.display.set_caption('Fun game!') #window title

gameExit = False #set up gameexit for loop

while not gameExit: #game loop
	for event in pygame.event.get():#mk variable event equal the current event
		if event.type == pygame.QUIT:'''This checks whether the current event 
		is quit (pressing the X button). We'll go over more events, or just
		check out the Pygame documentation for more events.'''
			gameExit = True
			'''Invalidates the while statement, so you exit the game loop.'''



pygame.quit() #un-initialize
quit() #quit python