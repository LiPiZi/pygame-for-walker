import sys
import pygame
import random



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
	
	randAppleX = round(random.randrange(0,(disp_width-block_size)/10.0))*10.0
	randAppleY = round(random.randrange(0,(disp_height-block_size)/10.0))*10.0
	'''A little bit complicated. This is making it so that the apple will be
	on the same grid as the snake.'''
	
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
		
		if char_x == randAppleX and char_y == randAppleY:
			print("eat food")
		'''Collision between the snake and the apple. This is easy because our
		objects are identical in size. You won't always be able to do it like
		that. See:
		https://www.youtube.com/watch?v=L8VE7o4wkM0 for the tutorial.'''
		clock.tick(fps)
	#LOOP END
	pygame.quit()
	quit()
	

if __name__ == "__main__":
	main()