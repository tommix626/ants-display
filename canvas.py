from image_processor import ImageProcessor
from sparse_grid import SparseGrid
import matplotlib.pyplot as plt
import numpy as np

class Canvas:
    def __init__(self, width, height):
        self.grid = SparseGrid(width, height)
        self.width = width
        self.height = height
        self.updated_cells = set()
        self.critical_points = set()
        #ploting
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.im = None
        self.ants_plot = None
        self.food_plot = None
        # self.ax.invert_yaxis()

    def place_food_source(self, x, y):
        # self.grid.update_cell(x, y, 1)  # Assuming 1 indicates a food source
        self.critical_points.add((x, y))

    def remove_food_source(self, x, y):
        self.grid.update_cell(x, y, 0)
        self.critical_points.discard((x, y))

    def update_pheromone_level(self, x, y, amount):
        current_level = self.grid.get_cell(x, y)
        self.grid.update_cell(x, y, current_level + amount)
        self.updated_cells.add((x, y))

    def evaporate_pheromones(self, lin_evap_rate, exp_evap_rate):
        for x, y in self.updated_cells:
            current_level = self.grid.get_cell(x, y)
            new_level = min(current_level - lin_evap_rate, current_level * (exp_evap_rate))
            new_level = max(new_level, 0)
            self.grid.update_cell(x, y, new_level)
        self.updated_cells.clear()

    def get_pheromone_level(self, x, y):
        return self.grid.get_cell(x, y)

    def draw_canvas(self):
        # Convert the sparse grid to a dense format for plotting
        dense_grid = self.grid.grid.toarray()

        # Create a plot
        plt.figure(figsize=(10, 10))
        plt.imshow(dense_grid, cmap='hot', interpolation='nearest')

        # Mark the ants on the grid (adjust for the flipped y-coordinates)
        ant_x, ant_y = zip(*[(ant.x, self.height - ant.y - 1) for ant in ants])
        plt.scatter(ant_y, ant_x, c='white', alpha=0.6, s=20)

        # Mark the food sources with larger dots (adjust for the flipped y-coordinates)
        for x, y in self.critical_points:
            plt.scatter(y, self.height - x - 1, c='blue', s=50)
        plt.scatter(2, 2, c='white', s=100)
        plt.colorbar()
        plt.title("Ant Colony Canvas")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.show()
    def draw_canvas_all(self,ants):
        # Convert the sparse grid to a dense format for plotting
        dense_grid = self.grid.grid.toarray()

        # Create a plot
        plt.figure(figsize=(10, 10))
        plt.imshow(dense_grid, cmap='hot', interpolation='nearest')

        # Mark the ants on the grid
        ant_x, ant_y = zip(*[(ant.x, ant.y) for ant in ants])
        plt.scatter(ant_y, ant_x, c='white', alpha=0.6, s=20)  # White dots with transparency

        # Mark the food sources with larger blue dots
        for x, y in self.critical_points:
            plt.scatter(y, x, c='blue', s=50)  # Larger blue dots for critical points

        plt.colorbar()  # Show pheromone intensity scale
        plt.title("Ant Colony Canvas")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.gca().invert_yaxis()  # Invert Y-axis to match grid orientation
        plt.show()

    def draw_canvas_update(self, ants):
        # Convert the sparse grid to a dense format for plotting
        dense_grid = self.grid.grid.toarray()

        # Initialize or update the imshow plot
        if self.im is None:
            self.im = self.ax.imshow(dense_grid, cmap='hot', interpolation='nearest', vmin=0, vmax=dense_grid.max())
            plt.colorbar(self.im, ax=self.ax)
        else:
            self.im.set_data(dense_grid)
            self.im.set_clim(vmin=0, vmax=dense_grid.max())  # Adjust color limits if necessary
            # self.im.set_clim(vmin=0, vmax=200)  # Adjust color limits if necessary

        # Mark the ants on the grid
        ant_x, ant_y = zip(*[(ant.x, ant.y) for ant in ants])
        if self.ants_plot is None:
            self.ants_plot = self.ax.scatter(ant_y, ant_x, c='white', alpha=0.6, s=20)
        else:
            self.ants_plot.set_offsets(np.c_[ant_y, ant_x])

        # # Mark the food sources with larger blue dots
        # food_x, food_y = zip(*self.critical_points)
        # if self.food_plot is None:
        #     self.food_plot = self.ax.scatter(food_y, food_x, c='blue', s=5)
        # else:
        #     self.food_plot.set_offsets(np.c_[food_y, food_x])

        # Update the plot
        self.ax.set_title("Ant Colony Canvas")
        self.ax.set_xlabel(ImageProcessor.get_current_time())
        self.ax.set_ylabel("Y-axis")
        plt.draw()
        plt.pause(0.00001)  # Pause to allow the plot to update

    def clear_critical_points(self):
        self.critical_points.clear()  # Clear the set of critical points