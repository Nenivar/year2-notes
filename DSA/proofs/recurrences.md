# Recurrences

## Subsitution Method

1. Guess form of answer
2. Use induction to check & find values of variables

## General Method

$$T(n) = c_1T(n-1) + c_2T(n-2) + P(n)$$
> where $P(n)$ is an order-$k$ polynomial in $n$, $\sum_{0\leq i\leq k} p_i n^i, p_k > 0$
Case:
* $c_2 = 0:\qquad$ try $d_1c_1^n + \sum_{0\leq i\leq k} e_i n^i$
  * if this doesn't work, try adding $e_{k+1}n^{k+1}$
* $c_2 > 0:\qquad$ find $r_1,r_2$, the solutions to $x^2 = c_1x + c$
  * $r_1 =\not r_2,\qquad$ try $d_1(r_1)^n + d_2(r_2)^n + \sum_{0\leq i\leq k}e_i n^i$
  * $r_1 = r_2,\qquad$ try $d_1(r_1)^n + d_2(r_1)^n n + \sum_{0\leq i\leq k}e_i n^i$

## Example 1

$$T(n) = 2T(n-1) + n-1$$

* $T(1) = 0, T(2) = 1, T(3) = 4, T(4) = 11\dots$

* $c_1=2, c_2=0, P(n)=n-1$

$\rightarrow$ guess $T(n)=d_12^n + e_0 + e_1n$

#### Induction

1. **Inductive Hypothesis:** $T(m) = d_12^m + e_1m + e_0$
2. **Base Case:** $n=0, d_12^0 + e_10 + e_0$ provided $d_1=-e_0$
3. **Inductive Step:**

$\qquad\qquad T(n) = 2T(n-1) + (n-1)$

$\qquad\qquad = 2(d_12^{n-1} + e_1(n-1) + e_0) + n-1$ by inductive hypothesis

$\qquad\qquad = d_12^n + 2e_1n - 2e_1 + 2e_0 + n - 1$

$\qquad\qquad = d_12^n + e_1n + e_0 + (e_0 - 2e_1 -1) + (e_1+1)n$

$\qquad\qquad = d_12^n + e_1n + e_0$ provided $e_0 = -1, e_1 = -1$

$\qquad\qquad \rightarrow solution: T(n) = 2^n + n - 1$

$\therefore T(n) \in \Theta(2^n)$

### Example 2

$$T(n) = 2T(\frac{n}{2}) + cn$$
> where n is a power of 2

$T(n) = 2T(2T(\frac{n}{4}) + \frac{cn}{2}) + cn = 4T(\frac{n}{4}) + 2cn$

$T(n) = 4T(2T(\frac{n}{8}) + \frac{cn}{4}) + cn = 8T(\frac{n}{8}) + 3cn$

$...= 2^k T(\frac{n}{2^k}) + kcn$ as a guess

$= nT(1) + cn \log n$ when $k = \log n$

$\Rightarrow$ guess $T(n) = an + bn \log n$

> Check with **strong induction**:
> 1. **Inductive Hypothesis:** $T(m) = am + bm \log m, \forall$ integers $m<n$
> 2. **Base Case:** $n=1, a = T(1)$
> 3. **Inductive Step:**
> 
> $\qquad \quad T(n) = 2T(\frac{n}{2}) + cn$
> 
> $\qquad \quad =2(\frac{an}{2} + \frac{bn}{2} \log {n}{2}) + cn$ by inductive hypothesis
> 
> $\qquad \quad =an + bn \log n - bn + cn$
> 
> $\qquad \quad = an + bn \log n$ for $b=c$

We've shown that $T(n) = T(1) n + cn \log n < (T(1) + c) n \log n,$ for $n>1$

$\therefore T(n) \in O(n \log n)$

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

$$T(n) = aT([\frac{n}{b}]) + f(n)$$

where $a \geq 1, b > 1, f(n) > 0$ for **large** $n$

Case, where $p = log_b(a)$:
1. $f(n) \in O(n^c), c < p\quad\Rightarrow T(n) \in \Theta(n^p)$
2. $f(n) \in \Theta(n^c), c = p\quad\Rightarrow T(n) \in \Theta(n^p \log n)$
3. $f(n) \in \Omega(n^c), c > p\quad\Rightarrow T(n) \in \Theta(f(n))$

> Works for *Divide-&-Conquer* recursions   

---

## Akra-Bazzi Formula

Single-case formula for asymptotic behaviour for T(n), under **very broad conditions** on T(n):

$$T(n)=\sum_{1\leq i \leq k} a_i T ([d_i n]) + f(n)$$

> where $f(n) = \alpha n^c$,
> 
> $\sum_{1 \leq i \leq k} a_i \geq 1, 0 < a_i, 0<d_i<1$ for $1\leq i \leq k, k$ integer $> 0, \alpha > 0, c \geq 0$

$$\Rightarrow\quad T(x) \in \Theta(x^p(1 + \int^x_{u=1} f(u) u^{-p-1} du))$$

Case, where $p=$ solution to $\sum_{1\leq i\leq k} a_i(d_{i^p})=1$:

1. $c < p\quad\Rightarrow T(n) \in \Theta(n^p)$
2. $c = p\quad\Rightarrow T(n) \in \Theta(n^p \log n)$
3. $c > p\quad\Rightarrow T(n) \in \Theta(n^c)$

### Iteration vs Divide-&-Conquer

Iteration:
* $T(n) = aT(n-1) + n, a > 1$
* $T(n) \in \Theta(a^n)$

Divide-&-Conquer:
* $T(n) = aT([\frac{n}{a}]) + bn, a > 1, b > 1$
* $T(n) \in \Theta(n \log n)$

> Divide-&-Conquer algorithms tend to have **better** worst-case asymptotic behaviour than iterative algorithms

### Example 1

$T(n) = T(\lceil \frac{3}{4}n \rceil) + T(\lfloor \frac{n}{4} \rfloor) + n$

$\rightarrow k = 2, a_1=a_2=1, d_1 = \frac{3}{4}, d_2=\frac{1}{4}, \alpha=1, c=1$

> check conditions OK

$p=$ solution to $\sum_{1\leq i\leq k} a_i (d_i^p) = 1$
$(\frac{3}{4})^p + (\frac{1}{4})^p = 1$

$\therefore p=1$

$\Rightarrow$ case 2;
$$T(n) \in \Theta(n^p \log n) = \Theta(n \log n)$$

### Example 2

$T(n) = 3T(\lceil \frac{n}{4}n \rceil) + T(\lfloor \frac{n}{2} \rfloor) + 7n^2\sqrt{n}$

$\rightarrow k=2, a_1=3, a_2=1, d_1=4, d_2=\frac{1}{2}, \alpha=7, c=\frac{5}{2}$

> check conditions OK

$p=$ solution to $\sum_{1\leq i\leq k} a_i (d_i^p) = 1$

$3(\frac{1}{4})^p + (\frac{1}{2})^p = 1$

$p < 2,$ since $3(\frac{1}{4})^2 + (\frac{1}{2})^2 = \frac{7}{16} < 1,$ so $p < \frac{5}{2}$

$\Rightarrow$ case 3:
$$T(n) \in \Theta(n^{\frac{5}{2}})$$