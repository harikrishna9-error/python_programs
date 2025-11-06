import sys

def solve():
    try:
        n, c = map(int, sys.stdin.readline().strip().split())
        
        adj = [set() for _ in range(n + 1)]
        conflicting_employees = set()

        for _ in range(c):
            u, v = map(int, sys.stdin.readline().strip().split())
            adj[u].add(v)
            adj[v].add(u)
            conflicting_employees.add(u)
            conflicting_employees.add(v)

        expertise = [0] + list(map(int, sys.stdin.readline().strip().split()))

    except (IOError, ValueError):
        return

    total_expertise = 0
    visited = [False] * (n + 1)
    
    memo = {}

    def solve_mw_is(employees_list):
        state = tuple(sorted(employees_list))
        if not employees_list:
            return 0
        
        if state in memo:
            return memo[state]
            
        first_employee = employees_list[0]
        
        # Case 1: Don't select first_employee
        res1 = solve_mw_is(employees_list[1:])
        
        # Case 2: Select first_employee
        conflicts_of_first = adj[first_employee]
        remaining_employees = [emp for emp in employees_list[1:] if emp not in conflicts_of_first]
        res2 = expertise[first_employee] + solve_mw_is(remaining_employees)
        
        result = max(res1, res2)
        memo[state] = result
        return result

    for i in range(1, n + 1):
        if i not in conflicting_employees:
            total_expertise += expertise[i]
        elif i in conflicting_employees and not visited[i]:
            component = []
            queue = [i]
            visited[i] = True
            
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                component.append(u)
                
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
            
            total_expertise += solve_mw_is(component)

    print(total_expertise)

if __name__ == "__main__":
    solve()
