import sys, pygame

pygame.init() #initialize pygame

gameDisplay = pygame.display.set_mode((800, 600)) #make window
pygame.display.set_caption('Fun game!') #window title

gameExit = False #set up gameexit for loop

while not gameExit: #game loop
	for event in pygame.event.get():#mk variable event equal the current event
		if event.type == pygame.QUIT:'''This checks whether the current event 
		is quit (pressing the X button). See pygame module documentation for
		more events.'''
			gameExit = True
			'''Invalidates the while statement'''



pygame.quit() #un-initialize
quit() #quit python