import sys
import pygame
import random
'''we're making apples appear now. Apples appear randomly, so we're importing
the random library.'''



def main():
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
	
	randAppleX = random.randrange(0, disp_width-block_size)
	randAppleY = random.randrange(0, disp_height-block_size)
	'''we're putting the apple in a random place. Keep in mind things are
	drawn from the upper-left hand corner, so if we placed the apple at 
	800X or 600Y, it would be off the screen.'''

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

		gameDisplay.fill(white) #draw bg
		pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,block_size, \
		block_size])
		pygame.draw.rect(gameDisplay,black,[char_x,char_y,block_size, \
		block_size]) #draw character

		pygame.display.update()
		
		clock.tick(fps)
	#LOOP END
	pygame.quit()
	quit()
	

if __name__ == "__main__":
	main()