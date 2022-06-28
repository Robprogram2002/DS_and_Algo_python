# Graph Algorithms

A graph is a way of representing relationships that exist between pairs of objects. That is, a graph is a set of
objects, called vertices, together with a collection of pairwise connections between them, called edges. Graphs have
applications in modeling many domains.

Viewed abstractly, a **graph** G is simply a set V of **vertices** and a collection E of pairs of vertices from V,
called **edges**. Thus, a graph is a way of representing connections or relationships between pairs of objects from some
setV.

Edges in a graph are either directed or undirected. An edge (u,v) is said to be **directed** from u to v if the pair (
u,v) is ordered, with u preceding v. An edge (u,v) is said to be **undirected** if the pair (u,v) is not ordered.

If all the edges in a graph are undirected, then we say the graph is an **undirected graph**. Likewise, a directed
graph, also called a **digraph**, is a graph whose edges are all directed.

A graph that has both directed and undirected edges is often called a **mixed graph**. Note that an undirected or mixed
graph can be converted into a directed graph by replacing every undirected edge (u,v) by the pair of directed edges (
u,v) and (v,u). It is often useful, however, to keep undirected and mixed graphs represented as they are, for such
graphs have several applications

The two vertices joined by an edge are called the **end vertices** (or **endpoints**) of the edge. If an edge is
directed, its first endpoint is its **origin** and the other is the **destination** of the edge. Two vertices u and v
are said to be **adjacent** if there is an edge whose end vertices are u and v. An edge is said tobe **incident** to a
vertex if the vertex is one of the edge’s endpoints.

The **outgoing edges** of a vertex are the directed edges whose origin is that vertex. The **incoming edges** of a
vertex are the directed edges whose destination is that vertex

The **degree** of a vertex v, denoted `deg(v)`, is the number of incident edges of v.The **in-degree** and **
out-degree** of a vertex v are the number of the incoming and outgoing edges of v, and are denoted `indeg(v)`
and `outdeg(v)`, respectively.

The definition of a graph refers to the group of edges as a **collection**, not a **set**, thus allowing two undirected
edges to have the same end vertices, and for two directed edges to have the same origin and the same destination. Such
edges are called **parallel edges** or **multiple edges** (f.e. they could indicate different flights operating on the
same route at different times of the day in a flight network).

Another special type of edge is one that connects a vertex to itself. Namely, we say that an edge (undirected or
directed) is a **self-loop** if its two endpoints coincide.

With few exceptions, graphs do not have parallel edges or self-loops. Such graphs are said to be **simple**. Thus, we
can usually say that the edges of a simple graph are a set of vertex pairs (and not just a collection). Throughout this
chapter, we assume that a graph is simple unless otherwise specified.

A **path** is a sequence of alternating vertices and edges that starts at a vertex and ends at a vertex such that each
edge is incident to its predecessor and successor vertex. A **cycle** is a path that starts and ends at the same vertex,
and that includes at least one edge. We say that a path is **simple** if each vertex in the path is distinct, and we say
that a cycle is **simple** if each vertex in the cycle is distinct, except for the first and last one.

A **directed path** is a path such that all edges are directed and are traversed along their direction. A **directed
cycle** is similarly defined.

Note that a directed graph may have a cycle consisting of two edges with opposite direction between the same pair of
vertices. A directed graph is **acyclic** if it has no directed cycles.

If a graph is simple, we may omit the edges when describing path P or cycle C, as these are well-defined, in which case
P is a list of adjacent vertices and C is a cycle of adjacent vertices.

Given vertices u and v of a (directed) graph G, we say that u **reaches** v,and that v is **reachable** from u,if G has
a (directed) path from u to v. In an undirected graph, the notion of **reachability** is symmetric, that is to say, u
reaches v if an only if v reaches u. However, in a directed graph, it is possible that u reaches v but v does not reach
u, because a directed path must be traversed according to the respective directions of the edges

A graph is **connected** if, for any two vertices, there is a path between them. A directed graph G' is **strongly
connected** if for any two vertices u and v of G', u reaches v and v reaches u

