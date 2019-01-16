# Linear Programming

1. Linear Program
2. Standard Form
3. Slack Form
4. Simplex Algorithm

---

## Standard Form

1. If obj. function is minimise, maximise
   
   > e.g. minimise $4x+y+z\rightarrow$ maximise $-4x-y-z$
2. Variable does not have non-neg constraint
   $\rightarrow 2$ variables with non-neg constraints

   > e.g.
   > ||||
   > |-|-|-|
   > |$x-y=6$|$\rightarrow$|$x'-x''-y=6$|
   > |$x+2z\geq24$|$x=x'-x''$|$x'-x''+2z'-2z''\geq24$|
   > |$y\geq0$|$z=z'-z''$|$y,x',x'',z',z''\geq0$|
   > |$z\leq0$||
3. Equality $\rightarrow 2$ inequalities
   
   > e.g.
   > ||||
   > |-|-|-|
   > |$2x+y=5$|$\rightarrow$|$2x+y\geq5$|
   > |||$2x+y\leq5$|
4. Inequalities in correct form (i.e. function $\leq$ constant - negate both sides if not  )
   
   > e.g. $ax+by\leq c$

> #### Example:
> TODO

---

## Slack Form

A.K.A simplex init.

### Feasible Basic Solution

1. Set new variable $z=$ objective function
2. For each inequality:
   * introduce a new variable (e.g. $a,b$)
   * rewrite the inequality

> #### Example
> |||||
> |-|-|-|-|
> |max|$3x+2y$|$\rightarrow$|$Z=3x+2y$|
> ||$x+y\leq7$||$a=7-x-y$|
> ||$2x-y\leq2$||$b=2-2x+y$|
> ||$x,y\geq0$||$x,y\geq0$|

### Infeasible Basic Solution

1. Derive an auxiliary linear program $L_{aux}$ from $L$
   
   > e.g. 
   > ||||||
   > |-|-|-|-|-|
   > |maximize|$2x_1-x_2$|$\rightarrow$|maximize|$-x_0$|
   > ||$2x_1-x_2\leq2$|||$2x_1-x_2-x_0\leq2$|
   > ||$x_1-5x_2\leq-4$|||$x_1-5x_2-x_0\leq-4$|
   > ||$x_1,x_2\geq0$|||$x_0,x_1,x_2\geq0$|
2. Solve $L_{aux}$
   1. Convert to slack form
   2. Do a pivot with $x_0$ and a basic variable with the largest $-$ve constant
   3. Pivot\iterate until we find an optimal solution (objective value = 0)
3. Use the final form of $L_{aux}$ to get a slack form for $L$ with feasible basic solution
   * $L_{aux}$:
     
     $z=-x_0$

     $x_3=\frac 14 5 + \frac 4 5 x_0 - \frac 9 5 x_1 + \frac 1 5 x_4$

     $x_2=\frac 4 5 + \frac 1 5 x_0 + \frac 1 5 x_1 + 
     \frac 1 5 x_4$

   * Objective function for L = $2x_1-x_2$
   * Rewrite this in terms of non-basic variables:
     
     $2x_1 - \frac 4 5 + \frac 1 5 x_0 - \frac 1 5 x_1 - \frac 1 5 x_4$
   * Set $x_0$ to $0$ and simplify:
     
     $\frac {-4} 5 + \frac 9 5 x_1 - \frac 1 5 x_1$
   * To get L, replace objective function in $L_{aux}$ by this and set $x_0$ to $0$ in other equations too
   * Resulting slack form:
     
     $z = -\frac 4 5 + \frac 9 5 x_1 - \frac 1 5 x_1$

     $x_3 = \frac 14 5 - \frac 9 5 x_1 + \frac 1 5 x_4$

     $x_2 = \frac 4 5 + \frac 1 5 x_1 + \frac 1 5 x_4$

> L is feasible iff the optimal value of $L_{aux}$ is $0$

> #### Example
> TODO

---

## Simplex Algorithm

1. Find basic solution
2. Pivot/iterate until we find an optimal solution

### Basic Solution

Set all non-basic variables to 0.

> #### Example
> TODO

### Pivot

While there are positive non-basic variables:

1. Select a non-basic variable with a positive coefficient in the objective function
2. Increase the variable as much as possible without increasing any non-negativity constraints
3. Find the tightest constraint
4. Switch roles of basic and non-basic variables

> #### Example
> TODO