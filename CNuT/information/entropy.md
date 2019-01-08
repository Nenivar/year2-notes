# Entropy

## Information and Entropy

> #### Information In an Event
> The info. conveyed when an event *E* occurs is:
> $$log_2{\frac{1}{P(E)}}$$

The idea is that a **lower**-probability event conveys **more** information than a higher-probability one.

* an event with probability $1$ conveys $0$ information
* an event with probability $2^{-n}$ conveys $n$ bits of information

> #### Entropy
> The entropy $H(X)$ of a random variable $X$ with range $X$ is the quantity:
> $$H(X)=\sum_{x\in X} p_x(x) \log_2 \dfrac{1}{p_x(x)} = -\sum_{x\in X} p_x(x) \log_2 (p_x(x))$$

### Example

Pick an integer between $0$ and $255$ inclusive uniformly at random - there are $2^8$ possible cases, each of which occurs with probability $2^{-8}$. So:

$$H(X)=\dfrac{2^8}{2^8\log_2 (\frac{1}{2^{-8}})}=8$$

$\therefore$ you can represent such a number with $8$ bits.

### Properties

1. The entropy of a random variable $X$ is always $\geq 0$
2. For a random variable $X$ with finite range $X$, the entropy is bounded by:
   $$H(X) \leq log_2\vert X\vert$$
   This bound is tight iff $X$ has the uniform distribution
3. For two independent random variables $X,Y$, if $Z=(X,Y)$ is the random variable that gives you both the values of $X$ and $Y$, then we have the sum formula:
   $$H(Z)=H(X)+H(Y)$$

> #### Binary Entropy Function
> For a random variable $X$ with two possible outcomes $\{0,1\}$ where the outcome $0$ has probability $p$, the entropy is:
> $$H(X)= -p\log_2(p) - (1-p)\log_2(1-p)$$
> (a.k.a $h_2(p)$)

---

## The Meaning of the Logarithm

> #### Two Stage Process
> For any two stage process where we first sample according to a distribution $S$ with range $\{1,\dots,n\}$ that returns an integer $i$ with probability $p_i$, then sample from a distribution $A_i$ and return that value, if the ranges of $A_i$ are disjoint then for the random variable $X$ representing the whole process we have:
> $$H(X)=\sum_{i=1}^n p_i \times H(A_i)$$

---

## Conditional Entropy & Mutual Information

> #### Conditional Entropy
> The conditional entropy of a random variable $X$ with range $X$ conditioned on the event $Y=y$ is:
> $$H(X\vert Y = y) = -\sum_{x\in X}p_{X\vert Y}(x,y) \cdot log_2(p_{x\vert Y}(x,y))$$
> The conditional entropy of a random variable $X$ with range $X$ conditioned on the random variable $Y$ with range $Y$ is:
> $$H(X\vert Y) = \sum_{y\in Y} p_y(y) \cdot H(X\vert Y=y)$$
> > $$H(X,Y) = H(X) + H(Y\vert X) = H(Y) + H(X\vert Y)$$

You should interpret $H(X\vert Y)$ as the amount of entropy in $X$ that is independent of $Y$.

For example, if $X$ represents the lower $3$ bits of a number and $Y$ is the lowest bit on its own, then $H(X) = 3$ and $H(X\vert Y) = 2$ since $2$ of the bits have nothing to do with $Y$.

> #### Mutual Information
> The mutual info. between two random variables $X,Y$ with ranges $X$ and $Y$ resp. is:
> $$I(X,Y) = \sum_{x\in X}\sum_{y\in Y} p_{XY}(x,y) \cdot log_2\dfrac{p_{XY}(x,y)}{p_x(x) \times p_y(y)}$$
> or:
> $$I(X,Y) = H(X) - H(X\vert Y) = H(Y) - H(Y\vert X)$$
> All the information in $X$ minus the information in $X$ that is independent of $Y$.