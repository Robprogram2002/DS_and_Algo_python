# Search Trees

We'll use a **search tree** structure to efficiently implement a **sorted map**.

## Binary search tree

A **binary search tree** is a binary tree T with each position p storing a key-value pair (k,v) such that:

* Keys stored in the left subtree of p are less than k.
* Keys stored in the right subtree of p are greater than k

a binary search tree hierarchically represents the sorted order of its keys. In particular, the structural property
regarding the placement of keys within a binary search tree assures the following important consequence regarding an
**inorder traversal** of the tree.

> **Proposition :** An inorder traversal ofa binary search tree visits positions in increasing order oftheir keys.

a consequence of this proposition is that we can produce a sorted iteration of the keys of a map in linear time, when
represented as a binary search tree. Although an inorder traversal is typically expressed using a top-down recursion, we
can provide non-recursive descriptions of operations that allow more fine-grained navigation among the positions of a
binary search relative to the order of their keys.

With a binary search tree, we can provide additional navigation based on the natural order of the keys stored in the
tree. In particular, we can support the following methods, akin to those provided by a PositionalList

* first(): Return the position containing the least key, or None if the tree is empty.
* last(): Return the position containing the greatest key, or None if empty tree.
* before(p): Return the position containing the greatest key that is less than that of position p, or None if p is the
  first position.
* after(p): Return the position containing the least key that is greater than that of position p or None if p is the
  last position.

The “first” position of a binary search tree can be located by starting a walk at the root and continuing to the left
child, as long as a left child exists. By symmetry, the last position is reached by repeated steps rightward starting at
the root.

The successor of a position, after(p), is determined by the following algorithm.

    Algorithm after(p): 
      if right(p) is not None then      {successor is leftmost position in p’s right subtree} 
        walk = right(p) 
        while left(walk) is not None do 
          walk = left(walk)
        return walk
      else                              {successor is nearest ancestor having p in its left subtree} 
        walk = p 
        ancestor = parent(walk) 
        while ancestor is not None and walk == right(ancestor) do 
          walk = ancestor 
          ancestor = parent(walk)
        return ancestor

The rationale for this process is based purely on the workings of an inorder traversal, given the correspondence of last
Proposition. If p has a right subtree, that right subtree is recursively traversed immediately after p is visited, and
so the first position to be visited after p is the leftmost position within the right subtree.

If p does not have a right subtree, then the flow of control of an inorder traversal returns to p’s parent. If p were in
the right subtree of that parent, then the parent’s subtree traversal is complete and the flow of control progresses to
its parent and so on. Once an ancestor is reached in which the recursion is returning from its left subtree, then that
ancestor becomes the next position visited by the inorder traversal, and thus is the successor of p. Notice that the
only case in which no such ancestor is found is when p was the rightmost (last) position of the full tree, in which case
there is no successor.

A symmetric algorithm can be defined to determine the predecessor of a position, before(p). At this point, we note that
the running time of single call to after(p) or before(p) is bounded by the height h of the full tree, because it is
found after either a single downward walk or a single upward walk. While the worst-case running time is O(h), we note
that either of these methods run in O(1) amortized time, in that series of n calls to after(p) starting at the first
position will execute in a total of O(n) time.

### Searches

We can attempt to locate a particular key in a binary search tree by viewing it as a decision tree. In this case, the
question asked at each position p is whether the desired key k is less than, equal to, or greater than the key stored at
position p, which we denote as p.key().If the answer is “less than,” then the search continues in the left subtree. If
the answer is “equal,” then the search terminates successfully. If the answer is “greater than,” then the search
continues in the right subtree. Finally, if we reach an empty subtree, then the search terminates unsuccessfully.

    Algorithm TreeSearch(T, p, k): 
      if k == p.key() then 
        return p
      else if k < p.key() and T.left(p) is not None then 
        return TreeSearch(T, T.left(p), k)
      else if k > p.key() and T.right(p) is not None then 
        return TreeSearch(T, T.right(p), k)
      return p

If key k occurs in a subtree rooted at p, a call to `TreeSearch(T, p, k)` results in the position at which the key is
found; in this case, the getitem map operation would return the associated value at that position. In the event of an
unsuccessful search, the TreeSearch algorithm returns the final position explored on the search path.

The analysis of the worst-case running time of searching in a binary search tree T is simple. Algorithm TreeSearch is
recursive and executes a constant number of primitive operations for each recursive call. Each recursive call of
TreeSearch is made on a child of the previous position. That is, TreeSearch is called on the positions of a path of T
that starts at the root and goes down one level at a time. Thus, the number of such positions is bounded by h+1, where h
is the height of T. In other words, since we spend O(1) time per position encountered in the search, the overall search
runs in O(h) time, where h is the height of the binary search tree T.

