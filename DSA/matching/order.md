# Order Statistics

> #### Selection Problem:
> Select $i^{th}$ smallest of $n$ elements
> 
> * minimum: $i = 1$
> * maximum: $i = n$
> * median: $i = \lfloor \frac{n+1}{2} \rfloor$ or $i = \lceil \frac{n+1}{2} \rceil$

###  Simple solution:

Sort input and pick $i^th$ element of sorted array, e.g. with merge sort for $O(n \log n)$

But we can do better!

---

## Randomized Partition Algorithm

### Partition

Rearranges a list so that all elements to the **left** of the pivot are *less than* the pivot, all elements to the **right** of the pivot are *more than* the pivot.

```
PARTITION(A: [], p: int, r: int) -> int:
    pick q in range(p, r) -- somehow
    x = A[q]
    swap A[q] and A[r]
    i = p-1
    for j=p to r-1
        if A[j] <= x
            i = i + 1
            swap A[i] and A[j]
    swap A[i + 1] and A[r]
    return i+1 -- index of the pivot
```

* where `p` is the start of the section to be partitioned
* `r` is the end of the section to be partitioned

#### Analysis

Invariants at the start of each iteration:
* $A[k] \leq x$ for $p \leq k \leq i$
* $A[k] > x$ for $i < k < j$
* $A[r] = x$

Start of first iteration:
* $i = p-1$
* $j = p$
* $A[r] = x$

Terminates with:
* $A[k] \leq x$ for $p \leq k \leq i$
* $A[k] > x$ for $i + 1 < k \leq r$
* $A[i + 1] = x$

### Rand-Select

Use `PARTITION` repeatedly to find the $i^th$ smallest element of `A`

1. pick a pivot randomly
2. partition according to the pivot
3. only need to look in one 'side' of the array to find the $i^th$ smallest element
4. repeat until:
   * we happen to pick the $i^th$ smallest element as a pivot
   * the side we have to look in only has one element

```
RAND_SELECT(A: [], p: int, r: int, i: int) -> int:
    if p == r:
        return A[p]
    
    q = PARTITION(A, p, r) -- chose pivot randomly
    k = q - p + 1 -- pivot's index in A[p,...,r]
    if i == k:
        return A[q]
    elif i < k:
        return RAND_SELECT(A, p, q-1, i)
    else:
        return RAND_SELECT(A, q+1, r, i-k)
```

### Example

Find the $6^{th}$ smallest number in $A=[3,8,1,7,4,6,2,5,9]$

1. Pick pivot randomly, e.g. $4$
2. Partition on pivot $4$: $[3,1,2]++[4]++[9,6,8,5,7]$ returns $i + 1 = 4$
3. $6 > i + 1$; $i + 1$ smallest numbers are $[3,1,2,4]$ in some order

$6^{th}$ smallest number is $(6-(i + 1))^th$ smallest number in $A[i+2,...,r]$

$=$`RAND_SELECT(A, 5, 9, 2)`

### Analysis

#### Running Time

##### Worst case:

Might partition the array with one element on on side and all the rest on the other side:

$T(n) = T(n-1) + f(n); f(n) \in \Theta(n)$

$$\therefore T(n) \in \Theta(n^2)$$

##### Best case:

Might partition the array with the same number of elements above and below the pivot each time:

$T(n) = T(\lfloor \frac{n}{2} \rfloor) + f(n); f(n) \in \Theta(n)$

$\qquad= aT([\frac{n}{b}]) + f(n)$ with $a=1, b=2, f(n) \in \Theta(n)$

Case $3$ of Master Theorem $\Rightarrow T(n) \in \Theta(n)$

---

## BFPRT

Choosing a pivot randomly might get you a bad pivot - there's a way to pick a good one every time.

### Algorithm

`SELECT(A: [], p: int, q: int, i: int) -> int:`
1. **divide** the $n=q-p + 1$ elements into groups of $5$
   * find the *median* of each group
2. recursively `SELECT(x)`, the median of the $\lceil \frac{n}{5} \rceil$ group medians, to be the pivot
3. **partition** $A[p,...,q]$ using pivot $x$
   * set $k=$ index of $x$
4. case:
   1. $i=k:$ return $x$
   2. $i<k:$ recursively `SELECT` $i^{th}$ smallest element in **lower** part
   3. $i>k:$ recursively `SELECT` $(i-k)^{th}$ smallest element in **upper** part

### Example

$A = [2,3,1,7,4,12,14,19,6,5,17,13,11,8,9]$

Split into groups of *five* and find the median of each:
1. $[2,3,1,7,4]:$ median 3
2. $[12,14,19,6,5]:$ median 12
3. $[17,13,11,8,9]:$ median 11

Median-of-medians is $11$ - partition $A$ with $11$ as pivot:
* $[2,3,1,7,4,6,5,9,8]++[11]++[17,13,19,12,14]$

If $i =\not$ index of pivot, recursively `SELECT` on:
* $[2,3,1,7,4,6,5,9,8]++[11]++[17,13,19,12,14]$

Some elements **must** end up on LHS of pivot, e.g. 3 lowest elements in groups of 5 with group median < pivot

### Analysis

#### Non-Recursive:

* $\Theta(n)$ time to break into groups
* $\Theta(1)$ time to sort **one** group of $5$ elements
* $\to \Theta(n)$ time to find medians of all groups
* $T(\lceil \frac{n}{5} \rceil)$ time to find median of the group medians
* $\Theta(n)$ time to partition $n$ elements around the pivot

Total so far:

$T(\lceil \frac{n}{5}\rceil) + f(n)$ time for some $f(n) \in \Theta(n)$

$\therefore \leq T(\lceil \frac{n}{5} \rceil) + \alpha n$ for some $\alpha > 0$

#### Recursive:

Time to recursively call `SELECT` on one 'half' of the input:

* have $\lceil \frac{n}{5} \rceil$ group medians; at least half of which are $\leq x$
* just one is $=x$
* and at most one is for a group of size $< 5$
* so at least $3(\lceil \frac{n}{5} \rceil/2 -2)$ elements are known to be $\leq x$
* upper 'half' of input has therefore at most $n -3()$
* I got bored at this point

---

## Summary

* `RAND_SELECT` is linear-time on average and simpler to implement
* `SELECT` is worst-case linear-time and slightly harder to implement