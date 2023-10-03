# TREES

A tree is an abstract data type that stores elements **hierarchically**. Except the top element, each element in a tree
has a **parent** element and zero or more **children** elements.

Formally, we define a tree T as a set of **nodes** storing elements such that the nodes have a **parent-child**
relationship that satisfies the following properties:

* If T is nonempty, it has a special node, called the root ofT, that has no parent.
* Each node v of T different from the root has a unique parent node w;every node with parent w is a child of w.

Note that according to our definition, a tree can be empty, meaning that it does not have any nodes. This convention
also allows us to define a tree recursively such that a tree T is either empty or consists of a node r, called the root
of T,and a (possibly empty) set of subtrees whose roots are the children of r.

Two nodes that are children of the same parent are **siblings**. A node v is external if v has no children. A node v is
internal if it has one or more children. External nodes are also known as **leaves**.

The **subtree of T rooted at a node v** is the tree consisting of all the descendants of v in T (including v itself).

An **edge** of tree T is a pair of nodes (u,v) such that u is the parent of v,or vice versa. A **path** of T is a
sequence of nodes such that any two consecutive nodes in the sequence form an edge.

A tree is **ordered** if there is a meaningful linear order among the children of each node; that is, we purposefully
identify the children of a node as being the first, second, third, and so on.

### The Tree Abstract Data Type

we define a tree ADT using the concept of a **position** as an abstraction for a node of a tree. An element is stored at
each position, and positions satisfy parent-child relationships that define the tree structure. A position object for a
tree supports the method:

    p.element(): Return the element stored at position p.

The tree ADT then supports the following accessor methods

    T.root(): Return the position of the root of tree T, or None if T is empty
    T.is root(p): Return True if position p is the root of Tree T.
    T.parent(p): Return the position of the parent of position p, or None if p is the root of T.
    T.num children(p): Return the number of children of position p. 
    T.children(p): Generate an iteration of the children of position p. 
    T.is leaf(p): Return True if position p does not have any children.
    len(T): Return the number of positions (and hence elements) that are contained in tree T.
    T.is empty(): Return True if tree T does not contain any positions. 
    T.positions(): Generate an iteration of all positions of tree T.
    iter(T): Generate an iteration of all elements stored within tree T.

Any of the above methods that accepts a position as an argument should generate a ValueError if that position is invalid
for T.

#### Computing Depth and Height

Let p be the position of a node of a tree T.The **depth** of p is the number of ancestors of p, excluding p itself. Note
that this definition implies that the depth of the root of T is 0. The depth of p can also be recursively defined as
follows:

* If p is the root, then the depth of p is 0.
* Otherwise, the depth of p is one plus the depth of the parent of p.

The running time of ``T.depth(p)`` for position p is `O(dp +1)`,where `dp` denotes the depth of p in the tree T, because
the algorithm performs a constant-time recursive step for each ancestor of p. Thus, algorithm `T.depth(p)` runs in **O(
n)**
worstcase time, where n is the total number of positions of T, because a position of T may have depth n−1 if all nodes
form a single branch.

The **height** of a position p in a tree T is also defined recursively:

* If p is a leaf, then the height of p is 0.
* Otherwise, the height of p is one more than the maximum of the heights of p’s children.

The height of a nonempty tree T is the height of the root of T. In addition, height can also be viewed as follows.

    Proposition: The height of a nonempty tree T is equal to the maximum of the depths ofits leafpositions.

## Binary Trees

A binary tree is an ordered tree with the following properties:

1. Every node has at most two children.
2. Each child node is labeled as being either a left child or a right child.
3. A left child precedes a right child in the order of children of a node.

The subtree rooted at a left or right child of an internal node v is called a **left subtree** or **right subtree**,
respectively, of v. A binary tree is **proper** if each node has either zero or two children. Some people also refer to
such trees as being full binary trees. Thus, in a proper binary tree, every internal node has exactly two children. A
binary tree that is not proper is **improper**.

Examples are decision trees and arithmetic expression trees.

