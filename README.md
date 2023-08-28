# RSA_Generate_tool
The RSA algorithm coded in Python

**RSA Algorithm**
* Pick two large primes $p,q$.
* Compute $n=pq$ and $\varphi(n)=\mathrm{lcm}(p-1,q-1)$
* Choose a public key $e$ such that $1< e< \varphi(n)$ and $\gcd(e,\varphi(n))=1$
* Calculate $d$ such that $de\equiv 1 \pmod\varphi(n)$
* Let the message **key** be $m$
* **Encrypt: ** $c\equiv m^e\pmod n$
* **Decrypt: ** $m\equiv c^d\pmod n$

## 3 different modes

- 1: generate RSA public and priv keys using default math function 
- 2: generate priv and pub keys using RSA library
- 3: decode encrypted message with private key 
