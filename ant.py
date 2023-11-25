import random
from collections import deque

class Ant:
    def __init__(self, x, y, canvas, memory_size=30, pheromone_deposit=1, active_pheromone_multiplier=5, active_mode_duration=50):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.memory_size = memory_size  # Adjust memory size as needed
        self.memory = deque(maxlen=memory_size) # Fixed-size queue to store memory
        self.active_mode = False
        self.pheromone_deposit = pheromone_deposit
        self.active_pheromone_multiplier = active_pheromone_multiplier
        self.active_mode_duration = active_mode_duration

    def move(self):
        adjacent_cells = self.get_adjacent_cells()
        new_cells = [cell for cell in adjacent_cells if cell not in self.memory] # filter the unvisited
        # If there are no new cells, ignore memory this turn to avoid being trapped
        if not new_cells:
            new_cells = adjacent_cells

        probabilities = self.calculate_probabilities(new_cells)
        next_cell = self.choose_next_cell(new_cells, probabilities)
        self.update_position(*next_cell)

        self.update_memory(next_cell)

        if self.detect_critical_point():
            self.active_mode = True
            self.active_mode_steps = self.active_mode_duration  # Reset the counter

        if self.active_mode:
            self.active_mode_steps -= 1
            if self.active_mode_steps <= 0:
                self.active_mode = False  # Turn off active mode after duration

        self.deposit_pheromones()

    def get_adjacent_cells(self):
        """Get coordinates of adjacent cells within the canvas boundaries."""
        adjacent = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # Skip the current cell
                new_x, new_y = self.x + dx, self.y + dy
                if 0 <= new_x < self.canvas.width and 0 <= new_y < self.canvas.height:
                    adjacent.append((new_x, new_y))
        return adjacent

    def calculate_probabilities(self, cells, smoothing_factor=0.01):
        """Calculate the probabilities for each cell based on pheromone levels with smoothing."""
        pheromone_levels = [self.canvas.get_pheromone_level(*cell) for cell in cells]

        # Apply smoothing to pheromone levels
        smoothed_levels = [level + smoothing_factor for level in pheromone_levels]
        total_pheromone = sum(smoothed_levels)

        # Calculate probabilities with smoothing applied
        probabilities = [level / total_pheromone for level in smoothed_levels]
        return probabilities
    def choose_next_cell(self, cells, probabilities):
        """Choose the next cell based on calculated probabilities."""
        return random.choices(cells, weights=probabilities, k=1)[0]

    def update_position(self, x, y):
        """Update the ant's position."""
        self.x, self.y = x, y

    def update_memory(self, new_cell):
        """Update the ant's memory with its current position."""
        # Add the new position to the memory
        self.memory.append(new_cell)

    def deposit_pheromones(self):
        # Deposit a higher amount of pheromones if in active mode, else deposit the standard amount
        deposit_amount = self.pheromone_deposit
        if self.active_mode:
            deposit_amount *= self.active_pheromone_multiplier
            # # TEST:peripheral deposit a little (guass bluring)
            # adjacent_cells = self.get_adjacent_cells()
            # for pos in adjacent_cells:
            #     self.canvas.update_pheromone_level(*pos, deposit_amount // 10)
        self.canvas.update_pheromone_level(self.x, self.y, deposit_amount)


    def detect_critical_point(self):
        # This method will check if the ant's current position is a critical point
        return (self.x, self.y) in self.canvas.critical_points

# Example usage
# canvas = Canvas(width, height)
# ant = Ant(x, y, canvas)