Incidentally, we can also define a binary tree in a recursive way such that a binary tree is either empty or consists
of:

* A node r, called the root of T, that stores an element
* A binary tree (possibly empty), called the left subtree ofT
* A binary tree (possibly empty), called the right subtree of T

### The Binary Tree Abstract Data Type

A binary tree is a specialization of a tree that supports three additional accessor methods:

* T.left(p): Return the position that represents the left child of p, or None if p has no left child.
* T.right(p): Return the position that represents the right child of p, or None if p has no right child.
* T.sibling(p): Return the position that represents the sibling of p, or None if p has no sibling.

### Properties of Binary Trees

We denote the set of all nodes of a tree T at the same depth d as **level d** of T. In a binary tree, level 0 has at
most one node (the root), level 1 has at most two nodes (the children of the root), level 2 has at most four nodes, and
so on In general, level d has at most 2d nodes.

We can see that the maximum number of nodes on the levels of a binary tree grows exponentially as we go down the tree.
From this simple observation, we can derive the following properties relating the height of a binary tree T with its
number of nodes.

********************

Also, the following relationship exists between the number of internal nodes and external nodes in a proper binary tree.

    Proposition: In a nonempty proper binary tree T, with n_E external nodes and n_I internal nodes, we have 
    n_E = n_I +1.

Remember the graphical justification for the last proposition.

Note that the above relationship does not hold, in general, for improper binary trees and non-binary trees, although
there are other interesting relationships that do hold.

## Implementing Trees

There are several choices for the internal representation of trees. We describe the most common representations in this
section. We begin with the case of a binary tree, since its shape is more narrowly defined.

### Linked Structure for Binary Trees

use a **linked structure**, with a node that maintains references to the element stored at a position p and to the nodes
associated with the children and parent of p. If p is the root of T, then the parent field of p is None. Likewise, if p
does not have a left child (respectively, right child), the associated field is None. The tree itself maintains an
instance variable storing a reference to the root node (if any), and a variable, called size, that represents the
overall number of nodes of T.

For linked binary trees, a reasonable set of update methods to support for general usage are the following:

    T.add root(e): Create a root for an empty tree, storing e as the element, and return the position of that root; an error 
    occurs if the tree is not empty.

    T.add left(p, e): Create a new node storing element e, link the node as the left child of position p, and return 
    the resulting position; an error occurs if p already has a left child.

    T.add right(p, e): Create a new node storing element e, link the node as the right child of position p, and return 
    the resulting position; an error occurs if p already has a right child    

    T.replace(p, e): Replace the element stored at position p with element e, and return the previously stored element.
    
    T.delete(p): Remove the node at position p, replacing it with its child, if any, and return the element that had 
    been stored at p; an error occurs if p has two children.

    T.attach(p, T1, T2): Attach the internal structure of trees T1 and T2, respectively, as the left and right subtrees 
    of leaf position p of T, and reset T1 and T2 to empty trees; an error condition occurs if p is not a leaf.

We have specifically chosen this collection of operations because each can be implemented in O(1) worst-case time with
our linked representation. The most complex of these are delete and attach, due to the case analyses involving the
various parent-child relationships and boundary conditions, yet there remains only a constant number of operations to
perform.

To avoid the problem of undesirable update methods being inherited by subclasses of LinkedBinaryTree, we have chosen an
implementation in which none of the above methods are publicly supported. In particular applications, subclasses of
LinkedBinaryTree can invoke the nonpublic methods internally, while preserving a public interface that is appropriate
for the application. A subclass may also choose to wrap one or more of the nonpublic update methods with a public method
to expose it to the user.

#### Performance of the Linked Binary Tree Implementation

To summarize the efficiencies of the linked structure representation, we analyze the running times of the
LinkedBinaryTree methods

* The len method, implemented in LinkedBinaryTree, uses an instance variable storing the number of nodes of T and takes
  O(1) time. Method is empty, inherited from Tree, relies on a single call to len and thus takes O(1) time.
