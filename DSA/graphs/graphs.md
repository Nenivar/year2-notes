# Graphs

## Implementation

Graphs can be implemented as either:

* Adjacency **Matrix**
* Adjacency **List** (Linked List)

Their runtimes are:

|                             | Adj. Matrix     | Adj. List              |
|-----------------------------|-----------------|------------------------|
|  Space                      | $\Theta$(`|V|`) | $\Theta$(`|V| + |E|`)  |
|  Edge u->v?                 | O(`1`)          | O(`deg(u)`)            |
| All edges leaving u $\in$ V | O(`V`)          | O(`deg(u)`)            |

> `deg(u)` is the number of edges leaving u

## Exploring a graph

Assume we use an adjacency **list**.

### Algorithm

```
Traverse(s):
    put s into the bag
    while the bag is not empty:
        take u from the bag
        if u unmarked:
            mark u
            for every edge (u,v):
                put v into the bag
```

#### Time-Complexity

* `put` $\in$ O(`1`)
* `take` $\in$ O(`1`)

We do at most `2|E|` put operations

$\rightarrow$ We do at most `2|E|`s take operationss

$\Rightarrow$ Overall time complexity is O(`|E|`)

> With an adjacency **matrix** this would have been O(`V`$^2$)

#### Implementation of Bag

* **Breadth**-first
    * Use a queue
* **Depth**-first
    * Use a stack

### Algorithm for Shortest Path (**breadth**-first)

Adjust the original algorithm to use a **queue**:

```
Traverse(s):
```

> These allow you to track the distance from each vertex

> It takes O(`|V|`) time to setup `dist`

```
    for all V, set dist(v) = ∞
    set dist(s) = 0
```

```
    put s into the queue
    while the queue is not empty:
        take u from the queue
        if u is not marked:
            mark u
            for every edge (u,v):
                put v into the bag
```

> This is complexity O(`1`) for each

```
                if dist(v) == ∞:
                    dist(v) = dist(u) + 1
```

This gives us a total time-complexity of O(`|E| + |V|`)