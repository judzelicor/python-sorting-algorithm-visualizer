import random
from bins import Bin
from algorithms import Algorithms

class Visualizer:
    """
    This class contains the the bins that are to be sorted
    """
    def __init__(self, window):
        self.algorithm = Algorithms()
        self.window = window
        self.bin_count = 7
        self.min_fence = 0
        self.max_fence = 100
        self.generic_list = self.generate_generic_list(self.bin_count, self.min_fence, self.max_fence)
        self.min_value = min(self.generic_list)
        self.max_value = max(self.generic_list)
        self.bin_unit_width = round((self.window.width - self.window.X_PADDING) / self.bin_count)
        self.bin_unit_height = 200
        self.bins = self.generate_bins(self.generic_list)
        self.is_swapping = False
        self.is_sorting = True
        self.should_swap = False
        self.bins_to_swap = []
        self.coors_to_swap = []

    def sort(self):
        print(self.should_swap)
        if (self.is_sorting and self.should_swap):
            self.bins_to_swap = []
            self.coors_to_swap = []
            try:
                # self.bins = next(self.algorithm.bubble_sort(self, self.bins))
                next(self.algorithm.bubble_sort(self, self.bins))
                # for bin in self.bins:
                #     print(bin.get_value())
            except:
                pass
        else:
            self.bins_to_swap[0].velocity = -2
            self.bins_to_swap[0].target_x = self.coors_to_swap[1]
            self.bins_to_swap[1].velocity = 2
            self.bins_to_swap[1].target_x = self.coors_to_swap[0]

    def draw(self):
        bins = self.bins

        for bin in bins:
            bin.draw()

    def generate_generic_list(self, value_count, min_fence, max_fence):
        generic_list = []

        for index in range(value_count):
            value = random.randint(min_fence, max_fence)
            generic_list.append(value)
        
        return generic_list

    def generate_bins(self, generic_list):
        bins = []

        for index, value in enumerate(generic_list):
            bin = Bin(self, index, value, self.bin_unit_width, self.window)
            bins.append(bin)
        
        return bins


# https://stackoverflow.com/questions/49991443/how-do-i-animate-a-rectangle-in-pygame-to-move-from-side-to-side-forever