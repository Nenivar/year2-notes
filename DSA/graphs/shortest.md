# Single Shortest Path

---

## Priority Queues

> Q contains **distinct** elements x (each with a key)
> 
> Supports:
> * ```insert(x, k)```: inserts `x` with `x.key = k`
> * ```decreaseKey(x, k)```: sets `x.key = k` where `x.key < k`
> * ```extractMin()```: removes & returns element with the **smallest key**

### Implementation

#### Unsorted Linked List

|op. | insert | decreaseKey | extractMin |
|-|-|-|-|
|time | $\mathbb{O}(1)$ | $\mathbb{O}(n)$ | $\mathbb{O}(n)$ |

![](../assets/graphs/shortest_1.png)

Adding item on head is easy - searching for item is hard!

#### Sorted Linked List

|op. | insert | decreaseKey | extractMin |
|-|-|-|-|
|time | $\mathbb{O}(n)$ | $\mathbb{O}(n)$ | $\mathbb{O}(1)$ |

Extract min is easy (remove head of list) - increase/decrease key is hard!

![](../assets/graphs/shortest_2.png)

#### Binary Heap

> Any element has a key **less than or equal to** the keys of its children

![](../assets/graphs/shortest_3.png)

Can be stored implicitly as an array:
![](../assets/graphs/shortest_4.png)

##### Assumption

This relies on the assumption that **we can find the location of any element `x` in the heap in $\mathbb{O}(1)$ time**

> Given each element `x` also has an ass. unique +ve int id; $x.id \leq N$

![](../assets/graphs/shortest_6.png)

##### Decrease Key

`decreaseKey(x, k)`

> |Step|Time
> |-|-|
> | 1. Find element `x` |$\mathbb{O}(1)$|
> | 2. Check that $k \leq  x.key$ |$\mathbb{O}(1)$|
> | 3. Set `x.key = k`|$\mathbb{O}(1)$|
> | 4. While `x.key < parent.key`:<br> swap x w/ parent<br>*(stop if `x = root`)*  | Each swap: $\mathbb{O}(1)$;<br>Height of tree=$\mathbb{O}(\log n);$<br>$\log n$ swaps|

$\mathbb{O}(\log n)$ time

##### Insert

`insert(x, k)`

> |Step|Time
> |-|-|
> | 1. Put `x` in next free slot |$\mathbb{O}(1)$|
> | 2. Run `decreaseKey(x, k)` |$\mathbb{O}(\log n)$|

$\mathbb{O}(\log n)$ time

##### ExtractMin

`extractMin()`

> |Step|Time
> |-|-|
> | 1. Extract element at root |$\mathbb{O}(1)$|
> | 2. Root = rightmost element in bottom level (`y`) |$\mathbb{O}(1)$|
> | 3. While `y.key > children.any`:<br>swap `y` w/ child with smaller key<br>*(stop if `y` becomes a leaf)*  |$\mathbb{O}(1)$<br>Height of tree is $\mathbb{O}(\log n)$|

$\mathbb{O}(\log n)$ time

### Summary

![](../assets/graphs/shortest_5.png)

### Heapsort

Sorting array `arr` -> `newArr`

(Given queue is a **binary heap**)

1. `|arr| = n`
1. insert every element into a priority queue
1. `extractmin` from queue `n` times
    * put elements in `newArr` in order they come out

$\mathbb{O}(n \log n)$ time

---

## Dijkstra's Algorithm