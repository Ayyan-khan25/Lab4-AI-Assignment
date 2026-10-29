import heapq

def search(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    processed = []
    expanded = []

    while pq:
        f, g, node, path = heapq.heappop(pq)

        # Ignore outdated queue entries (stale entries).
        if g != best[node]:
            continue

        processed.append(node)  # goal processing is recorded
        if node == goal:
            return g, path, processed, expanded

        # Count expansion only when successors are examined.
        expanded.append(node)
        for nxt, weight in graph.get(node, []):
            new_g = g + weight
            if new_g < best.get(nxt, float("inf")):
                best[nxt] = new_g
                heapq.heappush(
                    pq, (new_g + h[nxt], new_g, nxt, path + [nxt])
                )

    return None, [], processed, expanded

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

heuristic = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}
zero_h = {node: 0 for node in graph}

print("A*:", search(graph, heuristic, "S", "G"))
print("UCS:", search(graph, zero_h, "S", "G"))
