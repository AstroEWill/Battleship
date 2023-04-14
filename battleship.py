import sys
import pygame
pygame.init()

from settings import Settings
from coordFunctions import make_grid

class Battleship:
    "Class to manage game assets and behavior"
    def __init__(self):
        pygame.init() #initialize game, create resources
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Battleship')

        #Set background color
        self.bg_color = (209, 209, 209)

    def run_game(self):
        shipGrid = make_grid()
        width = int((self.settings.screen_width - 200) / len(shipGrid))
        height = int((self.settings.screen_height - 200) / len(shipGrid))

        margin = 5

        grid = []
        for row in range(len(shipGrid)):
            grid.append([])
            for col in range(len(shipGrid)):
                grid[row].append(0)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (width + margin)
                    row = pos[1] // (height + margin)

                    grid[row][column] = 1
                    if shipGrid[row][column] != '~':
                        print('Hit')
                    else:
                        print('Miss')            

            #Redraw the screen for each pass through the loop
            self.screen.fill(self.settings.bg_color)
            for row in range(len(shipGrid)):
                for col in range(len(shipGrid)):
                    color = (255,255,255)
                    if grid[row][col] == 1:
                        if shipGrid[row][col] != '~':
                            color = (103,214,17)
                        else:
                            color = (102,102,102)
                    pygame.draw.rect(self.screen,color,[(margin+width)*col + margin,
                                                        (margin+height)*row + margin,
                                                        width,
                                                        height])

            #Make most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    #Make a game instance and run the game
    bs = Battleship()
    bs.run_game()