In the context of the sorted map ADT, the search will be used as a subroutine for implementing the __getitem__ method,
as well as for the __setitem__ and __delitem__ methods, since each of these begins by trying to locate an existing item
with a given key. To implement sorted map operations such as find_lt and find_gt, we will combine this search with
traversal methods before and after. All of these operations will run in worst-case O(h) time for a tree with height h.We
can use a variation of this technique to implement the find_range method in time O(s+h),where s is the number of items
reported.

Admittedly, the height h of T can be as large as the number of entries, n,but we expect that it is usually much smaller.
Indeed, later in this chapter we show various strategies to maintain an upper bound of O(logn) on the height of a search
tree T.

### Insertions and Deletions

Insertion begins with a search for key k (assuming the map is nonempty). If found, that item’s existing value is
reassigned. Otherwise, a node for the new item can be inserted into the underlying tree T in place of the empty subtree
that was reached at the end of the failed search. The binary search tree property is sustained by that placement (note
that it is placed exactly where a search would expect it)

Deleting an item from a binary search tree T is a bit more complex than inserting a new item because the location of the
deletion might be anywhere in the tree. (In contrast, insertions are always enacted at the bottom of a path.) To delete
an item with key k, we begin by calling TreeSearch(T, T.root(), k) to find the position p of T storing an item with key
equal to k. If the search is successful, we distinguish between two cases (of increasing difficulty):

* If p has at most one child, the deletion of the node at position p is easily implemented. When introducing update
  methods for the LinkedBinaryTree, we declared a nonpublic utility, delete(p), that deletes a node at position p and
  replaces it with its child (if any), presuming that p has at most one child. That is precisely the desired behavior.
  It removes the item with key k from the map while maintaining all other ancestor-descendant relationships in the tree
* If position p has two children, instead we proceed as follows:
    1. We locate position r containing the item having the greatest key that is strictly less than that of position
       p,that is, `r= before(p)`. Because p has two children, its predecessor is the rightmost position of the left
       subtree of p.
    2. We use r’s item as a replacement for the one being deleted at position p. Because r has the immediately preceding
       key in the map, any items in p’s right subtree will have keys greater than r and any other items in p’s left
       subtree will have keys less than r. Therefore, the binary search tree property is satisfied after the replacement
    3. Having used r’s as a replacement for p, we instead delete the node at position r from the tree. Fortunately,
       since r was located as the rightmost position in a subtree, r does not have a right child. Therefore, its
       deletion can be performed using the first (and simpler) approach.

As with searching and insertion, this algorithm for a deletion involves the traversal of a single path downward from the
root, possibly moving an item between two positions of this path, and removing a node from that path and promoting its
child. Therefore, it executes in time O(h) where h is the height of the tree.

### Python Implementation

we define a TreeMap class that implements the sorted map ADT using a binary search tree. In fact, our implementation is
more general. We support all the standard map operations all additional sorted map operations and positional operations
including first(), last(), find position(k), before(p), after(p),and delete(p).

Our TreeMap class takes advantage of multiple inheritance for code reuse, inheriting from the LinkedBinaryTree class for
our representation as a positional binary tree, and from the MapBase class. to provide us with the key-value composite
item and the concrete behaviors from the collections.MutableMapping abstract base class. We subclass the nested Position
class to support more specific p.key() and p.value() accessors for our map, rather than the p.element() syntax inherited
from the tree ADT.

### Performance of a Binary Search Tree

Almost all operations have a worst-case running time that depends on h,where h is the height of the current tree. This
is because most operations rely on a constant amount of work for each node along a particular path of the tree, and the
maximum path length within a tree is proportional to the height of the tree.

We note that although a single call to the after method has worst-case running time ofO(h), the n successive calls made
during a call to iter require a total of O(n) time, since each edge is traced at most twice; in a sense, those calls
have O(1) amortized time bounds. A similar argument can be used to prove the O(s +h) worst-case bound for a call to find
range that reports s results

A binary search tree T is therefore an efficient implementation of a map with n entries only if its height is small. In
the best case, T has height `h= |log(n+1)| −1`, which yields logarithmic-time performance for all the map operations. In
the worst case, however, T has height n, in which case it would look and feel like an ordered list implementation of a
map. Such a worst-case configuration arises, for example, if we insert items with keys in increasing or decreasing
order.

We can nevertheless take comfort that, on average, a binary search tree with n keys generated from a random series of
insertions and removals of keys has expected height O(logn).

## Balanced Search Trees

if we could assume a random series of insertions and removals, the standard binary search tree supports O(logn) expected
running times for the basic map operations. However, we may only claim O(n) worst-case time, because some sequences of
operations may lead to an unbalanced tree with height proportional to n.

In the remainder, we explore four search tree algorithms that provide stronger performance guarantees. Three of the four
data structures (AVL trees, splay trees, and red-black trees) are based on augmenting a standard binary search tree with
occasional operations to reshape the tree and reduce its height.

