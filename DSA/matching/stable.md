# Stable Matching

## Situation

$S_1 ... S_n$ students applying for summer internships, with $E_1 ... E_n$ employers.

1. students list employers in order of preference
1. employers list students in order of preference
1. employers give offers to students
1. students accept or decline (and can accept first & decline later)

> Unstable matching:
> 
> * there is a pair (S, E) not matched to each other s.t
>   * S prefers E to the employer they're matched to
>   * E prefers S to the student they're matched to

## Algorithm of Happiness

(aka Gale-Shapley)

1. let $i$ be the smallest value so that $E_i$ is unmatched
2. $E_i$ makes an offer to the **most desirable student** that has not already rejected an offer from $E_i$
3. the student accepts if:
   * it's the **first offer** they've received
   * *OR* they **prefer** $E_i$ to the employer they're currently matched to
4. If there are no unmatched employers, **stop**; else **repeat**

## Correctness

The algorithm terminates after at most $n^2$ offers:

* employers make offers in decreasing order ofpreference
* so each offer is for a **different pair** (S, E)
* there are $n^2$ different pairs (S, E)

All students and employers are matched when the algorithm terminates:

* suppose not everyone is matched - there must be at least one unmatched student $s_u$ and one unmatched employer $e_u$
* $e_u$ must have made an offer to all the students, including $s_u$
* $s_u$ received at least one offer - after accepting her first offer she will have remained matched for the rest of the running of the algorithm.
* so $s_u$ is in fact matched - **contradiction**

The matching found by the algorithm is stable:

* employers make offers in descending order of preference
* students **only trade up**
* suppose the matching is unstable - i.e. $s_1$ is matched to $e_1$ but prefers $e_2$; $e_2$ is matched to $s_2$ but prefers $s_1$
* $e_2$ must have made an offer to $s_1$ before making an offer to $s_2$ - $s_1$ rejected the offer, so must prefer $e_1$ to $e_2$ - **contradiction**

## Implementation tip

Inverse each student's list of employers ordered by preference

$\rightarrow$ you can answer quickly when the number of employers is large;

> 'Does $S_k$ prefer employer $i$ to employer $j$?

Check whether `inverse-pref[k, i] < inverse_pref[k, j]`

## Perfection

Stable matchings are **not unique**.

> **Lemma**:
> 
> If $S$ rejects an offer from $E$, then $(S, E)$ is not feasible

> **Theorem**:
> 
> The algorithm pairs each employer $E$ with `best(E)`, $E$'s favourite student $S$ for which $(S, E)$ is feasible
> > **Corollary**:
> > 
> > The same matching is reached regardless of the ordering of the employers
> 
> Consequently, the algorithm assigns each student $S$ to `worst(S)`, $S$'s least favourite employer $E$ of those for which there is a stable matching containing $(S, E)$