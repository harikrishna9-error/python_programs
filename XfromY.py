import sys
from collections import deque

def main():
    X = sys.stdin.readline().strip()
    Y = sys.stdin.readline().strip()
    S, R = map(int, sys.stdin.readline().strip().split())
    
    len_x = len(X)
    revY = Y[::-1]

    # BFS state: (index in X, substrings count, Y_used count, revY_used count)
    queue = deque()
    queue.append((0, 0, 0, 0))  # starting from index 0

    visited = [None] * (len_x + 1)  # visited[i] = (min substrings to reach i, cost)

    substrings_Y = set()
    substrings_revY = set()
    len_y = len(Y)

    # Preprocess all substrings of Y and revY (limited up to len(Y))
    for i in range(len_y):
        for j in range(i + 1, len_y + 1):
            substrings_Y.add(Y[i:j])
            substrings_revY.add(revY[i:j])

    while queue:
        idx, total, y_used, ry_used = queue.popleft()

        if visited[idx] is not None:
            prev_total, prev_cost = visited[idx]
            curr_cost = y_used * S + ry_used * R
            if total > prev_total or (total == prev_total and curr_cost >= prev_cost):
                continue

        visited[idx] = (total, y_used * S + ry_used * R)

        # Try substrings of X starting at idx
        for j in range(idx + 1, min(len_x, idx + len_y) + 1):
            sub = X[idx:j]
            if sub in substrings_Y:
                queue.append((j, total + 1, y_used + 1, ry_used))
            if sub in substrings_revY:
                queue.append((j, total + 1, y_used, ry_used + 1))

    if visited[len_x] is None:
        print("Impossible")
    else:
        print(visited[len_x][1])


# Fast input-safe runner for CodeVita
if __name__ == "__main__":
    main()
