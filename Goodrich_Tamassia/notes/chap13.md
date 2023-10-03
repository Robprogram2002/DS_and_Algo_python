# Text Processing

In this chapter we explore some fundamental algorithms that can be used to efficiently analyze and process large textual
data sets. In addition to having interesting applications, text-processing algorithms also highlight some important
algorithmic design patterns

To allow fairly general notions of a string in our algorithm descriptions, we only assume that characters of a string
come from a known **alphabet**,which we denote as Σ.

In order to distinguish some special kinds of substrings, let us refer to any substring of the form S[0:k] for 0 ≤ k ≤ n
as a **prefix** of S; such a prefix results in Python when the first index is omitted from slice notation, as in S[:k].
Similarly, any substring of the form S[j:n] for 0 ≤ j ≤ n is a **suffix** of S; such a suffix results in Python when the
second index is omitted from slice notation, as in S[j:].

## Pattern-Matching Algorithms

We begin by examining the problem of searching for a pattern as a substring of a larger piece of text, for example, when
searching for a word in a document. The **pattern-matching problem** gives rise to the **brute-force method**, which is
often inefficient but has wide applicability.

> In the classic pattern-matching problem, we are given a text string T of length n and a **pattern** string P of length
> m, and want to find whether P is a substring of T.

If so, we may want to find the lowest index j within T at which P begins, such that T[j:j+m] equals P, or perhaps to
find all indices of T at which pattern P begins.

The pattern-matching problem is inherent to many behaviors of Python’s str class, such as PinT, T.find(P), T.index(P),
T.count(P), and is a subtask of more complex behaviors such as T.partition(P), T.split(P),and T.replace(P, Q).

### Brute Force

This algorithmic design pattern is a powerful technique for algorithm design when we have something we wish to search
for or when we wish to optimize some function. When applying this technique in a general situation, we typically
enumerate all possible configurations of the inputs involved and pick the best of all these enumerated configurations.

For the matching problem we simply test all the possible placements of P relative to T.

It consists of two nested loops, with the outer loop indexing through all possible starting indices of the pattern in
the text, and the inner loop indexing through each character of the pattern, comparing it to its potentially
corresponding character in the text. Thus, the correctness of the brute-force pattern-matching algorithm follows
immediately from this exhaustive search approach.

The running time of brute-force pattern matching in the worst case is not good, however, because, for each candidate
index in T, we can perform up to m character comparisons to discover that P does not match T at the current index.

we see that the outer for loop is executed at most n−m+1 times, and the inner while loop is executed at most m times.
Thus, the worst-case running time of the brute-force method is `O(nm)`

### The Boyer-Moore Algorithm

The Boyer-Moore pattern-matching algorithm can sometimes avoid comparisons between P and a sizable fraction of the
characters in T. we describe a simplified version of the original algorithm by Boyer and Moore.

The main idea is to improve the running time of the brute-force algorithm by adding two potentially time-saving
heuristics:

* **Looking-Glass Heuristic:** When testing a possible placement of P against T,begin the comparisons from the end of P
  and move backward to the front of P.
* **Character-Jump Heuristic:** During the testing of a possible placement ofP within T, a mismatch of text character
  T[i]=c with the corresponding pattern character P[k] is handled as follows. If c is not contained anywhere in P,then
  shift P completely past T[i] (for it cannot match any character in P). Otherwise, shift P until an occurrence of
  character c in P gets aligned with T[i].

The looking-glass heuristic sets up the other heuristic to allow us to avoid comparisons between P and whole groups of
characters in T. In this case at least, we can get to the destination faster by going backwards, for if we encounter a
mismatch during the consideration ofP at a certain location in T, then we are likely to avoid lots of needless
comparisons by significantly shifting P relative to T using the character-jump heuristic. The character-jump heuristic
pays off big if it can be applied early in the testing of a potential placement of P against T.

