
# Faulhaber's formulas

Using Bernoulli numbers to calculate the sum of first n natural numbers to the power of
p. This algorithm is generally slower for smaller n where brute forcing the sum wins out.
It is also slower than having the algorithm for a specific p being hardcoded. This 
alogrithm is useful when needing to sum the first n natural numbers when the power it 
is getting raised to cannot be determined before execution and n is fairly large such that
brute forcing isn't viable.


## Brute forcing vs. Hard Coding vs. Faulhaber's Formula

A simple brute force method of summing up the first n natural numbers to the power of numbers
is:
```
def brute_force(n,p):
    return sum([k**p for k in range(1,n+1)])
```
Hard coding the algorithm means removing the flexbility of changing p, and each case
of p must be hard coded.
```
def hard_coded(n,p):
    if p==1:
        return n*(n+1)/2
    if p==2:
        return n*(n+1)*(2*n+1)/6
    if p==3:
        return hard_coded(n,1)**2
```
...and so on.

Sometimes, adding each formula isn't feasible, for example having 100 possible values p can 
take on. So using Faulhaber's formula to calculate the result can help reduce time in coding.
But for small n, or where the same p may not be used, brute forcing can prove faster
to run and implement. Using Faulhaber's formula is only useful when n is large, or many
calculations are performed with a particular p.
```
import time

t1 = time.perf_counter()
faulhaber(1000,3)

t2 = time.perf_counter()
brute_force(1000,3)

t3 = time.perf_counter()
hard_coded(1000,3)

t4 = time.perf_counter()
```
In this code snippet, `t4-t3` and `t3-t2` will be much lesser than `t2-t1`. But on subsequent runs
`t2-t1` will be comparable to the time taken for `t4-t3` due to caching of the function.
And in subsequent `t3-t2` will be much greater than both the other runs. Hence running
```

t1 = time.perf_counter()
faulhaber(2346573,3)

t2 = time.perf_counter()
brute_force(2346573,3)

t3 = time.perf_counter()
hard_coded(2346573,3)

t3 = time.perf_counter()
```
Will yield extremely low times for `hard_coded` and `faulhaber` while `brute_force` will
take considerably longer. This is both due to the caching of the Bernoulli numbers and 
the binomial and the larger size of n. Hence, in cases involving multiple calls to a single
p or large n, faulhaber yields results comparable to hard coding the solution while also
not having to hard code each formula.


## References

https://en.wikipedia.org/wiki/Faulhaber%27s_formula

https://rosettacode.org/wiki/Bernoulli_numbers