A **subgraph** of a graph G is a graph H whose vertices and edges are subsets of the vertices and edges of G,
respectively. A **spanning subgraph** of G is a subgraph of G that contains all the vertices of the graph G. If a graph
G is not connected, its maximal connected subgraphs are called the **connected components** of G.

> A **forest** is a graph without cycles. A **tree** is a connected forest, that is, a connected graph without cycles.
> A **spanning tree** of a graph is a spanning subgraph that is a tree.

(...)

## The Graph ADT

We model the abstraction as a combination of three data types: Vertex, Edge,and Graph. A Vertex is a lightweight object
that stores an arbitrary element provided by the user; we assume it supports a method, `element()`, to retrieve the
stored element. An Edge also stores an associated object retrieved with the `element()` method. In addition, we assume
that an Edge supports the following methods:

* **endpoints():** Return a tuple (u,v) such that vertex u is the origin of the edge and vertex v is the destination;
  for an undirected graph, the orientation is arbitrary.
* **opposite(v):** Assuming vertex v is one endpoint of the edge (either origin or destination), return the other
  endpoint.

We presume that a graph can be either undirected or directed, with the designation declared upon construction; recall
that a mixed graph can be represented as a directed graph, modeling edge {u,v} as a pair of directed edges (u,v) and (
v,u). The Graph ADT includes the following methods:

* vertex_count(): Return the number of vertices of the graph.
* vertices(): Return an iteration of all the vertices of the graph.
* edge_count(): Return the number of edges of the graph.
* edges(): Return an iteration of all the edges of the graph.
* get_edge(u,v): Return the edge from vertex u to vertex v, if one exists; otherwise return None. For an undirected
  graph, there is no difference between get edge(u,v) and get edge(v,u).
* degree(v, out=True): For an undirected graph, return the number of edges incident to vertex v. For a directed graph,
  return the number of outgoing edges incident to vertex v, as designated by the optional parameter.
* incident_edges(v, out=True): Return an iteration of all edges incident to vertex v.In the case of a directed graph,
  report outgoing edges by default; report incoming edges if the optional parameter is set to False.
* insert_vertex(x=None): Create and return a new Vertex storing element x.
* insert_edge(u, v, x=None): Create and return a new Edge from vertex u to vertex v, storing element x (None by default)
* remove_vertex(v): Remove vertex v and all its incident edges from the graph.
* remove_edge(e): Remove edge e from the graph.

## Data Structures for Graphs

we introduce four data structures for representing a graph. In each representation, we maintain a collection to store
the vertices of a graph. However, the four representations differ greatly in the way they organize the edges.

![](C:\Users\rober\Pictures\graph_DS.PNG)

### Edge List Structure

It is possibly the simplest, though not the most efficient, representation of a graph G. All vertex objects are stored
in an unordered list V,and all edge objects are stored in an unordered list E.

To support the many methods of the Graph ADT, we assume the following additional features of an edge list
representation. Collections V and E are represented with doubly linked lists using our PositionalList class.

**Vertex Objects**

The vertex object for a vertex v storing element x has instance variables for:

* A reference to element x, to support the element() method.
* A reference to the position of the vertex instance in the listV, thereby allowing v to be efficiently removed from V
  if it were removed from the graph.

**Edge Objects**

The edge object for an edge e storing element x has instance variables for:

* A reference to element x, to support the element() method.
* References to the vertex objects associated with the endpoint vertices of e. These allow the edge instance to provide
  constant-time support for methods endpoints() and opposite(v).
* A reference to the position of the edge instance in list E, thereby allowing e to be efficiently removed from E if it
  were removed from the graph.

#### Performance of the Edge List Structure

We begin by discussing the space usage, which is O(n+m) for representing a graph with n vertices and m edges. Each
individual vertex or edge instance uses O(1) space, and the additional lists V and E use space proportional to their
number of entries.

The most significant limitations of an edge list structure, especially when compared to the other graph representations,
are the O(m) running times of methods get edge(u,v), degree(v),and incident edges(v). The problem is that with all edges
of the graph in an unordered list E, the only way to answer those queries is through an exhaustive inspection of all
edges. The other data structures introduced in this section will implement these methods more efficiently.

