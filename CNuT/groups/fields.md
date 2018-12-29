# Fields

$\mathbb{F} = (F, +, \times)$ is a field if it is a:
* commutative ring
* $0_R =\not 1_R$ 
* every element except $0_R$ is a unit

## Characteristics

> ### Ring
> 
> If adding $1_R$ to itself never produces $0$, then the ring has characteristic $0$
> 
> Otherwise, if $n$ is the smallest number s.t. adding $1_R$ to itself $n$ times gives $0$, the ring has characteristic $n$

The characteristic of a field has to be a **prime** or $0$.

But this does not mean that a field needs a prime number of elements to have a prime characteristic.

## Euclid's Algorithm

If $m, n$ are two nonzero integers, then there are unique integers $a,b$ s.t.:

$$a \times n + b \times m = gcd(m, n)$$

> |q|r|a|b|
> |-|-|-|-|
> |$0$|$256$|$1$|$0$|
> |...|...|...|...|
> 
> Let $q', r'..$ be values from the last row and $q'', r''...$ be values from the **second**-to last row:
> 
> * Divide $r''$ by $r'$ with remainder - set the quotient & remainder as the new $q$ & $r$ values
> * Set $a = a'' - q \times a'$ and $b = b'' - q \times b'$
> * Repeat until the remainder becomes $r=0$