The primary operation to re-balance a binary search tree is known as a **rotation**. During a rotation, we “rotate” a
child to be above its parent.

To maintain the binary search tree property through a rotation, we note that if position x was a left child of position
y prior to a rotation then y becomes the right child of x after the rotation, and vice versa. Furthermore, we must
relink the subtree of items with keys that lie between the keys of the two positions that are being rotated.

> Because a single rotation modifies a constant number of parent-child relationships, it can be implemented in O(1) time
> with a linked binary tree representation.

In the context of a tree-balancing algorithm, a rotation allows the shape of a tree to be modified while maintaining the
search tree property. If used wisely, this operation can be performed to avoid highly unbalanced tree configurations.
One or more rotations can be combined to provide broader re-balancing within a tree. One such compound operation we
consider is a **trinode restructuring**. For this manipulation, we consider a position x, its parent y, and its
grandparent z. The goal is to restructure the subtree rooted at z in order to reduce the overall path length to x and
its subtrees

    Algorithm restructure(x): 
        Input: A position x of a binary search tree T that has both a parent y and a grandparent z
        Output: Tree T after a trinode restructuring (which corresponds to a single or double rotation) 
        involving positions x, y,and z

        1: Let (a, b, c) be a left-to-right (inorder) listing of the positions x, y,and z,and let (T1,T2,T3,T4) 
        be a left-to-right (inorder) listing of the four subtrees of x, y,and z not rooted at x, y,or z.
        2: Replace the subtree rooted at z with a new subtree rooted at b. 
        3: Let a be the left child of b and let T1 and T2 be the left and right subtrees of a, respectively.
        4: Let c be the right child of b and let T3 and T4 be the left and right subtrees of c, respectively

In practice, the modification of a tree T caused by a trinode restructuring operation can be implemented through case
analysis either as a single rotation or as a double rotation. The double rotation arises when position x has the middle
of the three relevant keys and is first rotated above its parent, and then above what was originally its grandparent. In
any of the cases, the trinode restructuring is completed with O(1) running time.

### Python Framework for Balancing Search Trees

Our TreeMap class is a concrete map implementation that does not perform any explicit balancing operations. However, we
designed that class to also serve as a base class for other subclasses that implement more advanced tree-balancing
algorithms.

Our implementation of the basic map operations includes strategic calls to three nonpublic methods that serve as hooks
for rebalancing algorithms:

* A call to **_rebalance_insert(p)** is made from within the setitem method immediately after a new node is added to the
  tree at position p.
* A call to **_rebalance_delete(p)** is made each time a node has been deleted from the tree, with position p
  identifying the parent of the node that has just been removed. Formally, this hook is called from within the public
  delete(p) method, which is indirectly invoked by the public `__delitem__(k)` behavior.
* We also provide a hook, **_rebalance_access(p)**, that is called when an item at position p of a tree is accessed
  through a public method such as `__getitem__`. This hook is used by the splay tree structure to restructure a tree so
  that more frequently accessed items are brought closer to the root.

A subclass of TreeMap may override any of these methods to implement a nontrivial action to rebalance a tree. This is
another example of the **template method design pattern**,

#### Nonpublic Methods for Rotating and Restructuring

A second form of support for balanced search trees is our inclusion of nonpublic utility methods rotate and restructure
that, respectively, implement a single rotation and a trinode restructuring. Although these methods are not invoked by
the public TreeMap operations, we promote code reuse by providing these implementation in this class so that they are
inherited by all balanced-tree subclasses.

To simplify the code, we define an additional relink utility that properly links parent and child nodes to each other,
including the special case in which a “child” is a None reference. The focus of the rotate method then becomes
redefining the relationship between the parent and child, relinking a rotated node directly to its original grandparent,
and shifting the “middle” subtree between the rotated nodes. For the trinode restructuring, we determine whether to
perform a single or double rotation,

#### Factory for Creating Tree Nodes

The low-level definition of a node is provided by the nested Node class within LinkedBinaryTree. Yet, several of our
tree-balancing strategies require that auxiliary information be stored at each node to guide the balancing process.
Those classes will override the nested Node class to provide storage for an additional field.

Whenever we add a new node to the tree we intentionally instantiate the node using the syntax `self.Node`, rather than
the qualified name `LinkedBinaryTree.Node` . This is vital to our framework! When the expression self. Node is applied
to an instance of a tree (sub)class, Python’s name resolution follows the inheritance structure. If a subclass has
overridden the definition for the Node class, instantiation of `self.Node` relies on the newly defined node class. This
technique is an example of the **factory method design pattern**, as we provide a subclass the means to control the type
of node that is created within methods of the parent class.

## AVL Trees

we describe a simple balancing strategy that guarantees worst-case logarithmic running time for all the fundamental map
operations. we describe a simple balancing strategy that guarantees worst-case logarithmic running time for all the
fundamental map operations.

