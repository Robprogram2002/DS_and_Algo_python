from random import randint


class MutableMapping:
    # ------------- user defined methods --------------- #
    def __getitem__(self, item):
        raise NotImplementedError()

    def __setitem__(self, key, value):
        raise NotImplementedError()

    def __delitem__(self, key):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    # ------------ Concrete methods base on the before 5 -------------- #

    def __contains__(self, k):
        try:
            self[k]
            return True
        except KeyError:
            return False

    def get(self, k, d=None):
        try:
            result = self[k]
            return result
        except KeyError:
            return d

    def setdefault(self, k, d):
        try:
            result = self[k]
            return result
        except KeyError:
            self[k] = d
            return d

    def pop(self, k, d=None):
        try:
            result = self[k]
            del self[k]
            return result
        except KeyError:
            if d is None:
                raise KeyError('key cannot be None')
            return d

    def popitem(self):
        if len(self) == 0:
            raise KeyError('Empty dict')
        index = randint(0, len(self))
        for i, k in enumerate(self):
            if i == index:
                del self[k]

    def clear(self):
        for k in self:
            del self[k]

    def keys(self):
        return {k for k in self}

    def values(self):
        return {self[k] for k in self}

    def items(self):
        return {(k, self[k]) for k in self}

    def update(self, other):
        for k in other:
            self[k] = other[k]

    def __eq__(self, other):
        keys = self.keys()
        if keys != other.keys():
            return False
        for k in keys:
            if self[k] != other[k]:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)
