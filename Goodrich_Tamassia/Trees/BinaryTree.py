from Trees.BaseTree import Tree


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    # --------------------- additional abstract methods ---------------------
    def left(self, p: Tree.Position):
        """Return a Position representing p s left child.
        Return None if p does not have a left child."""
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p: Tree.Position):
        """Return a Position representing p s right child.
        Return None if p does not have a right child."""
        raise NotImplementedError('must be implemented by subclass')

    # ---------- concrete methods implemented in this class ----------

    def sibling(self, p: Tree.Position):
        """Return a Position representing p s sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:
            return None
        return self.right(parent) if p == self.left(parent) else self.left(parent)

    def num_children(self, p: Tree.Position):
        count = 0 if self.left(p) is None else 1
        return count if self.right(p) is None else count + 1

    def children(self, p: Tree.Position):
        """Generate an iteration of Positions representing p s children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    # ------------------ Traversal methods -----------------------

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p: Tree.Position):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p  # visit p between its subtrees
        if self.right(p) is not None:  # if right child exists, traverse its subtree
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def positions(self):
        """Generate an iteration of the tree s positions."""
        return self.inorder()  # make inorder the default
