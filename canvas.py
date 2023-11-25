from sparse_grid import SparseGrid

class Canvas:
    def __init__(self, width, height):
        self.grid = SparseGrid(width, height)
        self.width = width
        self.height = height
        self.updated_cells = set()

    def place_food_source(self, x, y):
        self.grid.update_cell(x, y, 1)  # Assuming 1 indicates a food source

    def remove_food_source(self, x, y):
        self.grid.update_cell(x, y, 0)

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
        # Visualization logic
        pass