when a match is found for that last character, the algorithm continues by trying to extend the match with the
second-to-last character of the pattern in its current alignment. That process continues until either matching the
entire pattern, or finding a mismatch at some interior position of the pattern.

The efficiency of the Boyer-Moore algorithm relies on creating a lookup table that quickly determines where a mismatched
character occurs elsewhere in the pattern. In particular, we define a function last(c) as

* If c is in P, last(c) is the index of the last (rightmost) occurrence of c in P. Otherwise, we conventionally define
  last(c)= −1.

We prefer to use a hash table to represent the last function, with only those characters from the pattern occurring in
the structure. The space usage for this approach is proportional to the number of distinct alphabet symbols that occur
in the pattern, and thus O(m). The expected lookup time remains independent of the problem (although the worst-case
bound is O(m)).

The correctness of the Boyer-Moore pattern-matching algorithm follows from the fact that each time the method makes a
shift, it is guaranteed not to “skip” over any possible matches. For last(c) is the location of the last occurrence of c
in P.

**Performance**

If using a traditional lookup table, the worst-case running time of the Boyer-Moore algorithm is O(nm+|Σ|). Namely, the
computation of the last function takes time O(m+|Σ|), and the actual search for the pattern takes O(nm) time in the
worst case, the same as the brute-force algorithm.

The worst-case performance, however, is unlikely to be achieved for English text, for, in that case, the Boyer-Moore
algorithm is often able to skip large portions of text.

We have actually presented a simplified version of the Boyer-Moore algorithm. The original algorithm achieves running
timeO(n+m+|Σ|) by using an alternative shift heuristic to the partially matched text string, whenever it shifts the
pattern more than the character-jump heuristic. This alternative shift heuristic is based on applying the main idea from
the Knuth-Morris-Pratt pattern-matching algorithm, which we discuss next.

### The Knuth-Morris-Pratt Algorithm

we should notice a major inefficiency for both algorithms described before. For a certain alignment of the pattern, if
we find several matching characters but then detect a mismatch, we ignore all the information gained by the successful
comparisons after restarting with the next incremental placement of the pattern.

The **Knuth-Morris-Pratt** (or **“KMP”**) algorithm avoids this waste of information and, in so doing, it achieves a
running time of `O(n+m)`, which is asymptotically optimal. That is, in the worst case any pattern-matching algorithm
will have to examine all the characters of the text and all the characters of the pattern at least once. The main idea
of the KMP algorithm is to precompute self-overlaps between portions of the pattern so that when a mismatch occurs at
one location, we immediately know the maximum amount to shift the pattern before continuing the search.

To implement the KMP algorithm, we will precompute a **failure function**, f,that indicates the proper shift of P upon a
failed comparison. Specifically, the failure function f(k) is defined as the length of the longest prefix of P that is a
suffix of P[1:k+1] (note that we did not include P[0] here, since we will shift at least one unit). Intuitively, if we
find a mismatch upon character P[k+1], the function f(k) tells us how many of the immediately preceding characters can
be reused to restart the pattern.

The main part of the KMP algorithm is its while loop, each iteration of which performs a comparison between the
character at index j in T and the character at index k in P. If the outcome of this comparison is a match, the algorithm
moves on to the next characters in both T and P (or reports a match if reaching the end of the pattern). If the
comparison failed, the algorithm consults the failure function for a new candidate character in P, or starts over with
the next index in T if failing on the first character of the pattern (since nothing can be reused).

**Performance**

The algorithm for computing the failure function runs inO(m) time. Its analysis is analogous to that of the main KMP
algorithm, yet with a pattern of length m compared to itself. Thus, we have:

> **Proposition :** TheKnuth-Morris-Pratt algorithm performs pattern matching on a text string of length n and a pattern
> string of length m in O(n+m) time.

The correctness of this algorithm follows from the definition of the failure function. Any comparisons that are skipped
are actually unnecessary, for the failure function guarantees that all the ignored comparisons are redundant—they would
involve comparing the same matching characters over again.

## Dynamic Programming