it is easier for explanation in this section to consider the height of a subtree rooted at position p to be the number
of nodes on the longest path from p to a leaf. By this definition, a leaf position has height 1, while we trivially
define the height of a “null” child to be 0.

we consider the following **height-balance property**, which characterizes the structure of a binary search tree T in
terms of the heights of its nodes.

> For every position p of T, the heights of the children of p differ by at most 1.

Any binary search tree T that satisfies the height-balance property is said to be an **AVL tree**, named after the
initials of its inventors: Adel’son-Vel’skii and Landis.

An immediate consequence of the height-balance property is that a subtree of an AVL tree is itself an AVL tree. The
height-balance property has also the important consequence of keeping the height small.

> **Proposition :** The height of an AVL tree storing n entries is O(logn).

### Update Operations

Given a binary search tree T, we say that a position is **balanced** if the absolute value of the difference between the
heights of its children is at most 1, and we say that it is **unbalanced** otherwise. Thus, the height-balance property
characterizing AVL trees is equivalent to saying that every position is **balanced**.

The insertion and deletion operations for AVL trees begin similarly to the corresponding operations for (standard)
binary search trees, but with post-processing for each operation to restore the balance of any portions of the tree that
are adversely affected by the change.

#### Insertion

An insertion of a new item in a binary search tree results in a new node at a leaf position p.This action may violate
the height-balance property yet the only positions that may become unbalanced are ancestors of p, because those are the
only positions whose subtrees have changed. Therefore, let us describe how to restructure T to fix any unbalance that
may have occurred (T is an AVL tree before insertion).

We can do this by a simple “search-and-repair” strategy. In particular, let z be the first position we encounter in
going up from p toward the root of T such that z is unbalanced. Also, let y denote the child of z with higher height (
and note that y must be an ancestor of p). Finally, let x be the child of y with higher height (there cannot be a tie
and position x must also be an ancestor of p, possibly p itself). We rebalance the subtree rooted at z by calling the
trinode restructuring method, restructure(x).

Since z is the nearest ancestor of p that became unbalanced after the insertion of p, it must be that the height of y
increased by one due to the insertion and that it is now 2 greater than its sibling. Since y remains balanced, it must
be that it formerly had subtrees with equal heights, and that the subtree containing x has increased its height by one.

After the trinode restructuring, we see that each of x, y,and z has become balanced. Furthermore, the node that becomes
the root of the subtree after the restructuring has height h+2, which is precisely the height that z had before the
insertion of the new item. Therefore, any ancestor of z that became temporarily unbalanced becomes balanced again, and
this one restructuring restores the heightbalance property globally.

#### Deletion

In particular, if position p represents the parent of the removed node in tree T, there may be an unbalanced node on the
path from p to the root of T. In fact, there can be at most one such unbalanced node.

As with insertion, we use trinode restructuring to restore balance in the tree T. In particular, let z be the first
unbalanced position encountered going up from p toward the root of T. Also, let y be the child of z with larger height (
note that position y is the child of z that is not an ancestor of p), and let x be the child of y defined as follows: If
one of the children of y is taller than the other, let x be the taller child of y; else (both children of y have the
same height), let x be the child of y on the same side as y. In any case, we then perform a restructure(x) operation.

The height-balance property is guaranteed to be locally. Unfortunately, this trinode restructuring may reduce the height
of the subtree rooted at b by 1, which may cause an ancestor of b to become unbalanced. So, after rebalancing z, we
continue walking up T looking for unbalanced positions. If we find another, we perform a restructure operation to
restore its balance, and continue marching up T looking for more, all the way to the root.

### Performance of AVL Trees

Because the standard binary search tree operation had running times bounded by the height and because the additional
work in maintaining balance factors and restructuring an AVL tree can be bounded by the length of a path in the tree,
the traditional map operations run in worst-case logarithmic time with an AVL tree.

### Python Implementation

We highlight two important aspects of our implementation. First, the AVLTreeMap overrides the definition of the nested
Node class, in order to provide support for storing the height of the subtree stored at a node. We also provide several
utilities involving heights of nodes, and the corresponding positions.

To implement the core logic of the AVL balancing strategy, we define a utility, named rebalance, that suffices as a hook
for restoring the height-balance property after an insertion or a deletion. Although the inherited behaviors for
insertion and deletion are quite different, the necessary post-processing for an AVL tree can be unified. In both cases,
we trace an upward path from the position p at which the change took place, recalculating the height of each position
based on the (updated) heights of its children, and using a trinode restructuring operation if an imbalanced position is
reached. If we reach an ancestor with height that is unchanged by the overall map operation, or if we perform a trinode
restructuring that results in the subtree having the same height it had before the map operation, we stop the process;
no further ancestor’s height will change. To detect the stopping condition, we record the “old” height of each node and
compare it to the newly calculated height.

