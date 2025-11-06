def parse_value(value):
    if value.startswith("0"):
        return int(value[1:]), 'filled'
    elif value.endswith("0"):
        return int(value[:-1]), 'hinted'
    else:
        return int(value), 'fixed'

def is_valid(grid, r, c, val):
    for i in range(9):
        if grid[r][i] == val and i != c:
            return False
        if grid[i][c] == val and i != r:
            return False
    start_r, start_c = 3 * (r // 3), 3 * (c // 3)
    for i in range(start_r, start_r + 3):
        for j in range(start_c, start_c + 3):
            if grid[i][j] == val and (i != r or j != c):
                return False
    return True

def main():
    grid = []
    types = []
    for _ in range(9):
        row = input().strip().split()
        grid_row = []
        type_row = []
        for val in row:
            num, cell_type = parse_value(val)
            grid_row.append(num)
            type_row.append(cell_type)
        grid.append(grid_row)
        types.append(type_row)
    
    allowed_hints = set(map(int, input().split()))
    k = int(input().strip())

    wrong_cells = []
    for r in range(9):
        for c in range(9):
            val = grid[r][c]
            cell_type = types[r][c]
            if not is_valid(grid, r, c, val):
                if cell_type == 'filled':
                    wrong_cells.append((r, c))
                elif cell_type == 'hinted' and val in allowed_hints:
                    wrong_cells.append((r, c))

    if not wrong_cells:
        print("Won")
    elif len(wrong_cells) > k:
        print("Impossible")
    else:
        for r, c in sorted(wrong_cells):
            print(f"{r} {c}")

if __name__ == "__main__":
    main()
