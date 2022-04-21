def hasPath_bfs(adj_list, src, dest, visited):

    q = deque()

    q.append(src)

    while len(q) > 0:

        top = q.popleft()

        if dest == top:
            return True

        for n in adj_list[top]:
            q.append(n)

    return False