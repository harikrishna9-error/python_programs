from collections import deque

def main():
    # Read input
    M, N = map(int, input().split())
    grid = []
    for _ in range(M):
        grid.append(list(map(int, input().split())))
    src_x, src_y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())
    dx, dy = map(int, input().split())
    
    # Directions: [forward, right, left, backward]
    directions = [
        (dx, dy),
        (dy, -dx),
        (-dy, dx),
        (-dx, -dy)
    ]
    
    # BFS setup
    queue = deque([(src_x, src_y, 0)])
    visited = set([(src_x, src_y)])
    
    while queue:
        x, y, moves = queue.popleft()
        
        # Check if reached destination
        if x == dest_x and y == dest_y:
            print(moves)
            return
        
        # Try all 4 possible moves
        for move_x, move_y in directions:
            new_x = x + move_x
            new_y = y + move_y
            
            # Check boundaries and cell value
            if 0 <= new_x < M and 0 <= new_y < N and grid[new_x][new_y] == 0:
                if (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, moves + 1))
    
    # If destination not reachable
    print(-1)

if __name__ == "__main__":
    main()
