# Lab4-AI-Assignment
# Lab 4: Informed Search — Heuristics & A*

**Course:** Artificial Intelligence Lab (CAI601400)  
**Week:** 4  
**Lectures:** L7–L8  
**CLO:** CLO2 (C3: Apply)

## Objective
To understand heuristic evaluation functions, manually trace A* search, compare A* with Uniform-Cost Search (UCS), and investigate how an overestimating heuristic can affect optimality.

## Graph Used

The same weighted graph is used for all three tasks.

```text
S → A (1)
S → B (4)
A → C (2)
B → G (5)
C → G (3)
```

**Start Node:** S  
**Goal Node:** G

### Supplied Heuristic Values

| Node | h(n) |
|---|---:|
| S | 5 |
| A | 4 |
| B | 4 |
| C | 2 |
| G | 0 |

A* uses the evaluation function:

`f(n) = g(n) + h(n)`

Where:
- `g(n)` is the actual path cost from the start node.
- `h(n)` is the estimated remaining cost to the goal.
- `f(n)` is the estimated total path cost.

## Task 1: Manual A* Trace

The first three expansions are:

| Expansion | Selected Node | g(n) | h(n) | f(n) |
|---|---|---:|---:|---:|
| 1 | S | 0 | 5 | 5 |
| 2 | A | 1 | 4 | 5 |
| 3 | C | 3 | 2 | 5 |

After expanding S, the frontier contains A (f = 5) and B (f = 8). A is selected because it has the lower f-value.

After expanding A, the frontier contains C (f = 5) and B (f = 8). C is selected next.

After expanding C, the frontier contains G (f = 6) and B (f = 8). Therefore, G is selected next.

**Final Path:** S → A → C → G  
**Total Cost:** 1 + 2 + 3 = 6

Task 1 is completed through manual calculations and frontier tracing; code is not required for this task.

## Task 2: A* vs Uniform-Cost Search (UCS)

A* is executed with the supplied heuristic. UCS is executed using a zero heuristic for every node.

### Results

| Measure | A* | UCS |
|---|---|---|
| Returned Path | S → A → C → G | S → A → C → G |
| Path Cost | 6 | 6 |
| Processed Nodes | S, A, C, G | S, A, B, C, G |
| Expanded Nodes | S, A, C | S, A, B, C |
| Expansion Count | 3 | 4 |

The path cost is independently calculated as:

`S → A → C → G = 1 + 2 + 3 = 6`

A* expands three nodes, while UCS expands four nodes. Both find the optimal path, but A* expands one fewer node on this graph.

**Counting convention:** A node is counted as expanded when its successors are examined. The goal is recorded as processed but is not included in the expansion count. Stale priority-queue entries are ignored.

## Task 3: Heuristic Overestimation

In this experiment, only the heuristic value of node C is changed.

- Original value: `h(C) = 2`
- Modified value: `h(C) = 10`
- True remaining cost from C to G: `3`

Since `10 > 3`, the modified heuristic overestimates the actual remaining cost and is not admissible.

### Results After Modification

| Measure | Result |
|---|---|
| Returned Path | S → B → G |
| Path Cost | 4 + 5 = 9 |
| Processed Nodes | S, A, B, G |
| Expanded Nodes | S, A, B |
| Expansion Count | 3 |

With the modified heuristic, C receives `f(C) = 3 + 10 = 13`. The goal reached through B has `f(G) = 9`, so G is selected before C. A* consequently returns a path of cost 9 instead of the optimal cost 6.

This experiment demonstrates that an overestimating heuristic can cause A* to return a suboptimal path. Overestimation removes the usual optimality guarantee, although it does not necessarily produce an incorrect result in every individual run.

## Conclusion

This lab demonstrates how A* combines actual path costs with heuristic estimates to guide search. The comparison with UCS shows that a useful heuristic can reduce node expansions on a particular graph. The overestimation experiment illustrates why heuristic quality matters when optimality is required.

**Technologies Used:** Python, `heapq` priority queue, A* Search, Uniform-Cost Search.

**File:** `week4_astar.py` (Python implementation for Tasks 2 and 3).
