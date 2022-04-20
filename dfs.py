def dfs(grid, i, j, m, n, visited):
    if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or \
            grid[i][j] == 'W':
        return False

    visited.add((i, j))

    dfs(grid, i + 1, j, m, n, visited)
    dfs(grid, i - 1, j, m, n, visited)
    dfs(grid, i, j + 1, m, n, visited)
    dfs(grid, i, j - 1, m, n, visited)

    return True