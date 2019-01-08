# Hamming & Reed-Solomon Codes

## Hamming Code

Not covering much as it isn't in the exam.

**(7,4)** Hamming code:

|bit|`000`|`001`|`010`|`011`|`100`|`101`|`110`|`111`|
|-|-|-|-|-|-|-|-|-|
|type|(parity)|parity|parity|data|parity|data|data|data|

Equations which define a valid codeword:
||||
|-|-|-|-|
|$p_{001} + d_{011} + d_{101} + d_{111}$|$=$|$0$|
|$p_{010} + d_{011} + d_{110} + d_{111}$|$=$|$0$|
|$p_{100} + d_{101} + d_{110} + d_{111}$|$=$|$0$|

### Decoding

Take a received word and check if all the parity bits are correct:
* yes $\to$ you can take the data bits
* no $\to$ add the indices of the incorrect parity bits to get the index of the incorrect bit (assuming one error)

> #### Example
> You receive `0110001`
> The equation:
> * $p_1 + d_3 + d_5 + d_7 = 0$ holds
> * $p_2 + d_3 + d_6 + d_7 = 0$ does not hold
> * $p_4 + d_5 + d_6 + d_7 = 0$ does not hold
> 
> $\therefore$ the mistakes must be bit $2+4=6$; the codeword should be `0110011` and the data bits should be `1011`

## Reed-Solomon Codes

The singleton bound gives us $d \leq n - k + 1$ for a linear code that turns $k$-bit messages into $n$-bit codewords.

Codes whose minimum distance $d$ is as high as this bound allows are called **Maximum Distance Seperable** (MDS) codes, such as **Reed-Solomon Codes**.

### Encoding

Pick a finite field $\mathbb{F}$ of size at least $n$ - call this size $q$.

Pick $n$ distinct points $x_1,\dots,x_n$ in $\mathbb{F}$.
To encode a message $m=m_0 + m_1x + m_2x^2 + \dots + m_{k-1}x^{k-1}$, view it as a polynomial:
$$M = m_0 + m_1x + m_2x^2 + \dots + m_{k-1}x^{k-1}$$
and compute the encoding:
$$E(m) = (M(x_1),M(x_2),\dots,M(x_n))$$

The generator matrix of the $(n,k,d=n-k+1)_q$ Reed-Solomon code is a **Vandermonde** matrix, transposed to have $k$ rows and $n$ columns.

The mininmum distance of the code is $d \geq n-k+1$ - the inequality must be exact.

### Decoding

You can test if there were any errors during transmission by interpolating a degree-bound $k-1$ polynomial from the first $k$ received values and testing if the **remaining values** lie on this polynomial.

If they do, then (assuming there were not more errors than this code can detect) the coeff. of the poly. give the original message back.

### Example

