from visualizer import Visualizer

import pygame
pygame.init()

class Window:
    def __init__(self):
        self.X_PADDING = 200
        self.Y_TOP_PADDING = 200
        self.width = 1080
        self.height = 720
        self.white = 255, 255, 255
        self.BACKGROUND_COLOR = self.white
        self.display = pygame.display.set_mode((self.width, self.height))
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.visualizer = Visualizer(self)

        pygame.display.set_caption("Sorting Algorithm Visualizer")

    def draw(self):
        bins = self.visualizer.bins
        self.display.fill(self.BACKGROUND_COLOR)

        self.visualizer.sort()

        for bin in bins:
            bin.draw()
            
        pygame.display.update()


    def render(self):
        while self.is_running:
            self.clock.tick(60)

            self.draw()

            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.is_running = False
                
        pygame.quit()

window = Window()

if __name__ == "__main__":
    window = Window()

    window.render()


# https://pygame.readthedocs.io/en/latest/10_games/games.html