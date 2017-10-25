import sys, pygame

pygame.init() #initialize pygame

gameDisplay = pygame.display.set_mode((800, 600)) #make window

pygame.display.set_caption('Slither')
'''This is the little window title. Called a caption. String inside.'''

gameExit = False
'''bool. True or False. Remember the capitals.'''

 '''called a game loop. It will keep running until gameexit is false.'''
while not gameExit:
	for event in pygame.event.get():
		print(event)


pygame.quit() #un-initialize

quit() #quit python