# Linear Algebra I

> ## Linear Independence
> A set $\{\bar{v}_i\}_i$of vectors is linearly independent if no linear combination of the vectors $\sum_i c_i \times \bar{v}_i$ with coefficients in $\mathbb{F}$ gives the zero vector $\bar{0}$, unless all coefficients are already $0$

> ## Basis
> A basis of a vector space $V$ is a finite list $(\bar{v}_1, ..., \bar{v}_n)$ of vectors that is linearly independent and generates $V$ as a group under addition
> > Any two bases of a vector space have the same number of elements - $n$ elements means dimension $n$

> ## Change of Basis
> Given a vector $\bar{a}$ in the usual basis $\bar{e}_1,...,\bar{e}_n$, to compute the coefficients of $\bar{a}$ in a basis $\bar{b}_1,...,\bar{b}_n$ set up and solve a system of equations:
> $$\sum_{i=1}^n c_i \times \bar{b}_i = \bar{a}$$
> where $c_i$ are the free variables

> ## Linear Map
> If $V$ and $W$ are two vector spaces over a field $\mathbb{F}$, we call a function $f: V \rightarrow W$ linear if for any $\bar{x}, \bar{y}$ in $V$ and any $a \in \mathbb{F}$ we have:
> * $f(\bar{v} + \bar{w}=f(\bar{v}) + f(\bar{w}))$
> * $f(a \times \bar{v})=a \times f(\bar{v}))$

**Rank:** maximal number of linearly independent row/columns a matrix has
* a matrix of size $n\times n$ is invertible iff its rank is $n$

## Converting from Basis

1. $B \times \bar{c} = \bar{a}$
2. $\bar{c}=B^{(-1)} \times \bar{a}$