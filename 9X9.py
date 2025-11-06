import sys
from typing import List, Tuple

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)

    raw = []
    for _ in range(9):
        row = [next(it) for _ in range(9)]
        raw.append(row)
    hint_list = list(map(int, [next(it) for _ in range(int(len(input_data) - 9*9 - 1))])) if False else None
    # above line dummy; we will instead reparse properly:
    # After 9x9 = 81 tokens, next tokens until last one except last is hint list, final is K.
    rest = list(it)
    K = int(rest[-1])
    hint_list = list(map(int, rest[:-1]))

    grid = [[0]*9 for _ in range(9)]
    original = [[0]*9 for _ in range(9)]
    fixed = [[False]*9 for _ in range(9)]
    is_hint = [[False]*9 for _ in range(9)]

    mutable_cells: List[Tuple[int,int]] = []

    for i in range(9):
        for j in range(9):
            s = raw[i][j]
            if s.endswith('0') and len(s) >= 2:  # hinted
                val = int(s[:-1])
                grid[i][j] = val
                original[i][j] = val
                is_hint[i][j] = True
                mutable_cells.append((i,j))
            elif s.startswith('0') and len(s) >= 2:  # Tina-filled
                val = int(s[1:])
                grid[i][j] = val
                original[i][j] = val
                mutable_cells.append((i,j))
            else:
                val = int(s)
                grid[i][j] = val
                original[i][j] = val
                fixed[i][j] = True  # cannot change

    # Helper
    def block_id(r,c):
        return (r//3)*3 + (c//3)

    # Used trackers
    row_used = [set() for _ in range(9)]
    col_used = [set() for _ in range(9)]
    block_used = [set() for _ in range(9)]

    # Initialize with all current assignments (including possible conflicts)
    for i in range(9):
        for j in range(9):
            v = grid[i][j]
            if v == 0:
                continue
            row_used[i].add(v)
            col_used[j].add(v)
            block_used[block_id(i,j)].add(v)

    best_diff = float('inf')
    best_assign = None

    # Precompute allowed set per mutable cell position (hinted restrict to hint_list)
    def legal_candidates(r,c):
        used = row_used[r] | col_used[c] | block_used[block_id(r,c)]
        if is_hint[r][c]:
            return [x for x in hint_list if x not in used]
        else:
            return [x for x in range(1,10) if x not in used]

    # Compute current diff
    def current_diff():
        d = 0
        for (i,j) in mutable_cells:
            if grid[i][j] != original[i][j]:
                d += 1
        return d

    # DFS with MRV
    def dfs():
        nonlocal best_diff, best_assign

        diff = current_diff()
        if diff >= best_diff:
            return
        if diff > K:
            return

        # Find mutable cell that violates or is unassigned or has smallest candidate set
        target = None
        min_cands = None
        min_len = 10

        # First, check if any current assignment causes local conflict: if so, prioritize fixing those
        conflict_cells = []
        for (r,c) in mutable_cells:
            val = grid[r][c]
            if val == 0:
                conflict_cells.append((r,c))
                continue
            # check duplicates in row/col/block
            cnt = 0
            for cc in range(9):
                if cc!=c and grid[r][cc]==val:
                    cnt +=1
            for rr in range(9):
                if rr!=r and grid[rr][c]==val:
                    cnt +=1
            br, bc = (r//3)*3, (c//3)*3
            for rr in range(br, br+3):
                for cc in range(bc, bc+3):
                    if (rr,cc)!=(r,c) and grid[rr][cc]==val:
                        cnt +=1
            if cnt > 0:
                conflict_cells.append((r,c))

        if conflict_cells:
            # pick among conflict cells the one with fewest legal candidates
            for (r,c) in conflict_cells:
                cands = legal_candidates(r,c)
                if len(cands) < min_len:
                    min_len = len(cands)
                    target = (r,c)
                    min_cands = cands
        else:
            # no local conflicts: pick un-fixed cell with minimal choices (could still improve diff)
            for (r,c) in mutable_cells:
                cands = legal_candidates(r,c)
                if len(cands) == 0:
                    return  # dead
                if len(cands) < min_len:
                    min_len = len(cands)
                    target = (r,c)
                    min_cands = cands

        if target is None:
            # All constraints locally satisfied; we have a candidate full assignment
            # Update best
            diff = current_diff()
            if diff < best_diff:
                best_diff = diff
                best_assign = [row[:] for row in grid]
            return

        r,c = target
        orig = grid[r][c]
        # Remove current from trackers if present
        if orig != 0:
            row_used[r].discard(orig)
            col_used[c].discard(orig)
            block_used[block_id(r,c)].discard(orig)

        for v in min_cands:
            # assign
            grid[r][c] = v
            row_used[r].add(v)
            col_used[c].add(v)
            block_used[block_id(r,c)].add(v)

            dfs()

            # undo
            row_used[r].discard(v)
            col_used[c].discard(v)
            block_used[block_id(r,c)].discard(v)
            grid[r][c] = orig

        # restore original in trackers
        if orig != 0:
            row_used[r].add(orig)
            col_used[c].add(orig)
            block_used[block_id(r,c)].add(orig)

    dfs()

    if best_assign is None:
        print("Impossible")
        return
    if best_diff == 0:
        print("Won")
        return
    if best_diff > K:
        print("Impossible")
        return

    # Output differing mutable cells in row-major order
    res = []
    for i in range(9):
        for j in range(9):
            if fixed[i][j]:
                continue
            if best_assign[i][j] != original[i][j]:
                res.append((i,j))
    for r,c in res:
        print(r, c)

if __name__ == "__main__":
    solve()
