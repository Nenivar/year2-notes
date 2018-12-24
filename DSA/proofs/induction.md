# Induction

1. **Base case:** $P(0)$
2. **Inductive Step:** $P(n) \rightarrow P(n + 1)$
3. $\therefore p(n)$, $\forall n > 0$

## Example

> $\sum^n_{k=1} k = \dfrac{n(n+1)}{2}$

1. $P(0) = \dfrac{0(0 + 1)}{2} = 0$
2. $P(k) = \dfrac{k(k+1)}{2}$
   
   $P(k + 1) = \dfrac{k(k+1)}{2} + (k+1)$

   $\qquad\qquad= \dfrac{(k+1)(k+2)}{2}$

   say $k+1 = m$

   then $\qquad= \dfrac{m(m+1)}{2}$

   $\therefore p(n)$, $\forall n > 0$

# Strong Induction

1. **Base case:** $P(0)$
2. **Strong inductive hypothesis**
3. **Inductive step:** $P(0), ..., P(n)$ together $\rightarrow P(n + 1)$
4. $\therefore p(n)$, $\forall n > 0$

## Example

$F_0 = 0, F_1 = 1, ...$

$F_n = F_{n-1} + F_{n-2}$, $\forall n \geq 2$

> $F_n$ + $F_{n + 3}$ is even

1. $F_0 + F_3 = 0 + 2 = 2$
2. $F_m + F_{m + 3}$ is even for $m=0,1,...,n-1$
3.
   * *case $n>1$*:
     
     $F_n = F_{n + 3} = F_{n-1} + F_{n-2} + F_{n + 2} + F_{n + 1}$
     
     $= (F_{n-1} + F_{n + 2}) + (F_{n-2} + F_{N + 1})$
     
     which are both even (by hypothesis)
   * *case $n=1$*:
     
     $F_1 + F_4 = 1 + 3 = 4$
     which is even
1. $\therefore n$ is even, $\forall n > 0$