* The accessor methods root, left, right, parent,and num children are implemented directly in LinkedBinaryTree and take
  O(1) time. The sibling and children methods are derived in BinaryTree based on a constant number of calls to these
  other accessors, so they run in O(1) time as well.
* The is root and is leaf methods, from the Tree class, both run in O(1) time, as is root calls root and then relies on
  equivalence testing of positions, while is leaf calls left and right and verifies that None is returned by both.
* The depth method at position p runs in O(dp +1) time where dp is its depth; the height method on the root of the tree
  runs in O(n) time.

### Array-Based Representation of a Binary Tree

This representation of a Binary Tree T is based on a way of numbering the positions of T. For every position p of T,let
**f(p)** be the integer defined as follows.

* If p is the root of T,then **f(p)= 0**.
* If p is the left child of position q,then **f(p)= 2 f(q)+1**.
* If p is the right child of position q,then **f(p)= 2 f(q)+2**.

The numbering function f is known as a **level numbering** of the positions in a binary tree T, for it numbers the
positions on each level of T in increasing order from left to right. Note well that the level numbering is based on
potential positions within the tree, not actual positions of a given tree, so they are not necessarily consecutive.

The level numbering function f suggests a representation of a binary tree T by means of an array-based structure A, with
the element at position p of T stored at index f(p) of the array.

One advantage of an array-based representation of a binary tree is that a position p can be represented by the single
integer f(p), and that position-based methods such as root, parent, left,and right can be implemented using simple
arithmetic operations on the number f(p).

The space usage of an array-based representation depends greatly on the shape of the tree. Let n be the number of nodes
of T,and let `f_M` be the maximum value of `f(p)` over all the nodes of T. The array A requires length `N = 1 + fM`,
since elements range from `A[0]` to `A[ fM]`. Note that A may have a number of empty cells that do not refer to existing
nodes of T. In fact, in the worst case, `N = 2^n − 1`.

Thus, in spite of the worst-case space usage, there are applications for which the array representation of a binary tree
is space efficient. Still, for general binary trees, the exponential worst-case space requirement of this representation
is prohibitive.

Another drawback of an array representation is that some update operations for trees cannot be efficiently supported.
For example, deleting a node and promoting its child takes O(n) time because it is not just the child that moves
locations within the array, but all descendants of that child.

### Linked Structure for General Trees

For a general tree, there is no a priori limit on the number of children that a node may have. A natural way to realize
a general tree T as a linked structure is to have each node store a single container of references to its children. For
example, a children field of a node can be a Python list of references to the children of the node (if any). we note
that, by using a collection to store the children of each position p, we can implement children(p) by simply iterating
that collection.

Operation | Running Time len, is empty O(1)
root, parent, O(1)
is root, is leaf  
children(p)               O(cp +1)
depth(p)                  O(dp +1)
height O(n)

## Tree Traversal Algorithms

A **traversal** of a tree T is a systematic way of accessing, or “visiting,” all the positions of T. The specific action
associated with the “visit” of a position p depends on the application of this traversal, and could involve anything
from incrementing a counter to performing some complex computation for p.

### Preorder and Postorder Traversals of General Trees

In a **preorder traversal** of a tree T, the root of T is visited first and then the subtrees rooted at its children are
traversed recursively. If the tree is ordered, then the subtrees are traversed according to the order of the children.
The pseudo-code for the preorder traversal of the subtree rooted at a position p is shown.

    preorder(T, p): 
      perform the “visit” action for position p 
      for each child c in T.children(p) do 
        preorder(T, c)

The **postorder traversal** can be viewed as the opposite of the preorder traversal, because it recursively traverses
the subtrees rooted at the children of the root first, and then visits the root (hence, the name). Pseudo-code for the
postorder traversal is shown next

    postorder(T, p): 
      for each child c in T.children(p) do 
        postorder(T, c)                           {recursively traverse the subtree rooted at c}
      perform the “visit” action for position p

