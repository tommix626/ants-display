from scipy.sparse import dok_matrix

class SparseGrid:
    def __init__(self, width, height):
        self.grid = dok_matrix((width, height), dtype=float)

    def update_cell(self, x, y, value):
        """Update the value at a specific cell."""
        self.grid[x, y] = value

    def get_cell(self, x, y):
        """Get the value at a specific cell."""
        return self.grid[x, y]

    def get_nonzero_cells(self):
        """Return a list of coordinates and values of non-zero cells."""
        return [(item[0], item[1], self.grid[item]) for item in self.grid.keys()]

    def reset(self):
        """Reset the grid to all zeros."""
        self.grid = dok_matrix(self.grid.shape, dtype=float)
