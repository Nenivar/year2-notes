# Algorithmic Game Theory

Method of studying strategic solutions - outcomes that affect you depend on the actions of others.

---

## Red-Blue Game

Pick either red or blue.
|situation|red|blue|
|-|-|-|
|**one picks red, other blue**|$-1$|$3$|
|**both pick red**|$2$|$2$|
|**both pick blue**|$0$|$0$|

### Payoff matrix
* first number of row player's points
* second number is column player's points

||red|blue|
|-|-|-|
|red|$2,2$|$-1,3$
|blue|$3,-1$|$0,0$|

### Strictly Dominated Strategies

Pick **blue** - no matter what your pair does, you'll get more points that way.

> My strategy $i$ **strictly dominates** my strategy $j$, if my payoff from $i$ is always strictly greater than from $j$, *regardless of what my opponent does*
> 
> $\rightarrow$ do not play a strictly dominat**ed** strategy

### Rational Choice Outcomes

Rational choice for individuals (avoiding strictly dominated strategy) can lead to bad outcomes.

Players might have different strategy sets:
||left|centre|right|
|-|-|-|-|
|up|$3,-1$|$11,3$|$0,0$|
|down|$3,0$|$0,2$|$-1,0$|

Strategy $2$ for:
* row player: down
* column player: centre

Notation:
> $R[i,j]=$ payoff to row player - e.g. $R[1,2]=11$
> 
> $C[i,j]=$ payoff to column player - e.g. $C[1,2]=3$

### Strategy Dominance

> #### Dominated
> For some $j$, you can't do any **worse** by changing from $i$ to $j$, and in some circumstances you'll do better

> #### Strictly Dominated
> For some $j$, you'll always do better by changing from $i$ to $j$

Where $m$ = # row player strategies,
$n$ = # column player strategies:
> #### Row Player
> Row-player's strategy $i$ is:
> * **dominated** if for some $j \in \{1,\dots,m\}$:
>   * $R[i,k] \leq R[j,k]$ for all $k \in \{1,\dots,n\}$
>   * $R[i,k] < R[j,k]$ for some $k \in \{1,\dots,n\}$
> * **strictly dominated** if for some $j \in \{1,\dots,m\}$:
>   * $R[i,k] < R[j,k]$ for all $k \in \{1,\dots,n\}$

> #### Column Player
> Column-player's strategy $i$ is:
> * **dominated** if for some $j \in \{1,\dots,n\}$:
>   * $C[k,i] \leq R[k,j]$ for all $k \in \{1,\dots,m\}$
>   * $C[k,i] < R[k,j]$ for some $k \in \{1,\dots,ms\}$
> * **strictly dominated** if for some $j \in \{1,\dots,n\}$:
>   * $R[k,i] < R[k,j]$ for all $k \in \{1,\dots,m\}$

---

## Rock-Paper-Scissors

||Rock|Paper|Scissors|
|-|-|-|-|
|Rock|$0,0$|$-1,1$|$1,-1$|
|Paper|$1,-1$|$0,0$|$-1,1$|
|Scissors|$-1,1$|$1,-1$|$0,0$|

No dominated strategies.

How to not lose:
* At each go, pick rock, paper, or scissors with equal probabilties.
* The other player's expected payoff is $\frac{1}{3} \cdot 1 + \frac{1}{3} \cdot -1 + \frac{1}{3} \cdot 0=0$

It's not possible to beat this strategy on average.

### Mixed Strategies

On each turn, play your strategy $i$ with probability $p_i$, where $0 \leq p_i \leq 1$ and $\sum_{1\leq i\leq m}p_i=1$

Write this **mixed strategy** as the vector $p=(p_1,\dots,p_m)$

