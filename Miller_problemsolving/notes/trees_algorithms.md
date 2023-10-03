## TREES AND TREE ALGORITHMS

> A tree data structure has a root, branches, and leaves.

The difference between a tree in nature and a tree in computer science is that a tree data structure has its
root at the top and its leaves on the bottom

Notice that you can start at the top of the tree and follow a path made of circles and arrows
all the way to the bottom. At each level of the tree we might ask ourselves a question and
then follow the path that agrees with our answer.

> A second property of trees is that all of the children of one node are independent of the children
of another node

> A third property is that each leaf node is unique.

One example of a tree structure that you probably use every day is a file system. In a file
system, directories, or folders, are structured as a tree. You can follow
a path from the root to any directory. That path will uniquely identify that subdirectory (and
all the files in it).

Another important property of trees, derived from their hierarchical nature,
is that you can move entire sections of a tree (called a **subtree**) to a different position in the
tree without affecting the lower levels of the hierarchy

A final example of a tree is a web page. The HTML source code and the tree accompanying the source illustrate another
hierarchy. Notice that each level of the tree corresponds to a level of nesting inside the HTML tags.

### Vocabulary and Definitions

**Node :**  It can have a name, which we call the **key**. A node may also have additional information. We call this
additional information the **payload**. *While the payload information is not central to many tree algorithms, it is
often critical in applications that make use of trees*

**Edge :** An edge connects two nodes to show
that there is a relationship between them. Every node (except the root) is connected by
exactly one incoming edge from another node. Each node may have several outgoing
edges.

**Path :** A path is an ordered list of nodes that are connected by edges. For example, Mammal →
Carnivora → Felidae → Felis → Domestica is a path.

**Children :** The set of nodes c that have incoming edges from the same node to are said to be the
children of that node.

**Parent :** A node is the parent of all the nodes it connects to with outgoing edges.

**Sibling :** Nodes in the tree that are children of the same parent are said to be siblings.

**Subtree :** A subtree is a set of nodes and edges comprised of a parent and all the descendants of
that parent.

**Leaf Node :** A leaf node is a node that has no children.

**Level :** The level of a node 𝑛 is the number of edges on the path from the root node to 𝑛. By definition,
the level of the root node is zero

**Height :** The height of a tree is equal to the maximum level of any node in the tree.

With the basic vocabulary now defined, we can move on to a formal definition of a tree. In fact,
we will provide two definitions of a tree. One definition involves nodes and edges. The second
definition, which will prove to be very useful, is a recursive definition.

###### Definition One

A tree consists of a set of nodes and a set of edges that connect pairs of nodes. A tree has the following properties:

• One node of the tree is designated as the root node.

• Every node 𝑛, except the root node, is connected by an edge from exactly one other node 𝑝, where 𝑝 is the parent of 𝑛.

• A unique path traverses from the root to each node.

• If each node in the tree has a maximum of two children, we say that the tree is a **binary tree**


######  Definition Two

A tree is either empty or consists of a root and zero or more subtrees, each of
which is also a tree. The root of each subtree is connected to the root of the parent tree by an edge

### Implementation

Keeping in mind the definitions from the previous section, we can use the following functions to create and manipulate
a binary tree:

• BinaryTree() creates a new instance of a binary tree.

• get_left_child() returns the binary tree corresponding to the left child of the current
node.

• get_right_child() returns the binary tree corresponding to the right child of the
current node.

• set_root_val(val) stores the object in parameter val in the current node.

• get_root_val() returns the object stored in the current node.

• insert_left(val) creates a new binary tree and installs it as the left child of the
current node.

• insert_right(val) creates a new binary tree and installs it as the right child of the
current node.

The key decision in implementing a tree is choosing a good internal storage technique. Python
allows us two very interesting possibilities, so we will examine both before choosing one.
The first technique we will call “list of lists,” the second technique we will call “nodes and
references.”

#####  List of Lists Representation

#### Nodes and References

In this case we will define a class that has attributes for the root value, as well as the left and right subtrees.
Since this representation  more closely follows the object-oriented programming paradigm, we will continue
to use this representation for the remainder of the chapter.

We will start out with a simple class definition for the nodes and references approach as shown
below. The important thing to remember about this representation is that the attributes left
and right will become references to other instances of the **BinaryTree** class.

    class BinaryTree:
        def __init__(self, root):
            self.key = root
            self.left_child = None
            self.right_child = None

Notice that the constructor function expects to get some kind of object to store in the root. Just
like you can store any object you like in a list, the root object of a tree can be a reference to
any object. we will store the name of the node as the root value

Next let’s look at the functions we need to build the tree beyond the root node. To add a left
child to the tree, we will create a new binary tree object and set the left attribute of the root to
refer to this new object

We must consider two cases for insertion. The first case is characterized by a node with no
existing left child. When there is no left child, simply add a node to the tree. The second case
is characterized by a node with an existing left child. In the second case, we insert a node and
push the existing child down one level in the tree

The code for insert_right must consider a symmetric set of cases. There will either be
no right child, or we must insert the node between the root and an existing right child.

