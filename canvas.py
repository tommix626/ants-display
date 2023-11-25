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

    def place_food_source(self, x, y):
        self.grid.update_cell(x, y, 1)  # Assuming 1 indicates a food source
        self.critical_points.add((x, y))

    def remove_food_source(self, x, y):
        self.grid.update_cell(x, y, 0)
        self.critical_points.discard((x, y))

    def update_pheromone_level(self, x, y, amount):
        current_level = self.grid.get_cell(x, y)
        self.grid.update_cell(x, y, current_level + amount)
        self.updated_cells.add((x, y))

    def evaporate_pheromones(self, evaporation_rate):
        for x, y in self.updated_cells:
            current_level = self.grid.get_cell(x, y)
            new_level = max(current_level - evaporation_rate, 0)
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

    def clear_critical_points(self):
        self.critical_points.clear()  # Clear the set of critical points