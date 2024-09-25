from collections import deque

def solve_maze(maze):
    start = None
    end = None
    rows, cols = len(maze), len(maze[0])
    
    # Find start and end positions
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)
    
    if not start or not end:
        return None
    
    # BFS to find the shortest path
    queue = deque([(start, [])])
    visited = set()
    
    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) == end:
            return path
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, down, left, up
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
                queue.append(((nx, ny), path + [(nx, ny)]))
    
    return None

# Example usage
maze = [
    ['S', '.', '#', '#', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '#', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['#', '#', '#', '#', '#', '.', 'E']
]

solution = solve_maze(maze)

if solution:
    print("Path found:")
    for x, y in solution:
        maze[x][y] = '*'
    maze[solution[-1][0]][solution[-1][1]] = 'E'
    for row in maze:
        print(''.join(row))
else:
    print("No solution found.")