To round out the definition for a simple binary tree data structure, we will write accessor
methods for the left and right children, as well as the root values.

### Parse Tree

With the implementation of our tree data structure complete, we now look at an example of how a tree can be used
to solve some real problems.

> Parse trees can be used to represent real-world constructions like sentences or
mathematical expressions

In particular we will look at:

* How to build a parse tree from a fully parenthesized mathematical expression.

* How to evaluate the expression stored in a parse tree.

* How to recover the original mathematical expression from a parse tree.

The first step in building a parse tree is to break up the expression string into a list of tokens. There are four
different kinds of tokens to consider: left parentheses, right parentheses, operators, and operands.

We know that whenever we read a left parenthesis we are starting a new expression, and hence we should create a new
tree to correspond to that expression. Conversely, whenever we read a right parenthesis, we have finished an expression.
We also know that operands are going to be leaf nodes and children of their operators. Finally, we know that every
operator is going to have both a left and a right child.

Using the information from above we can define four rules as follows:

1. If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.

2. If the current token is in the list ['+','-','/','*'], set the root value of the current node to the
operator represented by the current token. Add a new node as the right child of the current node and descend
to the right child.

3. If the current token is a number, set the root value of the current node to the number and return to the parent.

4. If the current token is a ')', go to the parent of the current node.

we need to keep track of the current node as well as the parent of the current node. The tree interface provides us
with a way to get children of a node, through the getLeftChild and getRightChild methods, but how can we keep track
of the parent? A simple solution to keeping track of parents as we traverse the tree is to use a stack. Whenever we
want to descend to a child of the current node, we first push the current node on the stack. When we want to return
to the parent of the current node, we pop the parent off the stack.

Using the rules described above, along with the Stack and BinaryTree operations, we are now ready to write a Python
function to create a parse tree.

(.....)

Now that we have built a parse tree, what can we do with it? As a first example, we will write a function to evaluate
the parse tree, returning the numerical result. To write this function, we will make use of the hierarchical
nature of the tree.

we can replace the original tree with the simplified tree representing the result of the operation.
This suggests that we can write an algorithm that evaluates a parse tree by recursively evaluating each subtree.

As we have done with past recursive algorithms, we will begin the design for the recursive evaluation function by
identifying the base case. A natural base case for recursive algorithms that operate on trees is to check for a leaf
node. In a parse tree, the leaf nodes will always be operands. Since numerical objects like integers and floating
points require no further interpretation, the evaluate function can simply return the value stored in the leaf node.

The recursive step that moves the function toward the base case is to call evaluate on both the left and the right
children of the current node. The recursive call effectively moves us down the tree, toward a leaf node.

To put the results of the two recursive calls together, we can simply apply the operator stored in the parent node to
the results returned from evaluating both children

### Tree Traversals

Now that we have examined the basic functionality of our tree data structure, it is time to look at some additional
usage patterns for trees.  There are three commonly used patterns to visit all the nodes in a tree. The difference
between these patterns is the order in which each node is visited. We call this visitation of the nodes a **traversal**.



* **Preorder :** In a preorder traversal, we visit the root node first, then recursively do a preorder traversal of the left
subtree, followed by a recursive preorder traversal of the right subtree.

The code for writing tree traversals is surprisingly elegant, largely because the traversals are written recursively.

You may wonder, what is the best way to write an algorithm like preorder traversal? Should it be a function that simply
uses a tree as a data structure, or should it be a method of the tree data structure itself?

Which of these two ways to implement preorder is best? The answer is that implementing preorder as an external
function is probably better in this case. The reason is that you very rarely want to just traverse the tree.
In most cases you are going to want to accomplish something else while using one of the basic traversal patterns.
In fact, we will see in the next example that the postorder traversal pattern follows very closely with the code
we wrote earlier to evaluate a parse tree. Therefore we will write the rest of the traversals as external functions.

We have already seen a common use for the postorder traversal, namely evaluating a parse tree. Look back at our
evaluate function above. What we are doing is evaluating the left subtree, evaluating the right subtree, and combining
them in the root through the function call to an operator. Assume that our binary tree is going to store only
expression tree data. Let’s rewrite the evaluation function, but model it even more closely on the postorder code.


### Priority Queues with Binary Heaps

One important variation of a queue is called a **priority queue**. A priority queue acts like a queue in
that you dequeue an item by removing it from the front. However, *in a priority queue the logical
order of items inside a queue is determined by their **priority***.

The highest priority items are at the front of the queue and the lowest priority items are at the back.
Thus when you enqueue an item on a priority queue, the new item may move all the way to the front.
We will see that the priority queue is a useful data structure for some of the graph algorithms we will study in the
next chapter

The classic way to implement a priority queue is using a data structure called a
**binary heap**. A binary heap will allow us both enqueue and dequeue items in 𝑂(log 𝑛).

The binary heap is interesting to study because when we diagram the heap it looks a lot like
a tree, but when we implement it we use only a single list as an internal representation. The
binary heap has two common variations: the **min heap**, in which the smallest key is always at
the front, and the **max heap**, in which the largest key value is always at the front. In this section
we will implement the min heap