## Splay Trees

### When to Splay

### Python Implementation

Although the mathematical analysis of a splay tree’s performance is complex the implementation of splay trees is a
rather simple adaptation to a standard binary search tree.

It is important to note that our original TreeMap class makes calls to the rebalance access method, not just from within
the getitem method, but also during setitem when modifying the value associated with an existing key, and after any map
operations that result in a failed search.

### Amortized Analysis of Splaying

## (2,4) Trees

we consider a data structure known as a (2,4) tree. It is a particular example of a more general structure known as a
**multiway search tree**, in which internal nodes may have more than two children.

Recall that general trees are defined so that internal nodes may have many children. we discuss how general trees can be
used as multiway search trees. Map items stored in a search tree are pairs of the form (k,v),where k is the key and v is
the value associated with the key.

Let w be a node of an ordered tree. We say that w is a **d-node** if w has d children. We define a multiway search tree
to be an ordered tree T that has the following properties:

* Each internal node of T has at least two children. That is, each internal node is a d-node such that d ≥ 2.
* Each internal d-node w of T with children c1,... ,cd stores an ordered set of d−1 key-value pairs (k1,v1),..., (
  kd−1,vd−1), where k1 ≤ ··· ≤ kd−1.
* Let us conventionally define k0 = −∞ and kd =+∞. For each item (k,v) stored at a node in the subtree of w rooted at
  ci, i = 1,... ,d,we have that ki−1 ≤ k ≤ ki.

That is, if we think of the set of keys stored at w as including the special fictitious keys k0 = −∞ and kd =+∞,thena
key k stored in the subtree of T rooted at a child node ci must be “in between” two keys stored at w. This simple
viewpoint gives rise to the rule that a d-node stores d−1 regular keys, and it also forms the basis of the algorithm for
searching in a multiway search tree.

By the above definition, the external nodes of a multiway search do not store any data and serve only as “placeholders.”
These external nodes can be efficiently represented by None references, as has been our convention with binary search
trees. However, for the sake of exposition, we will discuss these as actual nodes that do not store anything. Based on
this definition, there is an interesting relationship between the number of key-value pairs and the number of external
nodes in a multiway search tree.

> **Proposition :** An n-item multiway search tree has n+1 external nodes.

Searching for an item with key k in a multiway search tree T is simple. We perform such a search by tracing a path in T
starting at the root. When we are at a d-node w during this search, we compare the key k with the keys k1,... ,kd−1
stored at w.If k = ki for some i, the search is successfully completed. Otherwise, we continue the search in the child
ci of w such that ki−1 < k < ki. If we reach an external node, then we know that there is no item with key k in T, and
the search terminates unsuccessfully.

### Data Structures for Representing Multiway Search Trees

Before we discuss a linked data structure for representing a general tree. This representation can also be used for a
multiway search tree. When using a general tree to implement a multiway search tree, we must store at each node one or
more key-value pairs associated with that node. That is, we need to store with w a reference to some collection that
stores the items for w.

During a search for key k in a multiway search tree, the primary operation needed when navigating a node is finding the
smallest key at that node that is greater than or equal to k. For this reason, it is natural to model the information at
a node itself as a sorted map, allowing use of the find ge(k) method. We say such a map serves as a **secondary** data
structure to support the **primary** data structure represented by the entire multiway search tree. This reasoning may
at first seem like a circular argument, since we need a representation of a (secondary) ordered map to represent a (
primary) ordered map. We can avoid any circular dependence, however, by using the **bootstrapping technique**, where we
use a simple solution to a problem to create a new, more advanced solution

In the context of a multiway search tree, a natural choice for the secondary structure at each node is the
SortedTableMap. Because we want to determine the associated value in case of a match for key k, and otherwise the
corresponding child ci such that ki−1 < k < ki, we recommend having each key ki in the secondary structure map to the
pair (vi,ci). With such a realization of a multiway search tree T, processing a d-node w while searching for an item of
T with key k can be performed using a binary search operation in O(logd) time.

> Let dmax denote the maximum number of children of any node ofT,and let h denote the height of T. The search time in a
> multiway search tree is therefore `O(h log(dmax))`. If dmax is a constant, the running time for performing a search is
> `O(h)`.

The primary efficiency goal for a multiway search tree is to keep the height as small as possible. We next discuss a
strategy that caps dmax at 4 while guaranteeing a height h that is logarithmic in n, the total number of items stored in
the map.

### (2,4)-Tree Operations

Amultiway search tree that keeps the secondary data structures stored at each node small and also keeps the primary
multiway tree balanced is the (2,4) tree,which is sometimes called a 2-4 tree or 2-3-4 tree. This data structure
achieves these goals by maintaining two simple properties

* **Size Property:** Every internal node has at most four children.
* **Depth Property:** All the external nodes have the same depth.

