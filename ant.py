import random
from collections import deque

class Ant:
    def __init__(self, x, y, canvas, memory_size=5):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.memory_size = memory_size  # Adjust memory size as needed
        self.memory = deque(maxlen=memory_size) # Fixed-size queue to store memory

    def move(self):
        # Get adjacent cells
        adjacent_cells = self.get_adjacent_cells()
        # Filter out cells from memory to avoid small loops
        new_cells = [cell for cell in adjacent_cells if cell not in self.memory]
        # If there are no new cells, ignore memory this turn to avoid being trapped
        if not new_cells:
            new_cells = adjacent_cells

        # Calculate probabilities based on pheromone levels and memory
        probabilities = self.calculate_probabilities(new_cells)

        # Select next cell based on probabilities
        next_cell = self.choose_next_cell(new_cells, probabilities)
        self.update_position(*next_cell)

        # Update memory
        self.update_memory(next_cell)

        # Deposit pheromones
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

    def calculate_probabilities(self, cells, smoothing_factor=0.1):
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
        """Deposit pheromones on the current cell."""
        # Example: deposit a fixed amount of pheromone
        self.canvas.update_pheromone_level(self.x, self.y, amount=1)

# Example usage
# canvas = Canvas(width, height)
# ant = Ant(x, y, canvas)