Finally, we consider the methods that update the graph. It is easy to add a new vertex or a new edge to the graph
in `O(1)` time. For example, a new edge can be added to the graph by creating an Edge instance storing the given element
as data, adding that instance to the positional list E, and recording its resulting Position within E as an attribute of
the edge. That stored position can later be used to locate and remove this edge from E in O(1) time, and thus implement
the method remove edge(e)

It is worth discussing why the remove vertex(v) method has a running time of O(m). As stated in the graph ADT, when a
vertex v is removed from the graph, all edges incident to v must also be removed (otherwise, we would have a
contradiction of edges that refer to vertices that are not part of the graph). To locate the incident edges to the
vertex, we must examine all edges of E.

### Adjacency List Structure

the adjacency list structure groups the edges of a graph by storing them in smaller, secondary containers that are
associated with each individual vertex. Specifically, for each vertex v,we maintain a collection I(v), called the
**incidence collection** of v, whose entries are edges incident to v.

In the case of a directed graph, outgoing and incoming edges can be respectively stored in two separate collections,
Iout(v) and Iin(v). Traditionally, the incidence collection I(v) for a vertex v is a list, which is why we call this way
of representing a graph the adjacency list structure.

We require that the primary structure for an adjacency list maintain the collection V of vertices in a way so that we
can locate the secondary structure I(v) for a given vertex v in O(1) time. This could be done by using a positional list
to represent V, with each Vertex instance maintaining a direct reference to its I(v) incidence collection. If vertices
can be uniquely numbered from 0 to n−1, we could instead use a primary array-based structure to access the appropriate
secondary lists.

The primary benefit of an adjacency list is that the collection I(v) contains exactly those edges that should be
reported by the method incident edges(v).Therefore, we can implement this method by iterating the edges of I(v) in O(
deg(v)) time, where deg(v) is the degree of vertex v. This is the best possible outcome for any graph representation,
because there are deg(v) edges to be reported.

#### Performance of the Adjacency List Structure

Asymptotically, the space requirements for an adjacency list are the same as an edge list structure, using O(n +m) space
for a graph with n vertices and m edges. The primary list of vertices uses O(n) space. The sum of the lengths of all
secondary lists is O(m).

We have already noted that the incident edges(v) method can be achieved in O(deg(v)) time based on use of I(v). We can
achieve the degree(v) method of the graph ADT to use O(1) time. To locate a specific edge for implementing get edge(u,v)
, we can search through either I(u) and I(v). By choosing the smaller of the two, we get `O(min(deg(u),deg(v)))` running
time.

To efficiently support deletions of edges, an edge (u,v) would need to maintain a reference to its positions within both
I(u) and I(v), so that it could be deleted from those collections in O(1) time. To remove a vertex v, we must also
remove any incident edges, but at least we can locate those edges in O(deg(v)) time.

The easiest way to support edges() in O(m) and count edges() in O(1) is to maintain an auxiliary list E of edges, as in
the edge list representation. Otherwise, we can implement the edges method in O(n+m) time by accessing each secondary
list and reporting its edges, taking care not to report an undirected edge (u,v) twice.

### Adjacency Map Structure

We can improve the performance by using a hash-based map to implement I(v) for each vertex v. Specifically, we let the
opposite endpoint of each incident edge serve as a key in the map, with the edge structure serving as the value. We call
such a graph representation an adjacency map.

The advantage of the adjacency map, relative to an adjacency list, is that the get edge(u,v) method can be implemented
in expected O(1) time by searching for vertex u as a key in I(v), or vice versa. This provides a likely improvement over
the adjacency list, while retaining the worst-case bound of `O(min(deg(u),deg(v)))`.

In comparing the performance of adjacency map to other representations we find that it essentially achieves optimal
running times for all methods, making it an excellent all-purpose choice as a graph representation.

### Adjacency Matrix Structure

