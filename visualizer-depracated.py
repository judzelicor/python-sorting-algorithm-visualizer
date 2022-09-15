import pygame
import random
import time
import sort

class Bin:
    def __init__(self, window, index, value, bin_width, bin_height):
        self.index = index
        self.window = window
        self.visualizer = self.window.visualizer
        self.value = value
        self.maximum_height = self.window.height - self.window.Y_TOP_PADDING
        self.y_coordinate = round(self.window.height - self.maximum_height * (self.value / self.visualizer.max_value))
        self.width = bin_width
        self.height = self.window.height - self.y_coordinate
        self.x_coordinate = round(self.window.left_boundary + (self.index * self.width))
        self.fill = self.window.GRAYS[self.index % 3]
        self.velocity = 0
        self.should_swap = False

    def render(self):
        if (self.should_swap):
            self.x_coordinate += self.velocity

        pygame.draw.rect(self.window.display, self.fill, (self.x_coordinate, self.y_coordinate, self.width, self.height))

class Window:
    def __init__(self, width, height, generic_list):
        self.FPS = 60
        self.BLACK = 20, 20, 20
        self.WHITE = 250, 250, 250
        self.GREEN = 49, 145, 119
        self.RED = 237, 41, 57
        self.X_PADDING = 200
        self.Y_TOP_PADDING = 150
        self.GRAYS = [
            (156, 163, 175),
            (209, 213, 219),
            (229, 231, 235)
        ]
        self.BACKGROUND_COLOR = self.WHITE

        self.width = width
        self.height = height
        self.left_boundary = self.X_PADDING // 2
        self.display = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.visualizer = Visualizer(self, generic_list)
        self.sort = Sort(self, self.visualizer)
        self.count = 0

        pygame.display.set_caption("Sorting Algorithm Visualizer")

    def draw(self, dt):
        self.display.fill(self.BACKGROUND_COLOR)

        self.draw_bins()

    def draw_bins(self):
        generic_list = self.visualizer.generic_list

        for index, value in enumerate(generic_list):
            bin = Bin(self, index, value, self.visualizer.bin_width, self.visualizer.bin_height)

            bin.render()

    def restart(self):
        self.visualizer.generic_list = generic_list_generator()
        self.sort.is_sorting = False

    def handleKeypress(self, key):
        if (key == pygame.K_r):
            self.restart()

        elif (key == pygame.K_a) and not self.sort.is_sorting:
            self.sort.sort_order = "ASC"
        
        elif (key == pygame.K_d) and not self.sort.is_sorting:
            self.sort.sort_order = "DESC"

        elif (key == pygame.K_SPACE) and not self.sort.is_sorting:
            self.sort.is_sorting = True
            self.sort.bubble_sort(self.visualizer.generic_list)

    def render(self):
        prev_time = time.time()

        while self.is_running:
            self.clock.tick(self.FPS)

            now = time.time()
            dt = now - prev_time
            prev_time = now
            print(self.visualizer.generic_list)

            if (self.sort.is_sorting and not self.sort.is_swapping):
                try:
                    if self.count % 30 == 0:
                        next(self.sort.bubble_sort(self.visualizer.generic_list))
                    self.count += 1
                except:
                    pass

            self.draw(dt)

            pygame.display.update()

            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.is_running = False

                elif event.type == pygame.KEYDOWN:
                    self.handleKeypress(event.key)
                
        pygame.quit()


class Visualizer:
    def __init__(self, window, generic_list):
        pygame.init()
        self.window = window
        self.generic_list = generic_list
        self.min_value = min(self.generic_list)
        self.max_value = max(self.generic_list)
        self.bin_width = round((self.window.width - self.window.X_PADDING) / len(self.generic_list))
        self.bin_height = round((self.window.height - self.window.Y_TOP_PADDING) / (self.max_value - self.min_value))

    def swap(self):
        print(self.window.sort.bins_to_swap)
        pass

class Sort:
    def __init__(self, window, visualizer):
        self.window = window
        self.visualizer = visualizer
        self.is_sorting = False
        self.sort_order = "ASC"
        self.is_swapping = False
        self.bins_to_swap = []

    def start(self):
        pass

    def bubble_sort(self, generic_list):
        is_sorted = False
        passes = len(generic_list) - 1

        while not is_sorted:
            is_sorted = True
            for i in range(passes):
                if (generic_list[i] > generic_list[i + 1]):
                    temp = generic_list[i]
                    generic_list[i] = generic_list[i + 1]
                    generic_list[i + 1] = temp
                    # self.is_swapping = True
                    is_sorted = False
                    self.visualizer.generic_list = generic_list
                    self.bins_to_swap.append(generic_list[i])
                    self.bins_to_swap.append(generic_list[i + 1])
                    yield True
            passes -= 1



def generic_list_generator(n = 40, min_value = 0, max_value = 100):
    generic_list = []

    for _ in range(n):
        value = random.randint(min_value, max_value)
        generic_list.append(value)

    return generic_list


def main():
    bin_count = 16
    bin_min_value = 0
    bin_max_value = 100
    window_width = 1080
    window_height = 720
    generic_list = generic_list_generator(bin_count, bin_min_value, bin_max_value)

    window = Window(window_width, window_height, generic_list)
    window.render()


if __name__ == "__main__":
    main()