Again, we assume that external nodes are empty and, for the sake of simplicity, we describe our search and update
methods assuming that external nodes are real nodes, although this latter requirement is not strictly needed.

Enforcing the size property for (2,4) trees keeps the nodes in the multiway search tree simple. It also gives rise to
the alternative name “2-3-4 tree,” since it implies that each internal node in the tree has 2, 3, or 4 children. Another
implication of this rule is that we can represent the secondary map stored at each internal node using an unordered list
or an ordered array, and still achieve O(1)-time performance for all operations (since dmax = 4).

The depth property, on the other hand, enforces an important bound on the height of a (2,4) tree.

> **Proposition :** The height ofa (2,4) tree storing n items is O(logn).

Proposition states that the size and depth properties are sufficient for keeping a multiway tree balanced. Moreover,
this proposition implies that performing a search in a (2,4) tree takes O(logn) time and that the specific realization
of the secondary structures at the nodes is not a crucial design choice, since the maximum number of children dmax is a
constant.

Maintaining the size and depth properties requires some effort after performing insertions and deletions in a (2,4)
tree, however.

#### Insertion

To insert a new item (k,v), with key k,into a (2,4) tree T, we first perform a search for k. Assuming that T has no item
with key k, this search terminates unsuccessfully at an external node z.Let w be the parent of z. We insert the new item
into node w and add a new child y (an external node) to w on the left of z.

Our insertion method preserves the depth property, since we add a new external node at the same level as existing
external nodes. Nevertheless, it may violate the size property. Indeed, if a node w was previously a 4-node, then it
would become a 5-node after the insertion, which causes the tree T to no longer be a (2,4) tree. This type of violation
of the size property is called an **overflow** at node w,and it must be resolved in order to restore the properties of
a (
2,4) tree.

Let c1,... ,c5 be the children of w,and let k1,... ,k4 be the keys stored at w. To remedy the overflow at node w, we
perform a **split** operation on w as follows.

* Replace w with two nodes w' and w'',where
    * w' is a 3-node with children c1,c2,c3 storing keys k1 and k2
    * w'' is a 2-node with children c4,c5 storing key k4.
* If w is the root of T, create a new root node u; else, let u be the parent of w.
* Insert key k3 into u and make w' and w'' children of u,sothatif w was child i of u,then w' and w'' become children i
  and i+1 of u, respectively.

As a consequence of a split operation on node w, a new overflow may occur at the parent u of w. If such an overflow
occurs, it triggers in turn a split at node u. A split operation either eliminates the overflow or propagates it into
the parent of the current node.

Because dmax is at most 4, the original search for the placement of new key k uses O(1) time at each level, and
thus `O(logn)` time overall, since the height of the tree is O(logn)

The modifications to a single node to insert a new key and child can be implemented to run in O(1) time, as can a single
split operation. The number of cascading split operations is bounded by the height of the tree, and so that phase of the
insertion process also runs in `O(logn)` time. Therefore, the total time to perform an insertion in a (2,4) tree
is `O(logn)`.

#### Deletion

We begin such an operation by performing a search in T for an item with key k.Removing an item from a (2,4) tree can
always be reduced to the case where the item to be removed is stored at a node w whose children are external nodes.
Suppose, for instance, that the item with key k that we wish to remove is stored in the ith item (ki,vi) at a node z
that has only internal-node children. In this case, we swap the item (ki,vi) with an appropriate item that is stored at
a node w with external-node children as follows

1. We find the rightmost internal node w in the subtree rooted at the ith child of z, noting that the children of node w
   are all external nodes.
2. We swap the item (ki,vi) at z with the last item of w.

Once we ensure that the item to remove is stored at a node w with only externalnode children (because either it was
already at w or we swapped it into w), we simply remove the item from w and remove the ith external node of w.

Removing an item (and a child) from a node w as described above preserves the depth property, for we always remove an
external child from a node w with only external children. However, in removing such an external node, we may violate the
size property at w. Indeed, if w was previously a 2-node, then it becomes a 1-node with no items after the removal which
is not allowed in a (2,4) tree.

This type of violation of the size property is called an underflow at node w. To remedy an underflow, we check whether
an immediate sibling of w is a 3-node or a 4-node. If we find such a sibling s, then we perform a **transfer**
operation, in which we move a child of s to w,a key of s to the parent u of w and s, and a key of u to w.

If w has only one sibling, or if both immediate siblings of w are 2-nodes, then we perform a fusion operation, in which
we merge w with a sibling, creating a new node w', and move a key from the parent u of w to w' .

A fusion operation at node w may cause a new underflow to occur at the parent u of w, which in turn triggers a transfer
or fusion at u. Hence, the number of fusion operations is bounded by the height of the tree, which is O(logn) . If an
underflow propagates all the way up to the root, then the root is simply deleted.

### Performance of (2,4) Trees

