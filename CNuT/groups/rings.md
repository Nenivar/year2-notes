# Rings

$R = (R,+,\times)$ where $R$ is a set, and $+$, $\times$ are two operations $R \times R \rightarrow R$ if the following hold:

* **additive group**: $(R, +)$ is an Abelian group with neutral element $0_R$
* **multiplication**: $(R, \times)$ is an associative group with neutral element $1_R$
* **distributive law**: for any elements $a,b,c$ in $R$ we have $c \times (a + b) = c \times a + c \times b$ and vice versa

If the multiplication of the ring is commutative the ring is also commutative.

> * there can only be one neutral element for multiplication for any ring
> * there is a ring with one element, where $0_R$ = $1_R$ - but as soon as you hit two elements $0_R =\not 1_R$
> * multiplying any element from the ring by $0_R$ gives $0$

# Units

* **zero**: neutral element of the ring ($0_R$)
* **unit**: element $a$ in the ring which has an inverse $b$ s.t. $a \times b = 1$
  * $1_R$ is always a unit
* **zero divisor**: element $a =\not 0$ for which $b =\not 0$ and $a \times b = 0$
* **neither**

> $\mathbb{Z}_n^x$ is the subset of $\mathbb{Z}_n$ containing all elements $a$ for which $a \times_n b =\not 0$ for all other elements $b =\not 0 \in \mathbb{Z}_n$
> > basically: remove $0$ and all zero divisors

# Euler's Totient Function

$\phi(n)$ maps positive integer $n$ to the number of elements in $\mathbb{Z}_n^x$

Two elements $m, n$ are coprime if their `gcd` is $1$; $\phi(m \times n) = \phi(m) \times \phi(n)$

> For a prime $p$ and a positive integer $k$ we have $\phi(p^x) = p^{k-1}(p - 1)$

> $\therefore \phi(p) = p-1$ if $p$ is prime

To find $\phi(n)$, factor n as distinct primes$^{powers}$ and **multiply** the $\phi$s.

# Exponent Arithmetic

You cannot do $(a^n)^m$ in a commutative ring through normal means - exponents are integers and not ring elements.

$[a^k]_n = [([a]_n)^{[k]_{\phi(n)}}]_n$

> * reduce group elements/bases modulo n
> * and exponents modulo $\phi(n)$

For example,

$310 (mod 5)$

$= 3^{10(mod \phi(5))}$

$= 4$