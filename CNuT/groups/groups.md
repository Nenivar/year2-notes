# Groups

Group $\mathbb{G} = (G, +)$:

* set $G$
* operation $+: G\times G \rightarrow G$
* properties:
  * **associative**:
    * $g, h, k \in G$
    * $g + (h + k) = (g + h) + k$
  * **neutral element**:
    * $\forall g \in G,$
    * $e + g = g; g + e = g$
    * where $e$ = neutral element
  * **inverse**:
    * $\forall g \in G,$
    * $h + g = e; g + h = e$
    * where $h = (-g)$
* restrictions:
  1. one neutral element
  2. one inverse per element
  3. you can cancel out elements
     * $h + g = k + g$
       
       $\rightarrow h=k$
* order:
  * finite w/ $n$ elements: $n$
  * infinite: $\infty$

> $\mathbb{Z}_n$ is commutative

## Relations

A relation $R$ on a set $S$ is an equivalence relation (~) if it is:

* **reflexive**:
  * $\forall a \in S$
    
    $a R a$
* **symmetric**:
  * $\forall a,b \in S$
    
    if $a R b$ then $b R a$
* **transitive**:
  * $\forall a,b,c \in S$
    
    if $a R b$ and $b R c$ then $a R c$

with this we can do $S/$~, ($S$ modulo ~)

For a fixed modulus $n$, $[x]$ is the map $\mathbb{Z} \rightarrow \mathbb{Z}$ that sends $x$ to its remainder modulo $n$.