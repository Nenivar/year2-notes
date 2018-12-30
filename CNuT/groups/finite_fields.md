# Finite Fields

For every prime $p$ and every positive integer $n$, there is exactly one finite field with $p^n$ elements up to isomorphism.
> These are the only finite fields.

## Irreducible Polynomials (and Where to Find Them)

A polynomial $p$ over a field is irreducible if it is:

* **not a unit**
* cannot be decomposed into a product of non-units
  * if $p = ab$ then either $a$ or $b$ is a unit

### Finding

* degree $0$: units; therefore **not irreducible**
* degree $1$: all are **irreducible**
* degree $2$: harder

Use a table:

|$u$|$v$|$b=u + v$|$c = u + v$
|-|-|-|-|
|0|0|0|0|
|0|1|1|0|

* degree $\geq$ 3: ignore

## Roots of Unity

> The multiplicative group of a finite field is cyclic

> In a finite field $GF(p^n)$, for any field element $a$ we have $a^{(p^n-1)}=1$
> 
> This implies that $a^{(p^n-2)}=\frac{1}{a}$

> A field element $x$ is called a $k$-th root of unity if $x^k=1$ in the field, for a positive integer $k$.
> 
> If $x^k=1$ and $x^m=\not1$ $\forall 1 \leq m < k$, we say that $x$ is a primitive $k$-th root of unity

In finite fields, **all nonzero elements** are roots of unity.

## Frobenius Map

> In a finite field of characteristic $p$, $\phi(a)=a^p$ is called the **Frobenius automorphism**
> 
> $\phi(0)=0$, $\phi(1)=1$, $\phi(a \times b) = \phi(a) \times \phi(b)$ and $\phi(a + b) = \phi(a) + \phi(b)$ for all $a, b$