##### Binary Heap Operations

The basic operations we will implement for our binary heap are as follows:

• BinaryHeap() creates a new, empty, binary heap.

• insert(k) adds a new item to the heap.

• find_min() returns the item with the minimum key value, leaving item in the heap.

• del_min() returns the item with the minimum key value, removing the item from the heap.

• is_empty() returns true if the heap is empty, false otherwise.

• size() returns the number of items in the heap.

• build_heap(list) builds a new heap from a list of keys.


##### Binary Heap Implementation

###### The Structure Property

we will take advantage of the logarithmic nature of the binary tree to represent our heap. In order to guarantee
logarithmic performance, we must keep our tree balanced. A balanced binary tree has roughly the same number
of nodes in the left and right subtrees of the root. In our heap implementation we keep the tree balanced by
creating a complete binary tree

> A **complete binary tree** is a tree in which each level has all
of its nodes. The exception to this is the bottom level of the tree, which we fill in from left to
right

Another interesting property of a complete tree is that *we can represent it using a single list*. We
do not need to use nodes and references or even lists of lists. Because the tree is complete, the
left child of a parent (at position 𝑝) is the node that is found in position 2𝑝 in the list. Similarly,
the right child of the parent is at position 2𝑝 + 1 in the list. To find the parent of any node in
the tree, we can simply use Python’s integer division. Given that a node is at position 𝑛 in the
list, the parent is at position 𝑛/2.

The list representation of the tree, along with the full structure property, allows us to efficiently
traverse a complete binary tree using only a few simple mathematical operations. We will see
that this also leads to an efficient implementation of our binary heap.

###### The Heap Order Property

The method that we will use to store items in a heap relies on maintaining the **heap order
property**. The heap order property is as follows:

> In a heap, for every node 𝑥 with parent 𝑝, the key in 𝑝 is smaller than or equal to the key in x

###### Heap Operations


**Insert method**. The easiest, and most efficient, way to add an item to a list is to simply append the item to the end
of the list. The bad news about appending is that we will very likely violate the heap structure property. However, it is
possible to write a method that will allow us to regain the heap structure property by comparing
the newly added item with its parent. *If the newly added item is less than its parent, then we
can swap the item with its parent*.

Notice that when we percolate an item up, we are restoring the heap property between the
newly added item and the parent. We are also preserving the heap property for any siblings.
Of course, if the newly added item is very small, we may still need to swap it up another level.
In fact, we may need to keep swapping until we get to the top of the tree.

**Del min**. Since the heap property requires that the root of the tree be the smallest item in the tree, finding the
minimum item is easy. The hard part of del_min is restoring full compliance with the heap
structure and heap order properties after the root has been removed.

We can restore our heap in two steps. First, we will restore the root item by *taking the last item in the list
and moving it to the root position*. Moving the last item maintains our heap structure property. However, we
have probably destroyed the heap order property of our binary heap. Second, *we will restore
the heap order property by pushing the new root node down the tree to its proper position*.

In order to maintain the heap order property, all we need to do is swap the root with its smallest
child less than the root. After the initial swap, we may repeat the swapping process with a node
and its children until the node is swapped into a position on the tree where it is already less
than both children.

To finish our discussion of binary heaps, we will look at a method to build an entire heap
from a list of keys.If we start with an entire list then we can build the whole heap in 𝑂(𝑛) operations.

Although we start out in the middle of the
tree and work our way back toward the root, the percolates_down method ensures that the largest
child is always moved down the tree. Because the heap is a complete binary tree, any nodes
past the halfway point will be leaves and therefore have no children. Notice that when 𝑖 = 1,
we are percolating down from the root of the tree, so this may require multiple swaps

> percolates_down ensures that we check the next set
of children farther down in the tree to ensure that it is pushed as low as it can go.

The key to understanding that you can build the
heap in 𝑂(𝑛) is to remember that the log 𝑛 factor is derived from the height of the tree. For
most of the work in build_heap, the tree is shorter than log 𝑛.

> Using the fact that you can build a heap from a list in 𝑂(𝑛) time, you will construct a sorting
algorithm that uses a heap and sorts a list in 𝑂(𝑛 log 𝑛)

### Binary Search Trees

In this section we will study binary search trees as yet another way to map from a key to a value.
In this case we are not interested in the exact placement of items in the tree, but we are interested in using the
binary tree structure to provide for efficient searching.

##### Search Tree Operations

Before we look at the implementation, let’s review the interface provided by the map ADT.

• Map() Create a new, empty map.

• put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with
the new value.

• get(key) Given a key, return the value stored in the map or None otherwise. • del Delete the key-value pair from
the map using a statement of the form del map[key].

• len() Return the number of key-value pairs stored in the map. • in Return True for a statement of the form key
in map, if the given key is in the map.

##### Search Tree Implementation

> A binary search tree relies on the property that keys that are less than the parent are found in the left subtree,
and keys that are greater than the parent are found in the right subtree. We will call this the **bst property**

the bst property will guide our implementation.

