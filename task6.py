class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    # A utility function to check if the current color assignment is safe for vertex v
    def is_safe(self, v, color, c):
        for i in range(self.v):
            # Check if vertex 'i' is adjacent to 'v' and if 'i' already has color 'c'
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    # A recursive utility function to solve m-coloring problem using backtracking
    def graph_color_util(self, m, color, v):
        # Base case: If all vertices are assigned a color, then return true
        if v == self.v:
            return True

        for c in range(1, m + 1):
            # Check if assignment of color 'c' to 'v' is safe
            if self.is_safe(v, color, c):
                color[v] = c
                # Recur for the next vertex
                if self.graph_color_util(m, color, v + 1):
                    return True
                # If assigning color 'c' doesn't lead to a solution, backtrack
                color[v] = 0

    def graph_coloring(self, m):
        # Initialize all color values as 0 (no color assigned)
        color = [0] * self.v
        
        # Call graph_color_util() for vertex 0
        if not self.graph_color_util(m, color, 0):
            print("Solution does not exist")
            return False

        # If a solution exists, print it
        print("Solution exists and following are the assigned colors:")
        for c in color:
            print(c, end=" ")
        print() # For a newline at the end
        return True

# Driver Code
if __name__ == '__main__':
    g = Graph(4)
    g.graph = [[0, 1, 1, 1], 
               [1, 0, 1, 0], 
               [1, 1, 0, 1], 
               [1, 0, 1, 0]]
    m = 3 # Number of colors
    
    # Function call
    g.graph_coloring(m)