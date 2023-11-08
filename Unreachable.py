def count_minimum_unreachable_warehouses(warehouse_nodes, warehouse_from, warehouse_to):
    def build_graph(n, from_list, to_list):
        graph = [[] for _ in range(n)]
        for i in range(len(from_list)):
            graph[from_list[i] - 1].append(to_list[i] - 1)
            graph[to_list[i] - 1].append(from_list[i] - 1)
        return graph

    def traverse(current, graph, visited, track):
        if track[current]:
            return True
        if visited[current]:
            return False
        visited[current] = True
        track[current] = True
        answer = False
        for next_node in graph[current]:
            graph[next_node].remove(current)
            temp = traverse(next_node, graph, visited, track)
            if temp:
                answer = True
        track[current] = False
        return answer

    graph = build_graph(warehouse_nodes, warehouse_from, warehouse_to)
    visited = [False] * warehouse_nodes
    count = 0

    for i in range(warehouse_nodes):
        if visited[i]:
            continue
        temp = traverse(i, graph, visited, [False] * warehouse_nodes)
        if not temp:
            count += 1

    return count