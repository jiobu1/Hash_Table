## What Hash Table Solve?
* We need to look up  some data quickly
  * Some data that was slow to generate or obtain

In lieu of linear search...
It doesn't matter if _n_ is small. O(n) vs O(1)

**Any time-consuming process:**
* Memoization (caching)
* Network caching
* Indexing
* Removing duplicates from lists
* Detecting duplicates
* Counting duplicates

http://www.wiki.python.org/moin/TimeComplexity
```

                                          35
                                     /         \
                     34                                          33
                 /        \                                  /        \
             33                32                        32              31
            /  \              /  \                      /  \            /  \
         32      31        31      30                31      30      30      29
        /  \    /  \      /  \    /  \              /  \    /  \    /  \    /  \
       31  30  30  29    30  29   29  28           30  29  29  28  29  28  28  27
```

with memoization this can become an O(n) because previous number has already been stored

### Reading
SICT
Structure and Interpretation of Computer Programs

### Cryptographic Hash
emn178.github.io/online-tools/sha256.html
cryptography 