# The beauty of this design is that the concrete methods defined within the Tree abstract base class will be inherited
# by all subclasses. This promotes greater code reuse, as there will be no need for those subclasses to reimplement
# such behaviors.

# with the Tree class being abstract, there is no reason to create a direct instance of it, nor would such an instance
# be useful. The class exists to serve as a base for inheritance, and users will create instances of concrete subclasses
from linear_DA.Queue import LinkedQueue


class Tree:
    """ Abstract base class representing a tree structure """

    # ------------------------------- nested Position class -------------------------------
    class Position:
        """An abstraction representing the location of a single element"""

        def element(self):
            """Return the element stored at this Position"""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)

    # ---------- abstract methods that concrete subclass must support ----------

    def root(self):
        """Return Position representing the tree s root (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p: Position):
        """Return Position representing p s parent (or None if p is root)."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p: Position):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p: Position):
        """Generate an iteration of Positions representing p s children."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    # ---------- concrete methods implemented in this class ----------

    def is_root(self, p: Position):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p: Position):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p: Position):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def _height_recursive(self, p: Position):
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        return 1 + max(self._height_recursive(c) for c in self.children(p))

    def height(self, p: Position = None):
        """Return the height of the subtree rooted at Position p.
        If p is None, return the height of the entire tree. """
        if p is None:
            p = self.root()
        return self._height_recursive(p)

    # ------------------ Traversal methods -----------------------

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p: Position):
        """Generate a preorder iteration of positions in subtree rooted at p"""
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p: Position):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def breadth_first(self):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)

    def positions(self):
        """Generate an iteration of all positions of tree"""
        return self.breadth_first()

    def __iter__(self):
        """Generate an iteration of the tree s elements"""
        for p in self.positions():
            yield p.element()