> #### Notation
> $S_R,S_C$ are the sets of mixed strategies for the row player and column player.
> 
> If row player plays $p$ in $S_R$ and column player plays $q$ in $S_C$ then:
> * Expected payoff to row player:
>   $$R[p,q] = \sum_{1\leq i\leq m, 1\leq j\leq n} p_i \cdot q_j \cdot R[i,j]$$
> * Expected payoff to column player:
>   $$C[p,q] = \sum_{1\leq i\leq m, 1\leq j\leq n} p_i \cdot q_j \cdot C[i,j]$$

---

## Curry vs Pizza

||Curry !!|Pizza OK|
|-|-|-|
|Curry OK|$1,5$|$0,0$|
|Pizza !!|$0,0$|$5,1$|

If $p=(\frac{1}{6},\frac{5}{6}), q=(\frac{5}{6},\frac{1}{6})$ then $R[p,q]=$
$$(\frac{1}{6} \cdot \frac{5}{6} \cdot 1) + (\frac{1}{6} \cdot \frac{1}{6} \cdot 0) + (\frac{5}{6} \cdot \frac{5}{6} \cdot 0) + (\frac{5}{6} \cdot \frac{1}{6} \cdot 5)$$
$$= \frac{30}{36} = \frac{5}{6}$$

### Nash Equilibrium

A pair of mixed strategies $(p,q)$ for the row and column players respectively is called a **Nash Equilibrium**.