The asymptotic performance of a (2,4) tree is identical to that of an AVL tree (see Table 11.2) in terms of the sorted
map ADT, with guaranteed logarithmic bounds for most operations. The time complexity analysis for a (2,4) tree having n
key-value pairs is based on the following:

* The height of a (2,4) tree storing n entries is O(logn), by Proposition
* A split, transfer, or fusion operation takes O(1) time.
* A search, insertion, or removal of an entry visits O(logn) nodes.

## Red-Black Trees

AVL trees may require many restructure operations (rotations) to be performed after a deletion, and (2,4) trees may
require many split or fusing operations to be performed after an insertion or removal. The data structure we discuss in
this section, the red-black tree, does not have these drawbacks; it uses O(1) structural changes after an update in
order to stay balanced.

Formally, a **red-black tree** is a binary search tree with nodes colored red and black in a way that satisfies the
following properties:

* **Root Property:** The root is black.
* **Red Property:** The children of a red node (if any) are black.
* **Depth Property:** All nodes with zero or one children have the same black depth, defined as the number of black
  ancestors. (Recall that a node is its own ancestor).

We can make the red-black tree definition more intuitive by noting an interesting correspondence between red-black trees
and (2,4) trees (excluding their trivial external nodes). Namely, given a red-black tree, we can construct a
corresponding (2,4) tree by merging every red node w into its parent, storing the entry from w at its parent, and with
the children of w becoming ordered children of the parent.

The depth property of the red-black tree corresponds to the depth property of the (2,4) tree since exactly one black
node of the red-black tree contributes to each node of the corresponding (2,4) tree.

Conversely, we can transform any (2,4) tree into a corresponding red-black tree by coloring each node w black and then
performing the following transformations:

* If w is a 2-node, then keep the (black) children of w as is.
* If w is a 3-node, then create a new red node y,give w’s last two (black) children to y, and make the first child of w
  and y be the two children of w.
* If w is a 4-node, then create two new red nodes y and z,give w’s first two (black) children to y,give w’s last two (
  black) children to z,and make y and z be the two children of w.

Notice that a red node always has a black parent in this construction.

> **Proposition :** The height of a red-black tree storing n entries is O(logn).

### Red-Black Tree Operations

The algorithm for searching in a red-black tree T is the same as that for a standard binary search tree. Thus, searching
in a red-black tree takes time proportional to the height of the tree, which is O(logn).

The correspondence between (2,4) trees and red-black trees provides important intuition that we will use in our
discussion of how to perform updates in red-black trees; in fact, the update algorithms for red-black trees can seem
mysteriously complex without this intuition. Split and fuse operations of a (2,4) tree will be effectively mimicked by
recoloring neighboring red-black tree nodes. A rotation within a red-black tree will be used to change orientations of a
3-node.

#### Insertion

Now consider the insertion of a key-value pair (k,v) into a red-black tree T. We search for k in T until we reach a null
subtree, and we introduce a new leaf x at that position, storing the item. In the special case that x is the only node
of T, and thus the root, we color it black. In all other cases, we color x red. This action corresponds to inserting (
k,v) into a node of the (2,4) tree T' with external children.

The insertion preserves the root and depth properties of T,but it may violate the red property. Indeed, if x is not the
root of T and the parent y of x is red, then we have a parent and a child (namely, y and x) that are both red. Note that
by the root property, y cannot be the root of T, and by the red property (which was previously satisfied), the parent z
of y must be black.

> Since x and its parent are red, but x’s grandparent z is black, we call this violation of the red property a double
> red at node x.

To remedy a double red, we consider two cases.

**Case 1: The Sibling s of y Is Black (or None).** In this case, the double red denotes the fact that we have added the
new node to a corresponding 3-node of the (2,4) tree T', effectively creating a malformed 4-node. This formation has one
red node (y) that is the parent of another red node (x), while we want it to have the two red nodes as siblings instead.
To fix this problem, we perform a trinode restructuring of T.

After performing the restructure(x) operation, we color b black and we color a and c red. Thus, the restructuring
eliminates the double-red problem. Notice that the portion of any path through the restructured part of the tree is
incident to exactly one black node, both before and after the trinode restructuring. Therefore, the black depth of the
tree is unaffected.

**Case 2: The Sibling s of y Is Red.** In this case, the double red denotes an overflow in the corresponding (2,4) tree
T'. To fix the problem, we perform the equivalent of a split operation. Namely, we do a **recoloring**: *we color y and
s black and their parent z red (unless z is the root, in which case, it remains black).* Notice that unless z is the
root, the portion of any path through the affected part of the tree is incident to exactly one black node, both before
and after the recoloring. Therefore, the black depth of the tree is unaffected by the recoloring unless z is the root,
in which case it is increased by one.