The adjacency matrix structure for a graph G augments the edge list structure with a matrix A (a two-dimensional array).
which allows us to locate an edge between a given pair of vertices in worst-case constant time. In the adjacency matrix
representation, we think of the vertices as being the integers in the set {0,1,... ,n−1} and the edges as being pairs of
such integers. This allows us to store references to edges in the cells of a two-dimensional n×n array A.

Specifically, the cell A[i, j] holds a reference to the edge (u,v), if it exists, where u is the vertex with index i and
v is the vertex with index j. If there is no such edge, then A[i, j]= None. We note that array A is symmetric if graph G
is undirected, as `A[i, j]= A[ j, i]` for all pairs i and j.

The most significant advantage of an adjacency matrix is that any edge (u,v) can be accessed in worst-case O(1) time;
recall that the adjacency map supports that operation in O(1) expected time. However, several operation are less
efficient with an adjacency matrix. For example, to find the edges incident to vertex v,we must presumably examine all n
entries in the row associated with v; recall that an adjacency list or map can locate those edges in optimal O(deg(v))
time. Adding or removing vertices from a graph is problematic, as the matrix must be resized.

Furthermore, the O(n^2) space usage of an adjacency matrix is typically far worse than the O(n+m) space required of the
other representations. Although, in the worst case, the number of edges in a **dense** graph will be proportional to
n^2, most real-world graphs are **sparse**. In such cases, use of an adjacency matrix is inefficient. However, if a
graph is dense, the constants of proportionality of an adjacency matrix can be smaller than that of an adjacency list or
map. In fact, if edges do not have auxiliary data, a Boolean adjacency matrix can use one bit per edge slot, such that
**A[i, j]= True** if and only if associated (u,v) is an edge.

### Python Implementation

Our implementation will support directed or undirected graphs, but for ease of explanation, we first describe it in the
context of an undirected graph. We use a variant of the adjacency map representation. For each vertex v,we use a Python
dictionary to represent the secondary incidence map I(v).However, we do not explicitly maintain lists V and E, as
originally described in the edge list representation.

The list V is replaced by a top-level dictionary D that maps each vertex v to its incidence map I(v); note that we can
iterate through all vertices by generating the set of keys for dictionary D. By using such a dictionary D to map
vertices to the secondary incidence maps, we need not maintain references to those incidence maps as part of the vertex
structures. Also, a vertex does not need to explicitly maintain a reference to its position in D, because it can be
determined in O(1) expected time. This greatly simplifies our implementation.

However, a consequence of our design is that some worst-case running time bounds for the graph ADT operations become
**expected** bounds. Rather than maintain list E, we are content with taking the union of the edges found in the various
incidence maps; technically, this runs in O(n+m) time rather than strictly O(m) time, as the dictionary D has n keys,
even if some incidence maps are empty.

Classes Vertex and Edge are rather simple, and can be nested within the more complex Graph class. Note that we define
the `__hash__` method for both Vertex and Edge so that those instances can be used as keys in Python’s hash-based sets
and dictionaries. Graphs are undirected by default, but can be declared as directed with an optional parameter to the
constructor.

Internally, we manage the directed case by having two different top-level dictionary instances, outgoing and incoming,
such that outgoing[v] maps to another dictionary representing `I_out(v)`,and incoming[v] maps to a representation
of `I_in(v)`. In order to unify our treatment of directed and undirected graphs, we continue to use the outgoing and
incoming identifiers in the undirected case, yet as aliases to the same dictionary. For convenience, we define a utility
named is directed to allow us to distinguish between the two cases.

For methods degree and incident edges, which each accept an optional parameter to differentiate between the outgoing and
incoming orientations, we choose the appropriate map before proceeding. For method insert vertex, we always initialize
outgoing[v] to an empty dictionary for new vertex v. In the directed case, we independently initialize incoming[v] as
well. For the undirected case, that step is unnecessary as outgoing and incoming are aliases. We leave the
implementations of methods remove vertex and remove edge as exercises.

## Graph Traversals

Formally, a **traversal** is a systematic procedure for exploring a graph by examining all of its vertices and edges. A
traversal is efficient if it visits all the vertices and edges in time proportional to their number, that is, in linear
time. Interesting problems that deal with reachability in an undirected graphG include the following:

* Computing a path from vertex u to vertex v, or reporting that no such path exists.
* Given a start vertex s of G, computing, for every vertex v of G, a path with the minimum number of edges between s and
  v, or reporting that no such path exists.
* Testing whether G is connected.
* Computing a spanning tree of G,if G is connected.
* Computing the connected components of G.
* Computing a cycle in G, or reporting that G has no cycles.

Interesting problems that deal with reachability in a directed graph G include the following:

* Computing a directed path from vertex u to vertex v, or reporting that no such path exists.
* Finding all the vertices of G that are reachable from a given vertex s.
* Determine whether G is acyclic.
* Determine whether G is strongly connected.

we present two efficient graph traversal algorithms.

### Depth-First Search

The first traversal algorithm we consider in this section is **depth-first search (DFS)**. Depth-first search is useful
for testing a number of properties of graphs, including whether there is a path from one vertex to another and whether
or not a graph is connected.

    Algorithm DFS(G,u): {We assume u has already been marked as visited}
      Input: Agraph G and a vertex u of G 
      Output: A collection of vertices reachable from u, with their discovery edges 
      
      for each outgoing edge e =(u,v) of u do 
        if vertex v has not been visited then 
          Mark vertex v as visited (via edge e). 
          Recursively call DFS(G,v).

#### Classifying Graph Edges with DFS

An execution of depth-first search can be used to analyze the structure of a graph, based upon the way in which edges
are explored during the traversal. The DFS process naturally identifies what is known as the depth-first search tree
rooted at a starting vertex s. Whenever an edge e =(u,v) is used to discover a new vertex v during the DFS algorithm,
that edge is known as a **discovery edge** or **tree edge**, as oriented from u to v. All other edges that are
considered during the execution of DFS are known as **non-tree edges**, which take us to a previously visited vertex.

In the case of an undirected graph, we will find that all non-tree edges that are explored connect the current vertex to
one that is an ancestor of it in the DFS tree. We will call such an edge a **back edge**.

When performing a DFS on a directed graph, there are three possible kinds of non-tree edges:

* **back edges**, which connect a vertex to an ancestor in the DFS tree
* **forward edges**, which connect a vertex to a descendant in the DFS tree
* **cross edges**, which connect a vertex to a vertex that is neither its ancestor nor its descendant.

#### Properties of a Depth-First Search

There are a number of observations that we can make about the depth-first search algorithm, many of which derive from
the way the DFS algorithm partitions the edges of a graph G into groups.

> **Proposition :** Let G be an un directed graph on which a DFS traversal starting at a vertex s has been performed. Then
> the traversal visits all vertices in the connected component of s, and the discovery edges form a spanning tree of the
> connected component ofs.

Since we only follow a discovery edge when we go to an unvisited vertex, we will never form a cycle with such edges.
Therefore, the discovery edges form a connected subgraph without cycles, hence a tree. Moreover, this is a spanning tree
because, as we have just seen, the depth-first search visits each vertex in the connected component of s.

> **Proposition :** Let G be a directed graph. Depth-first search on G starting at a vertex s visits all the vertices of
> G that are reachable from s. Also, the DFStree contains directed paths from s to every vertex reachable from s.

Note that since back edges always connect a vertex v to a previously visited vertex u, each back edge implies a cycle in
G, consisting of the discovery edges from u to v plus the back edge (u,v).

#### Running Time of Depth-First Search

In terms of its running time, depth-first search is an efficient method for traversing a graph. Note that DFS is called
at most once on each vertex (since it gets marked as visited), and therefore every edge is examined at most twice for an
undirected graph, once from each of its end vertices, and at most once in a directed graph, from its origin vertex.

If we let ns ≤ n be the number of vertices reachable from a vertex s,and ms ≤ m be the number of incident edges to those
vertices, a DFS starting at s runs in O(ns+ms) time, provided the following conditions are satisfied:

* The graph is represented by a data structure such that creating and iterating through the incident edges(v) takes O(
  deg(v)) time, and the e.opposite(v) method takes O(1) time.
