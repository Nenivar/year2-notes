# P & NP

* **Decision Problems** - problems with a yes/no answer
* $P$ - set of decision problem families with running time **polynomial** in input size

---

## Reduction

Determine which families of problems are in $P$ - we can determine this for some families using **reductions**.

> A reduction **maps** family $A$ to family $B$ in polynomial time s.t:
> * the answer for an instance of $A$ is 'yes' $\Leftrightarrow$ answer for its image in $B$ is 'yes'

> If we have an algorithm with runtime **polynomial**  in input size that, given any instance of decision problem family $A$, transforms it into an instance of decision problem family $B$ s.t:
> * answer for the instance of $A$ is yes $\Leftrightarrow$ answer for instance of $B$ is yes
> 
> Then say: **there is a polynomial-time reduction of $A$ to $B$**
> *(or: $A$ **reduces** to $B$)*
> * (or: $A \leq_p B$)

If $A\leq_p B$, and we can solve $B$, we can use this to solve $A$.

### Properties

* If $A$ is in $P$ and $B\leq_p A$, then $B$ is in $P$.
* For any decision problem family $A$, there is a polynomial-time reduction of $A$ to $A$; $A\leq_p A$
* If $A\leq_p B$ and $B\leq_p C$ then $A\leq_p C$

### Example

* `INDEPENDENT_SET`: is there a set of $k$ vertices in $G$ s.t. no two vertices in the set are linked by an edge?
* `CLIQUE`: is there a set of $k$ vertices in $G$ s.t. every pair of vertices in the set is linked by an edge?

> `INDEPENDENT_SET[G,k]` has the answer 'yes' **iff** `CLIQUE[G',k]` has the answer 'yes'.
> 
> Where $G'=(V,E')$ is the complement of $G=(V,E)$
> i.e. $(v_1,v_2)\in E'$ iff $(v_1,v_2)\notin E$

We can map $G \mapsto G'$ in polynomial time.

$$\therefore INDEPENDENT\_SET \leq_p CLIQUE$$

---

## Verifying Solutions

$NP$ is the class of problems for which, if the answer to an instance is 'yes', we can **verify** this efficiently.

> $NP$ stands for '**Non-deterministic** polynomial'

Not every decision problem family is in $NP$.

> For example: *given a position in an $n\times n$ chess, can White force a win?*
> 
> $A$ is in $P$ implies $A$ is in $NP$
> * We can efficiently verify a claim that an instance of $A$ has answer 'yes', by solving $A$ ourselves
> 
> $$\therefore P\subseteq NP$$

> #### $NP$-hard
> For **every** $B$ in $NP$, $B\leq_p A$
> 
> *($A$ is at least as hard as the hardest problems in $NP$)*
> 
> * If there's a polynomial-time algorithm for a problem family in $NP$-hard, then $P=NP$
> * So if we can prove a problem family is in $NP$-hard, this is evidence there's **no polynomial-time** algorithm to solve it
> 
> A is in $NP$-hard doesn't necessarily imply $A$ is in $NP$.
> > e.g. the $n\times n$ chess problem family mentioned earlier is in $NP$-hard but not in $NP$

> #### $NP-complete$
> $A$ is in $NP$-hard and $A$ is in $NP$


If you can find a polynomial-time algorithm to solve just **one** of these families:
$$P=NP$$
If you can prove that for just **one** NP-complete decision problem family, there's **no** efficient algorithm to solve it:
$$P=\not NP$$

---

## Proving NP-Completeness by a Reduction

Suppose $A$ is in $NP$-complete, $B$ is in $NP$, and you can show that $A\leq_p B$:
* since $A$ is in $NP$-hard, for every $C$ in $NP$:
  
  $$C\leq_p A$$
* for every $C$ in $NP$, we have $C\leq_p A$ and $A\leq B$, so for every $C$ in $NP$:
  
  $$C\leq_p B$$
  (*i.e. $B$ is in $NP$-hard*)
* and since $B$ is in $NP$, it follows that $B$ is in $NP$-complete

> $A$ in $NP$-complete reduces to $B$ in $NP \Rightarrow B$ is in $NP$ complete