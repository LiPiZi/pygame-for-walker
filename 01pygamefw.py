import sys, pygame

pygame.init()
'''This will initialize the pygame module.
does return something. says successful or not successful, if you set it to a 
variable.'''
gameDisplay = pygame.display.set_mode((800, 600))
'''needs to be a tuple inside, hence the double paren. Tuple = bundled data.
it can also be an list (python array).
The method itself defines the window we're going to launch. In this case,
it is an 800x600 window.
This is in mixedCase/camelCase. That's when the first letter is un-capped and everything
else is capped. Fairly common in programming for objects.''' 

#pygame.display.flip()
'''almost the same as update. Name is metaphor for flipbook.
flip updates entire surface at once. The game sort of operates like a flipbook
in that it flashes a certain number of frames. Review: Pixels don't actually
move. The location of the color of the pixels change.'''

pygame.display.update()
'''this one can update anything, but if you don't give it a parameter it will 
update entire surface like flip, so it's a little more powerful than flip.'''

pygame.quit()
'''un-initializes pygame, at the end of the program.'''

quit()
'''actually quits python'''