* We have a way to “mark” a vertex or edge as explored, and to test if a vertex or edge has been explored in O(1) time.

**Proposition :** Let G be an un directed graph with n vertices and m edges. A DFS traversal ofG can be performed in O(
n+m) time, and can be used to solve the following problems in O(n+m) time:

* Computing a path between two given vertices of G, if one exists.
* Testing whether G is connected.
* Computing a spanning tree of G,if G is connected.
* Computing the connected components of G.
* Computing a cycle in G, or reporting thatG has no cycles.

**Proposition :** Let G be a directed graph with n vertices and m edges. A DFS traversal of G can be performed in O(
n+m) time, and can be used to solve the following problems inO(n+m) time:

* Computing a directed path between two given vertices of G, if one exists.
* Computing the set of vertices of G that are reachable from a given vertex s.
* Testing whether G is strongly connected.
* Computing a directed cycle in G, or reporting that G is acyclic.
* Computing the transitive closure of G

#### DFS Implementation and Extensions

In order to track which vertices have been visited, and to build a representation of the resulting DFS tree, our
implementation introduces a third parameter, named discovered. This parameter should be a Python dictionary that maps a
vertex of the graph to the tree edge that was used to discover that vertex. As a technicality, we assume that the source
vertex u occurs as a key of the dictionary, with None as its value. Thus, a caller might start the traversal as follows:

    result = {u: None} 
    DFS(g, u, result)

If we could assume that vertices could be numbered from 0 to n−1, then those numbers could be used as indices into an
array-based lookup table rather than a hash-based map. Alternatively, we could store each vertex’s discovery status and
associated tree edge directly as part of the vertex instance.

#### Reconstructing a Path from u to v

We can use the basic DFS function as a tool to identify the (directed) path leading from vertex u to v,if v is reachable
from u. This path can easily be reconstructed from the information that was recorded in the discovery dictionary during
the traversal.

To reconstruct the path, we begin at the end of the path, examining the discovery dictionary to determine what edge was
used to reach vertex v, and then what the other endpoint of that edge is. We add that vertex to a list, and then repeat
the process to determine what edge was used to discover it. Once we have traced the path all the way back to the
starting vertex u, we can reverse the list so that it is properly oriented from u to v, and return it to the caller.
This process takes time proportional to the length of the path, and therefore it runs in O(n) time (in addition to the
time originally spent calling DFS).

#### Testing for Connectivity

We can use the basic DFS function to determine whether a graph is connected. In the case of an undirected graph, we
simply start a depth-first search at an arbitrary vertex and then test whether len(discovered) equals n at the
conclusion. If the graph is connected, then by Proposition , all vertices will have been discovered; conversely, if the
graph is not connected, there must be at least one vertex v that is not reachable from u, and that will not be
discovered.

For directed graph, G, we may wish to test whether it is strongly connected,that is, whether for every pair of vertices
u and v, both u reaches v and v reaches u.

We begin by performing a depth-first search of our directed graph G starting at an arbitrary vertex s. If there is any
vertex of G that is not visited by this traversal, and is not reachable from s, then the graph is not strongly
connected. If this first depth-first search visits each vertex of G, we need to then check whether s is reachable from
all other vertices. Conceptually, we can accomplish this by making a copy of graph G, but with the orientation of all
edges reversed. A depth-first search starting at s in the reversed graph will reach every vertex that could reach s in
the original. In practice, a better approach than making a new graph is to reimplement a version of the DFS method that
loops through all incoming edges to the current vertex, rather than all outgoing edges. Since this algorithm makes just
two DFS traversals of G, it runs in O(n+m) time.

#### Computing all Connected Components

When a graph is not connected, the next goal we may have is to identify all **connected components** of an undirected
graph, or the **strongly connected components** of a directed graph. We begin by discussing the undirected case.

If an initial call to DFS fails to reach all vertices of a graph, we can restart a new call to DFS at one of those
unvisited vertices.

