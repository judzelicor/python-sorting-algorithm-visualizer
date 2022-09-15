class Algorithms:
    def bubble_sort(self, visualizer, bins):
        is_sorted = False
        passes = len(bins) - 1

        while not is_sorted:
            is_sorted = True
            for i in range(passes):
                if (bins[i].get_value() > bins[i + 1].get_value()):
                    visualizer.bins_to_swap = [bins[i + 1], bins[i]]
                    visualizer.coors_to_swap = [bins[i + 1].x_coordinate, bins[i].x_coordinate]
                    visualizer.should_swap = True
                    is_sorted = False
                    temp = bins[i]
                    visualizer.bins[i] = bins[i + 1]
                    visualizer.bins[i + 1] = temp

                    yield bins

            passes -= 1