Both preorder and postorder traversal algorithms are efficient ways to access all the positions of a tree. At each
position p, the non-recursive part of the traversal algorithm requires time O(cp+1), where cp is the number of children
of p, under the assumption that the “visit” itself takes O(1) time. the overall running time for the traversal of tree T
is O(n),where n is the number of positions in the tree. This running time is asymptotically optimal since the traversal
must visit all the n positions of the tree.

### Breadth-First Tree Traversal

another common approach is to traverse a tree so that we visit all the positions at depth d before we visit the
positions at depth d+1. Such an algorithm is known as a **breadth-first traversal**. The process is not recursive, since
we are not traversing entire subtrees at once. We use a queue to produce a FIFO (i.e., first-in first-out) semantics for
the order in which we visit nodes. The overall running time is O(n), due to the n calls to enqueue and n calls to
dequeue.

    Algorithm breadthfirst(T): 
      Initialize queue Q to contain T.root() 
      while Q not empty do 
        p = Q.dequeue()
        perform the “visit” action for position p 
        for each child c in T.children(p) do 
          Q.enqueue(c)

### Inorder Traversal of a Binary Tree

The standard preorder, postorder, and breadth-first traversals that were introduced for general trees, can be directly
applied to binary trees. Now, we introduce another common traversal algorithm specifically for a binary tree.

During an **inorder traversal**, we visit a position between the recursive traversals of its left and right subtrees.
The inorder traversal of a binary tree T can be informally viewed as visiting the nodes of T “from left to right.”
Indeed, for every position p, the inorder traversal visits p after all the positions in the left subtree of p and before
all the positions in the right subtree of p. Pseudo-code for the inorder traversal algorithm is

    Algorithm inorder(p): 
      if p has a left child lc then 
          inorder(lc)                                  {recursively traverse the left subtree of p}
    perform the “visit” action for position p 
    if p has a right child rc then 
      inorder(rc)                                      {recursively traverse the right subtree of p}

#### Binary Search Trees

An important application of the inorder traversal algorithm arises when we store an ordered sequence of elements in a
binary tree, defining a structure we call a **binary search tree**. Let S be a set whose unique elements have an order
relation. A binary search tree for S is a binary tree T such that, for each position p of T:

* Position p stores an element of S, denoted as e(p).
* Elements stored in the left subtree of p (if any) are less than e(p).
* Elements stored in the right subtree of p (if any) are greater than e(p)

The above properties assure that an inorder traversal of a binary search tree T visits the elements in nondecreasing
order.

We can use a binary search tree T for set S to find whether a given search value v is in S. At each internal position p
encountered, we compare our search value v with the element e(p) stored at p.If v < e(p), then the search continues in
the left subtree of p. If v = e(p), then the search terminates successfully. If v > e(p), then the search continues in
the right subtree of p. Finally, if we reach an empty subtree, the search terminates unsuccessfully.

In other words, a binary search tree can be viewed as a binary decision tree, where the question asked at each internal
node is whether the element at that node is less than, equal to, or larger than the element being searched for

## Implementing Tree Traversals in Python

we note that it is easy to produce an iteration of all elements of a tree, if we rely on a presumed iteration of all
positions. Therefore, support for the iter(T) syntax can be formally provided by a concrete implementation of the
special method iter within the abstract base class Tree.

To implement the positions method, we have a choice of tree traversal algorithms. Given that there are advantages to
each of those traversal orders, we will provide independent implementations of each strategy that can be called directly
by a user of our class. We can then trivially adapt one of those as a default order for the positions method of the tree
ADT.

The _subtree_preorder method is the recursive one. However, because we are relying on generators rather than traditional
functions, the recursion has a slightly different form. In order to yield all positions within the subtree of child c,
we loop over the positions yielded by the recursive call self. subtree preorder(c),and reyield each position in the
outer context. Note that if p is a leaf, the for loop over self.children(p) is trivial (this is the base case for our
recursion).

We rely on a similar technique in the public preorder method to re-yield all positions that are generated by the
recursive process starting at the root of the tree.

For many applications of binary trees, an inorder traversal provides a natural iteration. We could make it the default
for the BinaryTree class by overriding the positions method that was inherited from the Tree class

## Applications of Tree Traversals

