import sys, pygame

pygame.init() #initialize pygame

gameDisplay = pygame.display.set_mode((800, 600)) #make window

pygame.display.set_caption('Slither')
'''This is the little window title. Called a caption for some reason. Put a 
string inside.'''

gameExit = False
'''bool. True or False. Remember the capitals. This is not a pygame variable, 
it's just for the loop below.'''

 '''called a game loop. It will keep running until gameexit is false.'''
while not gameExit:
	for event in pygame.event.get():
		print(event)
		'''Run this, and python will tell you every move you make, every 
		breath you take inside the window. Try it out.'''

pygame.quit() #un-initialize

quit() #quit python