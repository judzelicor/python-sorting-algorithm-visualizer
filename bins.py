from xmlrpc.client import Boolean
import pygame

class Bin:
    def __init__(self, visualizer, index, value, bin_unit_width, window):
        self.index = index
        self.colors = [
            (156, 163, 175),
            (209, 213, 219),
            (229, 231, 235)
        ]
        self.target_x = 0
        self.visualizer = visualizer
        self.window = window
        self.value = value
        self.should_swap = False
        self.has_swapped = False
        self.velocity = 0
        self.bin_unit_width = bin_unit_width
        self.max_height = self.window.height - self.window.Y_TOP_PADDING
        self.x_coordinate = round((self.window.X_PADDING / 2) + (self.index * self.bin_unit_width))
        self.y_coordinate = round(self.window.height - self.max_height * (self.value / self.visualizer.max_value))
        self.fill = self.colors[self.index % 3]
        self.width = bin_unit_width
        self.height = self.window.height - self.y_coordinate
        self.bin_rect = (self.x_coordinate, self.y_coordinate, self.width, self.height)
        self.initial_x = self.x_coordinate

    def get_value(self):
        return self.value

    def move(self, index):
        self.index = index
        self.fill = self.colors[index % 3]

    def draw(self):
        self.x_coordinate = round(self.x_coordinate + self.velocity)
        # print(self.target_x, self.value, self.x_coordinate)
        if self.x_coordinate == self.target_x:
            self.velocity = 0
            self.visualizer.should_swap = False

        pygame.draw.rect(self.window.display, self.fill, (self.x_coordinate, self.y_coordinate, self.width, self.height))