However, it is possible that the double-red problem reappears after such a recoloring, albeit higher up in the tree
T,since z may have a red parent. If the double-red problem reappears at z, then we repeat the consideration of the two
cases at z. Thus, a recoloring either eliminates the double-red problem at node x, or propagates it to the grandparent z
of x. We continue going up T performing recolorings until we finally resolve the double-red problem (with either a final
recoloring or a trinode restructuring). Thus, the number of recolorings caused by an insertion is no more than half the
height of tree T,thatis, O(logn)

#### Deletion

Deleting an item with key k from a red-black tree T initially proceeds as for a binary search tree. Structurally, the
process results in the removal a node that has at most one child (either that originally containing key k or its inorder
predecessor) and the promotion of its remaining child (if any).

If the removed node was red, this structural change does not affect the black depths of any paths in the tree, nor
introduce any red violations, and so the resulting tree remains a valid red-black tree. In the corresponding (2,4) tree
T', this case denotes the shrinking of a 3-node or 4-node.

If the removed node was black, then it either had zero children or it had one child that was a red leaf (because the
null subtree of the removed node has black height 0). In the latter case, the removed node represents the black part of
a corresponding 3-node, and we restore the redblack properties by recoloring the promoted child to black.

The more complex case is when a (nonroot) black leaf is removed. In the corresponding (2,4) tree, this denotes the
removal of an item from a 2-node. Without rebalancing, such a change results in a deficit of one for the black depth
along the path leading to the deleted item. By necessity, the removed node must have a sibling whose subtree has black
height 1 (given that this was a valid red-black tree prior to the deletion of the black leaf).

We consider three possible cases to remedy a deficit.

(....)

### Performance of Red-Black Trees

The asymptotic performance of a red-black tree is identical to that of an AVL tree or a (2,4) tree in terms of the
sorted map ADT, with guaranteed logarithmic time bounds for most operations. The primary advantage of a red-black tree
is that an insertion or deletion requires only a **constant number of restructuring operations**.

(This is in contrast to AVL trees and (2,4) trees, both of which require a logarithmic number of structural changes per
map operation in the worst case.) That is, an insertion or deletion in a red-black tree requires logarithmic time for a
search, and may require a logarithmic number of recoloring operations that cascade upward. Yet we show, in the following
propositions, that there are a constant number of rotations or restructure operations for a single map operation.

> **Proposition :** The insertion of an item in a red-black tree storing n items can be done in O(logn) time and requires
> O(logn) recolorings and at most one trinode restructuring.

Recall that an insertion begins with a downward search, the creation of a new leaf node, and then a potential upward
effort to remedy a double-red violation. There may be logarithmically many recoloring operations due to an upward
cascading of Case 2 applications, but a single application of the Case 1 action eliminates the double-red problem with a
trinode restructuring. Therefore, at most one restructuring operation is needed for a red-black tree insertion.

> **Proposition :** Thealgorithm for deleting anitem fromared-black treewith n items takes O(logn) time and performs O(
> logn) recolorings and at most two restructuring operations.

A deletion begins with the standard binary search tree deletion algorithm, which requires time proportional to the
height of the tree; for red-black trees, that height is O(logn). The subsequent rebalancing takes place along an upward
path from the parent of a deleted node.

1. We considered three cases to remedy a resulting black deficit. Case 1 requires a trinode restructuring operation, yet
   completes the process, so this case is applied at most once.
2. Case 2 may be applied logarithmically many times, but it only involves a recoloring of up to two nodes per
   application
3. Case 3 requires a rotation, but this case can only apply once, because if the rotation does not resolve the problem,
   the very next action will be a terminal application of either Case 1 or Case 2.

In the worst case, there will be O(logn) recolorings from Case 2, a single rotation from Case 3, and a trinode
restructuring from Case 1.

### Python Implementation

It inherits from the standard TreeMap class and relies on the balancing framework. We begin by overriding the definition
of the nested Node class to introduce an additional Boolean field to denote the current color of a node. Our constructor
intentionally sets the color of a new node to red to be consistent with our approach for inserting items. We define
several additional utility functions, that aid in setting the color of nodes and querying various conditions.

When an element has been inserted as a leaf in the tree, the rebalance insert hook is called, allowing us the
opportunity to modify the tree. The new node is red by default, so we need only look for the special case of the new
node being the root (in which case it should be colored black), or the possibility that we have a double-red violation
because the new node’s parent is also red.

An additional challenge is that by the time the rebalance hook is called, the old node has already been removed from the
tree. That hook is invoked on the parent of the removed node. Some of the case analysis depends on knowing about the
properties of the removed node. Fortunately, we can reverse engineer that information by relying on the red-black tree
properties. In particular, if p denotes the parent of the removed node, it must be that:

* If p has no children, the removed node was a red leaf.
* If p has one child, the removed node was a black leaf, causing a deficit, unless that one remaining child is a red
  leaf.
* If p has two children, the removed node was a black node with one red child, which was promoted

