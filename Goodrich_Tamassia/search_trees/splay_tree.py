from search_trees.binary_search_tree import BinaryTreeMap


class SplayTreeMap(BinaryTreeMap):
    """Sorted map implementation using a splay tree"""

    # --------------------------------- splay operation --------------------------------
    def _splay(self, p):
        while p != self.root():
            parent = self.parent(p)
            grandparent = self.parent(p)
            if grandparent is None:
                # zig case
                self._rotate(p)
            elif (p == self.left(parent)) == (parent == self.left(grandparent)):
                # zig-zig case
                self._rotate(parent)
                self._rotate(p)
            else:
                # zig-zag case
                self._rotate(p)
                self._rotate(p)

    # ---------------------------- override balancing hooks ----------------------------

    def _rebalance_insert(self, p):
        self._splay(p)

    def _rebalance_delete(self, p):
        if p is not None:
            self._splay(p)

    def _rebalance_access(self, p):
        self._splay(p)
