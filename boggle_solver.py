class Boggle:
    def __init__(self, grid=None, dictionary=None):
        self.grid = grid if grid else []

        if dictionary:
            self.dictionary = {
                word.upper() for word in dictionary
            }
        else:
            self.dictionary = set()

        self.solution = []
        self.prefixes = set()

        for word in self.dictionary:
            for i in range(1, len(word) + 1):
                self.prefixes.add(word[:i])

    def setGrid(self, grid):
        self.grid = grid

    def setDictionary(self, dictionary):
        self.dictionary = {word.upper() for word in dictionary}
        self.prefixes = set()

        for word in self.dictionary:
            for i in range(1, len(word) + 1):
                self.prefixes.add(word[:i])

    def getSolution(self):
        self.solution = []
        found = set()
        rows = len(self.grid)
        cols = len(self.grid[0]) if rows > 0 else 0

        # DFS helper
        def dfs(r, c, visited, word):
            word_upper = word.upper()

            # Stop early if prefix not valid
            if word_upper not in self.prefixes:
                return

            # Valid Boggle word must be length >= 3
            if len(word_upper) >= 3 and word_upper in self.dictionary:
                found.add(word_upper)

            directions = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1), (1, 0), (1, 1)
            ]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                in_bounds = (0 <= nr < rows and 0 <= nc < cols)

                if in_bounds and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    dfs(nr, nc, visited, word + self.grid[nr][nc])
                    visited.remove((nr, nc))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, {(r, c)}, self.grid[r][c])

        self.solution = sorted(list(found))
        return self.solution


if __name__ == "__main__":
    grid = [
        ["Qu", "A", "T", "S"],
        ["E", "R", "I", "O"],
        ["N", "L", "St", "P"],
        ["M", "U", "C", "K"]
    ]

    dictionary = [
        "QUAIL", "QUIET", "TRIO", "CUP",
        "STORM", "MOP", "STICK", "RUM",
        "TAR", "QUIP"
    ]

    game = Boggle(grid, dictionary)
    words = game.getSolution()
    print("Found words:", words)
