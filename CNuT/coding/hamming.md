# Hamming Distance

## Terminology

* **code**: $c$ is a subset of the channel space $X$
* **codeword**: $c \in C$
* **block code**: code where all codewords have the **same length**
  * over $\Sigma$, an $(n, \Mu)$-code is a blockcode $C$ that contains $M$ codewords, each of which is $n$ symbols long:
    * **information length**: $\log(M)$
    * **redundancy**: $n - \log(M)$
    * **information rate**: $\frac{\log(M)}{n}$

---

## Hamming Distance

> #### Hamming Weight
> $w(x)$ of a word $x \in (\mathbb{F}_q)^k$ is the number of nonzero symbols $x_i =\not 0$ in $x$
> #### Hamming Distance
> $d(x,y)$ between two words $x, y \in (\mathbb{F}_q)^k$ is $w(x-y)$; the subtraction is done symbol-wise
> > * for any $x$, $d(x,x) = 0$; for any $x,y$, $d(x,y) \geq 0$
> > * for any $x,y$, $d(x,y) = d(y,x)$
> > * **triangular inequality:** for any $x,y,z$:
> > $$d(x,y) + d(y,z) \geq d(x,z)$$

If you send a codeword $c$ and there are $u$ errors in transmission, the received word $r$ will have $d(c, r) = u$.

---

## Minimum Distance

> #### Minimum distance of a block code $C \subseteq \Sigma^n$:
> $$d(C) := min_{c,c' \in C, c=\not c'} d(c,c')$$

E.g. in a code with min. dist. $3$, the Hamming distance between any two codewords is at least $3$.

If you received a word $r$ out of a channel that is not a codeword but has Hamming distance $1$ to some channel, then it has Hamming distance $2$ to the other channels - you can assume that a single error has occured, and you can decode $r$ as $c$.

> For a code to **correct** up to $t$ errors, it need a minimum distance of at least:
> $$d \geq 2t + 1$$
> To **detect** $t$ errors, it is enough to have:
> $$d \geq t + 1$$

If you send a codeword $c$, then all errors that can occur due to at most $t$ errors are in the set:
$$B_t(c) = \{w | d(c,w) \leq t\}$$
aka, **ball of radius $t$ with centre $c$**

---

## Singleton Bound

How many symbols do we need to add to get a code with minimal distance $d$?

> #### Singleton Bound:
> A code $C \subseteq \Sigma^n$ of minimal distance $d$ has at most $|\Sigma|^{n-d+1}$ codewords
> 
> or: if $E: \Sigma^k \to \Sigma^n$ then $d \leq n - k + 1$

---

## Optimal Codes

> For $q$ a prime power, $A_q(n,d)$ is the maximal number of words in any code of length $n$ over an alphabet of size $q$ with minimal distance $d$
> 
> Any code meeting this bound is an **optimal code**

---