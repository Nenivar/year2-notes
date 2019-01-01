# Algebra II

## Inner Product

$$\langle \bar{v} | \bar{w} \rangle =
\sum_{i=1}^n v_i \times w_i$$

### Properties:

* symmetry: $\langle \bar{v} | \bar{w} \rangle = \langle \bar{w} | \bar{v} \rangle$
* linearity: $\langle \bar{v} + \bar{z} | \bar{w} \rangle=
\langle \bar{v} | \bar{w} \rangle + \langle \bar{z} | \bar{w} \rangle$ and
$\langle a \times \bar{v} | \bar{w} \rangle = a \times \langle \bar{v} | \bar{w} \rangle$

> #### Orthogonal:
> $\langle \bar{v} | \bar{w} \rangle = 0$

---

## Orth-Bases

A basis is an **orthogonal basis** if for all $i, j \leq n$ with $i =\not j$, $\langle \bar{b}_i | \bar{b}_j \rangle = 0$

A basis is an **orthonormal basis** if the above applies and for all $i \leq n$, $\langle \bar{b}_i | \bar{b}_i \rangle = 1$

> The number of elements in a vector space must be of the form $q^n$, where $q = |\mathbb{F}|$

---

## Polynomials as Vectors

A polynomial of degree $d$ is given by $d+1$ coefficients/$(x,y)$ points through which the polynomial passes

### Vandermonde Matrix

$$M=
\begin{pmatrix}
1&1&...&1 \\
x_1&x_2&...&x_m \\
(x_1)^2&(x_2)^2&...&(x_m) ^2 \\
...&...&...&... \\
(x_1)^n&(x_2)^n&...&(x_m)^n
\end{pmatrix}$$

Computing $\bar{c} \times M$ gives us the vector $p(x_1),...,p(x_m))$ where $p(x_i)$ us the polynomial evaluated at the point $x_i$

> A square Vandermonde matrix with all points distinct is an **invertible** matrix

---

## Interpolation

$p(0)=2,p(1)=4,p(3)=3$

means:
$\bar{c} \times M = (2,4,3)$
where M is the Vandermonde matrix

To get back the coefficients, compute $\bar{c} = (2,4,3) \times M^{-1}$

### Lagrange Interpolation

This finds the unique polynomial of degree-bound $n$ that passes through $n+1$ given points.

> Polynomial $p(x)$ of degree-bound  $n$ for a set of points $(x_i, y_i)^n_{i=0}$:
> $$p(x) = \sum^n_{i=0} y_i \times L_{i,n}(x)$$
> where
> $$L_{i,n} = \prod_{k=\not i} \dfrac{x-x_k}{x_i-x_k}$$
> * the product over $k$ goes from $0$ to $n$ leaving out the value $i$; there are $n$ terms in the product
> * $x_i$ and $x_k$ are just constants

A polynomial of degree $n \geq 0$ that is not the all-zero polynomial, has at most $n$ zeros over any field

> For any of distinct points $\{x_0,x_1,...,x_n\}$ their Lagrange polynomials $L_{i,n}$ are a basis of the space of polynomials of degree-bound $n$
> > $L_{i,n}(x_i) = 1$
> >
> > $L_{i,n}(x) = 0$ for $x \in {x_0,...,x_n}$ and $x =\not x_i$

#### Example

Over $\mathbb{F}_5$ with $p(0)=2, p(1)=4, p(3)=3$:
* it has a degree-bound of $2$
* it passes through $(0,2),(1,4),(3,3)$

$$L_{0,2}(x) = \dfrac{(x-1)(x-3)}{(0-1)(0-3)} = 2(x-1)(x-3) = 4+2x+2x^2$$

The others are: $L_{1,2}(x) = 0 + 4x + 2x^2$ and $L_{2,2}(x) = 0 + 4x + x^2$

This makes:

$$p(x) = 2 \times L_{0,2}(x) + 4 \times L_{1,2}(x) + 3 \times L_{2,2}(x) = 2 + 2x$$