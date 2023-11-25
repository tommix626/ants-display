import random


class Ant:
    def __init__(self, x, y, canvas):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.memory = []  # Memory of last few positions
        self.memory_size = 5  # Adjust memory size as needed

    def move(self):
        # Get adjacent cells
        adjacent_cells = self.get_adjacent_cells()

        # Filter out cells in memory
        new_cells = [cell for cell in adjacent_cells if cell not in self.memory]

        if new_cells:
            # Select next cell based on pheromone levels
            next_cell = self.choose_next_cell(new_cells)
            self.update_position(*next_cell)

        # Update memory
        self.update_memory()

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

    def choose_next_cell(self, cells):
        """Choose the next cell based on pheromone levels."""
        # TODO: choose randomly for now, can be improved with pheromone-based logic
        return random.choice(cells)

    def update_position(self, x, y):
        """Update the ant's position."""
        self.x, self.y = x, y

    def update_memory(self):
        """Update the ant's memory with its current position."""
        self.memory.append((self.x, self.y))
        if len(self.memory) > self.memory_size:
            self.memory.pop(0)

    def deposit_pheromones(self):
        """Deposit pheromones on the current cell."""
        # Example: deposit a fixed amount of pheromone
        self.canvas.update_pheromone_level(self.x, self.y, amount=1)

# Example usage
# canvas = Canvas(width, height)
# ant = Ant(x, y, canvas)
