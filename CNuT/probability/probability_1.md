# Probability

## Fundamentals

> #### Probability Space
> ($\Omega$, $p: \Omega \to [0,1]$) where:
> * $\Omega$: **sample space**, finite set
> * $p$: **distribution function**, satisfying $\sum_{\omega\in\Omega}p(\omega)=1$
> > $p(\omega)$ is read as 'the probability that element $\omega$ gets picked'

> #### Event
> A subset $E \subseteq \Omega$ of a probability space $(\Omega, p)$ is called an **event**
> 
> The probability of an event $E$ is $P(E) := \sum_{e\in E}p(e)$
> 
> > * $P(\emptyset)=0$ and $P(\Omega) = 1$
> > * $P(E \cup F) \leq P(E) + P(F)$
> >   *  $P(E \cup F) = P(E) + P(F) - P(E \cap F)$
> > * $P(E \cap F) \leq$ `min` $(P(E), P(F))$ 
> > * if $E \subseteq F$ then $P(E) \leq P(F)$
> > * $P(\frac{\Omega}{E}) = 1 - P(E)$

If $p$ assigns the same probability to every element of a finite sample space $\Omega$ then it is **uniform**.

---

## Odds

Odds go from $0 \to +\infty$, wheras probabilities go from $0 \to 1$.

Probabilities add; odds **multiply**.

Converting:
$$r = \frac{p}{1-p}\qquad p = \frac{r}{1+r}$$

---

## Conditionals

> #### Conditional probability of $E$ given $F$:
> $$P(E|F) := \frac{P(E\cap F)}{P(F)}$$
>  (given $P(F) > 0$)

> #### Independence
> $E, F$ are independent if:
> $$P(E\cap F) = P(E) \times P(F)$$
> > $\equiv P(E|F) = P(E)$ given $P(F)=\not0$

> #### Total Probability
> A partition of a probability space $(\Omega, p)$ is a family of sets $S_i$ s.t.:
> * every element of $\Omega$ is in exactly one $S_i$
> * $P(S_i) > 0, \forall i$
> For every parition and event $E$:
> $$P(E) = \sum_i P(E \cap S_i) = \sum_i P(S_i) \times P(E | S_i)$$
> > ##### On-Off Lemma
> > This is useful for a partition of two elements, $F$ and $¬F$:
> > 
> > $E, F$ s.t. $0 < P(F) < 1$
> > $$P(E) = P(E|F) \times P(F) + P(E|¬F) \times P(¬F)$$

---

## Bayes' Theorem

> $E,F$ where $P(E) =\not 0$ and $P(F) =\not 0$:
> $$P(E|F) = \frac{P(F|E) \times P(E)}{P(F)}$$