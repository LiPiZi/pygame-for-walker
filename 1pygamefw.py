import sys, pygame

pygame.init()
'''initialize all of pygame modules we'll use.
does return something. says successful or not successful.'''
gameDisplay = pygame.display.set_mode((800, 600))
'''needs to be a tuple inside, hence the double paren. Tuple = bundled data.
it can also be an array.
The method itself defines the window we're going to launch. In this case,
it is an 800x600 window.
This is in mixedCase. That's when the first letter is un-capped and everything
else is capped. Fairly common in programming for objects.''' 

#pygame.display.flip()
'''almost the same as update. name is metaphor for flipbook.
flip updates entire surface at once.'''

pygame.display.update()
'''this one can update anything, but if you don't give it a parameter it will 
update entire surface like flip'''

pygame.quit()
'''un-initializes pygame'''

quit()
'''actually quits python'''