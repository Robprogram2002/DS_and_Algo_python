from Trees.linked_binary_tree import LinkedBinaryTree
from hash_tables.map_base import MapBase


class BinaryTreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree."""

    # ---------------------------- override Position class ----------------------------

    class Position(LinkedBinaryTree.Position):

        def key(self):
            """Return key of map's key-value pair."""
            return self.element()._key()

        def value(self):
            """Return value of map's key-value pair."""
            return self.element()._value

    # ------------------------------- nonpublic utilities -------------------------------

    def _subtree_search(self, p: Position, k):
        """Return Position of p's subtree having key k, or last node searched."""
        if p.key() == k:
            return p
        elif k < p.key() and self.left(p) is not None:
            return self._subtree_search(self.left(p), k)
        elif k > p.key() and self.right(p) is not None:
            return self._subtree_search(self.right(p), k)
        return p

    def _subtree_first_position(self, p: Position):
        """Return Position of first item in subtree rooted at p."""
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p: Position):
        """Return Position of last item in subtree rooted at p."""
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

        # --------------------- hooks used by subclasses to balance a tree ---------------------

    def _rebalance_insert(self, p):
        """Call to indicate that position p is newly added."""
        pass

    def _rebalance_delete(self, p):
        """Call to indicate that a child of p has been removed."""
        pass

    def _rebalance_access(self, p):
        """Call to indicate that position p was recently accessed."""
        pass

    # --------------------- public methods providing "positional" support ---------------------

    def first(self):
        """Return the first Position in the tree (or None if empty)."""
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """Return the last Position in the tree (or None if empty)."""
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        """Return the Position just before p in the natural order.

           Return None if p is the first position.
           """
        self._validate(p)
        if self.left(p) is not None:
            return self._subtree_last_position(self.left(p))
        else:
            walk = p
            ancestor = self.parent(p)
            while ancestor is not None and self.left(ancestor) == walk:
                walk = ancestor
                ancestor = self.parent(walk)
            return ancestor

    def after(self, p: Position):
        """Return the Position just after p in the natural order.

        Return None if p is the last position.
        """
        self._validate(p)
        if self.right(p) is not None:
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            ancestor = self.parent(walk)
            while ancestor is not None and self.right(ancestor) == walk:
                walk = ancestor
                ancestor = self.parent(walk)
            return ancestor

    def find_position(self, k):
        """Return position with key k, or else neighbor (or None if empty)."""
        if self.is_empty():
            return None
        p = self._subtree_search(self.root(), k)
        self._rebalance_access(p)  # hook for balanced tree subclasses
        return p

    def delete(self, p: Position):
        """Remove the item at given Position."""
        self._validate(p)
        if self.num_children(p) == 2:
            r = self._subtree_last_position(self.left(p))
            self._replace(p, r.element())
            p = r

        parent = self.parent(p)
        self.delete(p)
        self._rebalance_delete(parent)

    # --------------------- public methods for (standard) map interface ---------------------

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        p = self.find_position(k)
        self._rebalance_access(p)  # hook for balanced tree subclasses
        if p is not None and p.key() == k:
            return p.value()
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        p = self.find_position(k)
        if p is None:
            leaf = self._add_root(self._Item(k, v))
        elif p.key() == k:
            p.element()._value = v
            self._rebalance_access(p)  # hook for balanced tree subclasses
            return
        else:
            if k < p.key():
                leaf = self._add_left(p, self._Item(k, v))
            else:
                leaf = self._add_right(p, self._Item(k, v))
        self._rebalance_insert(leaf)  # hook for balanced tree subclasses

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)  # rely on positional version
                return  # successful deletion complete
            self._rebalance_access(p)  # hook for balanced tree subclasses
        raise KeyError('Key Error: ' + repr(k))

    def __iter__(self):
        """Generate an iteration of all keys in the map in order."""
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    # --------------------- public methods for sorted map interface ---------------------

    def __reversed__(self):
        """Generate an iteration of all keys in the map in reverse order."""
        p = self.last()
        while p is not None:
            yield p.key()
            p = self.before(p)

    def find_min(self):
        """Return (key,value) pair with minimum key (or None if empty)."""
        if self.is_empty():
            return None
        item = self.first()
        return item.key(), item.value()

    def find_max(self):
        """Return (key,value) pair with maximum key (or None if empty)."""
        if self.is_empty():
            return None
        item = self.last()
        return item.key(), item.value()

    def find_le(self, k):
        """Return (key,value) pair with greatest key less than or equal to k.

        Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        p = self.find_position(k)
        if k >= p.key():
            return k, p.value()
        else:
            item = self.before(p)
            return item.key(), item.value() if item is not None else None

    def find_lt(self, k):
        """Return (key,value) pair with greatest key strictly less than k.

        Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        p = self.find_position(k)
        if not p.key() < k:
            p = self.before(p)
        return p.key(), p.value() if p is not None else None

    def find_ge(self, k):
        """Return (key,value) pair with least key greater than or equal to k.

           Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        p = self.find_position(k)
        if k <= p.key():
            return k, p.value()
        else:
            item = self.after(p)
            return item.key(), item.value() if item is not None else None

    def find_gt(self, k):
        """Return (key,value) pair with least key strictly greater than k.

           Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        p = self.find_position(k)
        if not k < p.key():
            p = self.after(p)
        return p.key(), p.value() if p is not None else None

    def find_range(self, start, stop):
        """Iterate all (key,value) pairs such that start <= key < stop.

        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if not self.is_empty():
            s = self.find_ge(start) if start is not None else self.first()
            while s is not None and (stop is None or s.key() < stop):
                yield s.key(), s.value()
                s = self.after(s)

        # --------------------- nonpublic methods to support tree balancing ---------------------

    def _relink(self, parent, child, make_left_child):
        """Relink parent node with child node (we allow child to be None)."""
        if make_left_child:  # make it a left child
            parent._left = child
        else:  # make it a right child
            parent._right = child
        if child is not None:  # make child point to parent
            child._parent = parent

    def _rotate(self, p):
        """Rotate Position p above its parent.

        Switches between these configurations, depending on whether p==a or p==b.

              b                  a
             / \                /  \
            a  t2             t0   b
           / \                     / \
          t0  t1                  t1  t2

        Caller should ensure that p is not the root.
        """
        """Rotate Position p above its parent."""
        x = p._node
        y = x._parent  # we assume this exists
        z = y._parent  # grandparent (possibly None)
        if z is None:
            self._root = x  # x becomes root
            x._parent = None
        else:
            self._relink(z, x, y == z._left)  # x becomes a direct child of z
        # now rotate x and y, including transfer of middle subtree
        if x == y._left:
            self._relink(y, x._right, True)  # x._right becomes left child of y
            self._relink(x, y, False)  # y becomes right child of x
        else:
            self._relink(y, x._left, False)  # x._left becomes right child of y
            self._relink(x, y, True)  # y becomes left child of x

    def _restructure(self, x):
        """Perform a trinode restructure among Position x, its parent, and its grandparent.

        Return the Position that becomes root of the restructured subtree.

        Assumes the nodes are in one of the following configurations:

            z=a                 z=c           z=a               z=c
           /  \                /  \          /  \              /  \
          t0  y=b             y=b  t3       t0   y=c          y=a  t3
             /  \            /  \               /  \         /  \
            t1  x=c         x=a  t2            x=b  t3      t0   x=b
               /  \        /  \               /  \              /  \
              t2  t3      t0  t1             t1  t2            t1  t2

        The subtree will be restructured so that the node with key b becomes its root.

                  b
                /   \
              a       c
             / \     / \
            t0  t1  t2  t3

        Caller should ensure that x has a grandparent.
        """
        """Perform trinode restructure of Position x with parent/grandparent."""
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):  # matching alignments
            self._rotate(y)  # single rotation (of y)
            return y  # y is new subtree root
        else:  # opposite alignments
            self._rotate(x)  # double rotation (of x)
            self._rotate(x)
            return x  # x is new subtree root