Although the DFS complete function makes multiple calls to the original DFS function, the total time spent by a call to
DFS complete is O(n+m). Because each call to DFS explores a different component, the sum of ns +ms terms is n+m. The O(
n+m) total bound applies to the directed case as well, even though the sets of reachable vertices are not necessarily
disjoint. However, because the same discovery dictionary is passed as a parameter to all DFS calls, we know that the DFS
subroutine is called once on each vertex, and then each outgoing edge is explored only once during the process.

The DFS complete function can be used to analyze the connected components of an undirected graph. The discovery
dictionary it returns represents a **DFS forest** for the entire graph. We say this is a forest rather than a tree,
because the graph may not be connected. The number of connected components can be determined by the number of vertices
in the discovery dictionary that have None as their discovery edge (those are roots of DFS trees). A minor modification
to the core DFS method could be used to tag each vertex with a component number when it is discovered.

The situation is more complex for finding strongly connected components of a directed graph. There exists an approach
for computing those components in O(n+m) time, making use of two separate depth-first search traversals, but the details
are beyond the scope of this book.

#### Detecting Cycles with DFS

For both undirected and directed graphs, a cycle exists if and only if a back edge exists relative to the DFS traversal
of that graph. It is easy to see that if a back edge exists, a cycle exists by taking the back edge from the descendant
to its ancestor and then following the tree edges back to the descendant. Conversely, if a cycle exists in the graph,
there must be a back edge relative to a DFS (although we do not prove this fact here).

Algorithmically, detecting a back edge in the undirected case is easy, because all edges are either tree edges or back
edges. In the case of a directed graph, additional modifications to the core DFS implementation are needed to properly
categorize a nontree edge as a back edge. When a directed edge is explored leading to a previously visited vertex, we
must recognize whether that vertex is an ancestor of the current vertex.

## Breadth-First Search

The advancing and backtracking of a depth-first search, as described in the previous section, defines a traversal that
could be physically traced by a single person exploring a graph. The BFS algorithm is more akin to sending out, in all
directions, many explorers who collectively traverse a graph in coordinated fashion.

A BFS proceeds in rounds and subdivides the vertices into levels. BFS starts at vertex s, which is at level 0. In the
first round, we paint as “visited,” all vertices adjacent to the start vertex s—these vertices are one step away from
the beginning and are placed into level 1. In the second round, we allow all explorers to go two steps (i.e., edges)
away from the starting vertex. These new vertices, which are adjacent to level 1 vertices and not previously assigned to
a level, are placed into level 2 and marked as “visited.” This process continues in similar fashion, terminating when no
new vertices are found in a level.

For BFS on an undirected graph, all non-tree edges are cross edges , and for BFS on a directed graph, all non-tree edges
are either back edges or cross edges.

The BFS traversal algorithm has a number of interesting properties, some of which we explore in the proposition that
follows.

**Proposition :** Let G be an undirected or directed graph on which a BFS traversal starting at vertex s has been
performed. Then

* The traversal visits all vertices ofG that are reachable from s.
* For each vertex v at level i, the path of the BFStree T between s and v has i edges, and any other path of G from s to
  v has at least i edges.
* If(u,v) is an edge that is not in the BFS tree, then the level number of v can be at most 1 greater than the level
  number of u.

The analysis of the running time of BFS is similar to the one of DFS

**Proposition :** Let G be a graph with n vertices and m edges represented with the adjacency list structure. A BFS
traversal of G takes O(n+m) time.

Although our implementation of BFS progresses level by level, the BFS algorithm can also be implemented using a single
FIFO queue to represent the current fringe of the search. Starting with the source vertex in the queue, we repeatedly
remove the vertex from the front of the queue and insert any of its unvisited neighbors to the back of the queue

In comparing the capabilities of DFS and BFS, both can be used to efficiently find the set of vertices that are
reachable from a given source, and to determine paths to those vertices. However, BFS guarantees that those paths use as
few edges as possible. For an undirected graph, both algorithms can be used to test connectivity, to identify connected
components, or to locate a cycle. For directed graphs, the DFS algorithm is better suited for certain tasks, such as
finding a directed cycle in the graph, or in identifying the strongly connected components.

