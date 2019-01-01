# Recurrences

## Solving Recurrences

1. Guess form of answer
2. Use induction to check & find values of variables

---

## Subsitution Method



---

## Algorithmic Strategies

### Iteration

1. Process inputs $1,...,n-1$
2. Combine output with input $n$

*e.g. Insertion Sort*

Typical reccurence for worst-case time:
$$T(n) = aT(n-1) + f(n)$$

### Divide-And-Conquer

1. Divide inputs $1,...,n-1$ into a fixed number of groups and inputs
2. Process each group of inputs
3. Combine together the results

*e.g. Merge Sort*

Typical reccurence for worst-case time:
$$T(n) = aT(n/a) + f(n)$$

---

## Master Theorem

---

## Akra-Bazzi Formula

Single-case formula for asymptotic behaviour for T(n), under **very broad conditions** on T(n):

$$T(n)=\sum_{1\leq i \leq k} a_i T ([d_i n]) + f(n)$$

> $\sum_{1 \leq i \leq k} a_i \geq 1, 0 < a_i, 0<d_i<1$ for $1\leq i \leq k, \sum_{1\leq i\leq k} a_i(d_{i^p})=1$

$\rightarrow$

$$T(x) \in \Theta(x^p(1 + \int^x_{u=1} f(u) u^{-p-1} du))$$