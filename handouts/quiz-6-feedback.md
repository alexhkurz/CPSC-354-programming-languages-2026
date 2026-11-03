# Quiz 6 feedback

## Section S1

**(a)** Reduce $((\lambda x. \lambda y. x + y) 2) 3$ to normal form.

$$((\lambda x. \lambda y. x + y) 2) 3 \rightsquigarrow (\lambda y. 2 + y) 3 \rightsquigarrow 2 + 3 \rightsquigarrow 5$$

**(b)** Reduce $((\lambda x. \lambda y. y + x) 2) 3$ to normal form.

$$((\lambda x. \lambda y. y + x) 2) 3 \rightsquigarrow (\lambda y. y + 2) 3 \rightsquigarrow 3 + 2 \rightsquigarrow 5$$

**(c)** Reduce $((\lambda x. \lambda y. x + x) 2) 3$ to normal form.

$$((\lambda x. \lambda y. x + x) 2) 3 \rightsquigarrow (\lambda y. 2 + 2) 3 \rightsquigarrow 2 + 2 \rightsquigarrow 4$$

**(d)** Reduce $((\lambda x. \lambda y. y + y) 2) 3$ to normal form.

$$((\lambda x. \lambda y. y + y) 2) 3 \rightsquigarrow (\lambda y. y + y) 3 \rightsquigarrow 3 + 3 \rightsquigarrow 6$$

**(e)** Reduce $(\lambda x. x)((\lambda y. y) a)$ to normal form.

$$(\lambda x. x)((\lambda y. y) a) \rightsquigarrow (\lambda x. x) a \rightsquigarrow a$$

**(f)** Reduce $((\lambda x. \lambda y. x) y) q$ to normal form.

$$((\lambda x. \lambda y. x) y) q \rightsquigarrow ((\lambda x. \lambda z. x) y) q \rightsquigarrow (\lambda z. y) q \rightsquigarrow y$$

**(g)** Reduce $((\lambda x. \lambda y. y x) a) b$ to normal form.

$$((\lambda x. \lambda y. y x) a) b \rightsquigarrow (\lambda y. y a) b \rightsquigarrow b a$$

---

## Section S2

**(a)** Reduce $((\lambda x. \lambda y. x + y) 2) 3$ to normal form.

$$((\lambda x. \lambda y. x + y) 2) 3 \rightsquigarrow (\lambda y. 2 + y) 3 \rightsquigarrow 2 + 3 \rightsquigarrow 5$$

**(b)** Reduce $((\lambda x. \lambda y. y + x) 2) 3$ to normal form.

$$((\lambda x. \lambda y. y + x) 2) 3 \rightsquigarrow (\lambda y. y + 2) 3 \rightsquigarrow 3 + 2 \rightsquigarrow 5$$

**(c)** Reduce $((\lambda x. \lambda y. x + x) 2) 3$ to normal form.

$$((\lambda x. \lambda y. x + x) 2) 3 \rightsquigarrow (\lambda y. 2 + 2) 3 \rightsquigarrow 2 + 2 \rightsquigarrow 4$$

**(d)** Reduce $((\lambda x. \lambda y. y + y) 2) 3$ to normal form.

$$((\lambda x. \lambda y. y + y) 2) 3 \rightsquigarrow (\lambda y. y + y) 3 \rightsquigarrow 3 + 3 \rightsquigarrow 6$$

**(e)** Reduce $((\lambda x. \lambda y. y) u) v$ to normal form.

$$((\lambda x. \lambda y. y) u) v \rightsquigarrow (\lambda y. y) v \rightsquigarrow v$$

**(f)** Reduce $(\lambda x. x b) a$ to normal form.

$$(\lambda x. x b) a \rightsquigarrow a b$$

**(g)** Reduce $((\lambda x. \lambda y. x y) y) c$ to normal form.

$$((\lambda x. \lambda y. x y) y) c \rightsquigarrow ((\lambda x. \lambda z. x z) y) c \rightsquigarrow (\lambda z. y z) c \rightsquigarrow y c$$

---

## Section S3

**(a)** Reduce $((\lambda x. \lambda y. x + y) 2) 3$ to normal form.

$$((\lambda x. \lambda y. x + y) 2) 3 \rightsquigarrow (\lambda y. 2 + y) 3 \rightsquigarrow 2 + 3 \rightsquigarrow 5$$

**(b)** Reduce $((\lambda x. \lambda y. y + x) 2) 3$ to normal form.

$$((\lambda x. \lambda y. y + x) 2) 3 \rightsquigarrow (\lambda y. y + 2) 3 \rightsquigarrow 3 + 2 \rightsquigarrow 5$$

**(c)** Reduce $((\lambda x. \lambda y. x + x) 2) 3$ to normal form.

$$((\lambda x. \lambda y. x + x) 2) 3 \rightsquigarrow (\lambda y. 2 + 2) 3 \rightsquigarrow 2 + 2 \rightsquigarrow 4$$

**(d)** Reduce $((\lambda x. \lambda y. y + y) 2) 3$ to normal form.

$$((\lambda x. \lambda y. y + y) 2) 3 \rightsquigarrow (\lambda y. y + y) 3 \rightsquigarrow 3 + 3 \rightsquigarrow 6$$

**(e)** Reduce $(\lambda x. x x)(\lambda z. z)$ to normal form.

$$(\lambda x. x x)(\lambda z. z) \rightsquigarrow (\lambda z. z)(\lambda z. z) \rightsquigarrow \lambda z. z$$

**(f)** Reduce $((\lambda x. \lambda y. x + y) y) 2$ to normal form.

$$((\lambda x. \lambda y. x + y) y) 2 \rightsquigarrow ((\lambda x. \lambda z. x + z) y) 2 \rightsquigarrow (\lambda z. y + z) 2 \rightsquigarrow y + 2$$

**(g)** Reduce $((\lambda n. \lambda m. n m) m) n$ to normal form.

$$((\lambda n. \lambda m. n m) m) n \rightsquigarrow ((\lambda n. \lambda z. n z) m) n \rightsquigarrow (\lambda z. m z) n \rightsquigarrow m n$$