> #### Nash Equilibrium
> If neither player can increase her payoff by unilaterally deviating from her strategy.
> 
> ##### Formal definition:
> A nash equilibrium for a 2-player game is a pair $(p,q)$  with $p$ in $S_R,q$ in $S_C$ satisfying:
> * $R[p,q] \geq R[p',q]$ for all $p' \in S_R$
> * $C[p,q] \geq C[p,q']$ for all $q' \in S_C$
 
Players don't always play NE, but:
* **No regrets**: if you played a NE, you could say afterwards 'given what the other player did, I have no regrets'
* **Self-fulfilling belief** if I believe the other player will play their part of a NE, I can't get a better payoff than if I play my part - so I play my part

> Every game that can be specified by a payoff matrix has a Nash Equilibrium *(may have more than one)*

For Curry vs Pizza:
* $((1,0), (1,0))$ and $((0,1), (0,1))$ are Nash Equilibria
* So is $((\frac{1}{6}, \frac{5}{6}), (\frac{5}{6}, \frac{1}{6}))$

> #### Checking Nash Equilibria
> To check if $(p=(p_1,\dots,p_m), q=(q_1,\dots,q_n))$ is a Nash Equilibrium:
> * want $R[p,q] \geq R[p',q]$ for all $p'$ in $S_R$
> * want $C[p,q] \geq C[p,q']$ for all $q'$ in $S_C$
> 
> * $R[p',q] = \sum_{i\leq j\leq n} p'_i \cdot R[i,q]$ - weighted average of $R[i,q], 1\leq i\leq m$
> * $C[p,q'] = \sum_{1\leq j\leq n} q'_j \cdot C[p,j]$ - weighted average of $C[p,j], 1\leq j\leq n$
> 
> $\therefore$ it's enough to check that
> * $R[p,q] \geq R[i,q]$ for $i=1,\dots,m$
> * $C[p,q] \geq C[p,j]$ for $j=1,\dots,n$
> 
> > ##### Example:
> > Check  $(p,q)$ is a NE where $p=(\frac{1}{6},\frac{5}{6}), q=(\frac{5}{6},\frac{1}{6})$:
> * check $R[p,q] \geq R[1,q], R[p,q], \geq R[2,q]$
> * check $C[p,q] \geq C[p,1], C[p,q] \geq C[p,2]$
> 
> What are $C[p,q], C[p,q], C[p,2]$?
> 
> * $C[p,q] = (\frac 1 6 \cdot \frac 5 6 \cdot 5) + (\frac 5 6 \cdot \frac 1 6 \cdot 1) = \frac{30}{36} = \frac 5 6$
> * $C[p,1] = (\frac 1 6 \cdot 5) + (\frac 5 6 \cdot 0) = \frac 5 6, \leq C[p,q]$ as required
> * $C[p,2] = (\frac 1 6 \cdot 0) + (\frac 5 6 \cdot 1) = \frac 5 6, \leq C[p,q]$ as required
> 
> Check $(p,q)$ where $p=(\frac 2 3, \frac 1 3), q=(\frac 2 3, \frac 1 3)$
> * $R[p,q] = (\frac 2 3 \cdot \frac 2 3) \cdot 1 + (\frac 2 3 \cdot \frac 1 3)\cdot 0 + (\frac 1 3 \cdot \frac 2 3)\cdot 0 + (\frac 1 3 \cdot \frac 1 3)\cdot 5 = 1$
> * $R[p,q] = (\frac 2 3) \cdot 0 + (\frac 1 3)\cdot 5 = \frac 5 3$, greater than $R[p,q]$
> 
> $(\frac 2 3, \frac 1 3), (\frac 2 3, \frac 1 3)$ is **not** a Nash Equilibrium

---

## Zero-Sum Games

> Definition:
> A game is **zero-sum** if
> $$R[i,j] + C[i,j] = 0$$
> for all $i$ in $S_R, j$ in $S_C$
> 
> For example: rock-paper-scissors

Election example (zero-sum):

||Security|Tax Cuts|
|-|-|-|
|Economy|$3,-3$|$-1,1$|
|Student Fees|$-2,2$|$1,-1$|

> #### Announcing a Strategy in Advance
> Suppose row player has to announce their strategy $p=(p_1,p_2)$ in advance
> * expected payoffs $R[p,j]: 3p_1-2p_2$ if column player picks 'security', $-p_1+p_2$ if column player picks 'Tax cuts'
> * column player will pick whichever $j$ **maximizes** $C[p,j]$
> * zero-sum game, so this is the $j$ that **minimizes** $R[p,j]$
> * so row player's expected payoff is $min \{ 3p_1-2p_2, -p_1+p_2\}$
>   
>   $\rightarrow$ row player picks $(p_1,p_2)$ to maximize $min\{3p_1-2p_2, -p_1+p_2\}$
> 
> #### Picking What Strategy to Announce
> * **Row** player: pick $(p_1,p_2)$ to maximize $min\{3p_1-2p_2, -p_1+p_2\}$
> 
>   We can write this as a linear program:
>   |||
>   |-|-|
>   |maximize|$z$|
>   |subject to|$3p_1-2p_2-z\geq0$|
>   ||$-p_1+p_2-z\geq0$|
>   ||$p_1+p_2=1$|
>   ||$p_1,p_2\geq0$|
>   
>   Solution: $p_1=\frac 3 7, p_2 = \frac 4 7, z=\frac 1 7$
> 
> * **Column** player: pick $(q_1,q_2)$ to maximize $min\{-3q_1+q_2, 2q_1-q_2\}$
>   |||
>   |-|-|
>   |maximize|$w$|
>   |subject to|$-3q_1+q_2-w\geq0$|
>   ||$2q_1-q_2-w\geq0$|
>   ||$q_1+q_2=1$|
>   ||$q_1,q_2\geq0$|
> 
> Solution: $q_1=\frac 2 7, q_2=\frac 5 7, w=\frac {-1} 7$
> 
> #### Analysis
> If row player plays $(p_1,p_2) = (\frac 3 7, \frac 4 7)$, their expected payoff is at least
> $$z=\frac 1 7$$
> If column player plays $(q_1,q_2) = (\frac 2 7, \frac 5 7)$, their expected payoff is at least 
> $$w=\frac {-1} 7$$
> 
> Sum of these two **minimum** expected payoffs $= 0$
> 
> So $(\frac 2 7, \frac 5 7), (\frac 3 7, \frac 4 7)$ is a **Nash Equilibrium**

This is true for all $2$-player zero-sum games - we cacn find a Nash Equilibrium for these games using Linear Programming.