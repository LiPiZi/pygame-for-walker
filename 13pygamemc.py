import sys
import pygame
'''We're gonna do a little bit more readability work. first off, we separate
	the import statements, which is generally good manners.'''


'''Here we define main(). It's everything other than the import statements.
	'''
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
		pygame.draw.rect(gameDisplay,black,[char_x,char_y,block_size, \
		block_size])
		'''back slashes can be used to separate lines, so that they don't
		go over the pip 79 character limit. Not going over 79 characters is
		good manners because people like to program on one side of their
		screen.'''
		pygame.display.update()
		
		clock.tick(fps)
	#LOOP END
	pygame.quit()
	quit()
	
	
'''and here at the end, we do a "main check". This is generally good manners
because people like modularity access. We're making sure that we're just
running this program, not referencing it from another program. If we
referenced it in any way on another program, and we didn't have a main check,
the program would run automatically. Which would be rude.'''
if __name__ == "__main__":
	main()