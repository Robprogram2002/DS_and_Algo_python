import ctypes  # provides low-level arrays


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self, initial_capacity=0):
        """Create an empty array."""
        self._n = initial_capacity  # count actual elements
        self._capacity = initial_capacity + 1  # default array capacity
        self._A = self._make_array(initial_capacity + 1)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if isinstance(k, int):
            if 0 <= k < self._n:
                return self._A[k]  # retrieve from array
            elif -self._n <= k <= -1:
                return self._A[self._n + k]
            else:
                raise IndexError('invalid index')
        elif isinstance(k, slice):
            if 0 <= k.start <= self._n - 1 and 0 <= k.stop <= self._n:
                raise IndexError('Index out of box')
            length = k.stop - k.start
            slicing = DynamicArray(length)
            for j in range(length):
                slicing[j] = A[k.start + j]
            return slicing

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):  # nonpublic utility
        """Resize internal array to capacity c."""
        B = self._make_array(c)  # new (bigger) array
        for k in range(self._n):  # for each existing value
            B[k] = self._A[k]
        self._A = B  # use the bigger array
        self._capacity = c

    def _resize_and_insert(self, c, k, value):
        """Resize internal array to capacity c and insert a new element in the process"""
        B = self._make_array(c)
        for j in range(0, k):  # copy  all elemenst from index 0 to k-1
            B[j] = self._A[j]
        B[k] = value  # set value at index k
        for i in range(k, self._n):  # copy the rest of the original array
            B[i + 1] = self._A[i]
        self._A = B
        self._n += 1
        self._capacity = c

    def _make_array(self, c):  # nonpublic utility
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()  # see ctypes documentation

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this version)
        if self._n == self._capacity:  # not enough room
            return self._resize_and_insert(2 * self._capacity, k, value)  # so double capacity
        for j in range(self._n, k, -1):  # shift rightmost first
            self._A[j] = self._A[j - 1]
        self._A[k] = value  # store newest element
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)."""
        found = False
        for k in range(self._n):
            if self._A[k] == value:  # found a match!
                for j in range(k, self._n - 1):  # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None  # help garbage collection
                self._n -= 1  # we have one less item
                found = True
                break  # exit immediately

        if not found:
            raise ValueError('value not found')  # only reached if no match
        elif self._n < self._capacity // 4:
            self._resize(self._capacity / 2)

    def _remove_recursive(self, value, end):
        found_index = None
        k = end
        while k > 0 and found_index is None:
            if self._A[k - 1] == value:
                found_index = k - 1
            else:
                k -= 1

        if found_index is not None:
            for j in range(found_index, self._n - 1):
                self._A[j + 1], self._A[j] = self._A[j], self._A[j + 1]
            self._A[self._n - 1] = None
            self._n -= 1
            self._remove_recursive(value, found_index)

    def remove_all(self, value):
        self._remove_recursive(value, self._n)

    def pop(self, k=None):
        if k is not None and (0 <= k < self._n):
            for j in range(k, self._n - 1):
                self._A[j] = self._A[j + 1]

        self._A[self._n - 1] = None
        self._n -= 1

        if self._n < self._capacity // 4:
            self._resize(self._capacity // 2)

    def count(self, value):
        """Count the number of times a given object is found in the list. If it is not in the list return -1 """
        count = 0
        for k in range(self._n):
            if self._A[k] == value:
                count += 1
        return count if count > 0 else -1

    def index(self, value):
        """If value is found in the list return its index, otherwise return -1"""
        found = -1
        for k in range(self._n):
            if self._A[k] == value:
                found = k
                break
        return found

    def extend(self, other):
        if self._n + len(other) >= self._capacity:
            self._resize(2 * self._capacity)
        for k in range(self._n, self._n + len(other)):
            self._A[k] = other[k - self._n]
        self._n += len(other)

    def _recur_reverse(self, data: [], start: int, last: int):
        if start < last - 1:
            data[start], data[last - 1] = data[last - 1], data[start]  # swap first and last
            self._recur_reverse(data, start + 1, last - 1)  # recur on rest

    def reverse(self):
        self._recur_reverse(self._A, 0, self._n)

    def sort(self):
        print('asdjsnka')

    def print_lis(self):
        print('[', end=' ')
        for k in range(self._n):
            print(self._A[k], end=', ')
        print(']')

    def __contains__(self, item):
        return self.index(item) >= 0

    def __eq__(self, other):
        result = True
        if len(other) != len(self):
            result = False
        else:
            for k in range(self._n):
                if self._A[k] != other[k]:
                    result = False
                    break
        return result

    def __lt__(self, other):
        result = True
        n = min([len(self), len(other)])

        for k in range(n):
            if self._A[k] >= other[k]:
                result = False
                break

        return result

    def __le__(self, other):
        result = True
        k = 0
        n = min([len(self), len(other)])
        while result is True and k < n:
            if self._A[k] > other[k]:
                result = False
            k += 1
        return result

    def __add__(self, other):
        if isinstance(other, (int, float)):
            new_array = self._make_array(self._n)
            for k in range(self._n):
                new_array[k] = self._A[k] + other
            return list(new_array)
        elif isinstance(other, (list, DynamicArray)):
            new_array = self._make_array(self._n + len(other))
            for k in range(self._n):
                new_array[k] = self._A[k]
            for j in range(self._n, self._n + len(other)):
                new_array[j] = other[j - self._n]
            return list(new_array)
        else:
            raise TypeError('can only add a sequence or a number type')

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError('can only multiply by an integer value')
        size = self._n * other
        new_array = self._make_array(size)
        for k in range(size):
            # print(k, ' : ', k % self._n)
            new_array[k] = self._A[k % self._n]
        return list(new_array)

    def __setitem__(self, key, value):
        if 0 <= key < self._n:
            self._A[key] = value
        elif -self._n <= key <= -1:
            self._A[self._n + key] = value
        else:
            raise IndexError('index out of range')

    def __delitem__(self, key):
        self.pop(key)


if __name__ == '__main__':
    A = DynamicArray()
    A.append(3)
    A.append(200)
    A.append(-23)
    A.append(1)
    A.append(10)
    A.append(-2)
    A.append(0)
    print(A[-3])
    A.insert(2, 100)
    print(A._n)
    print(A._capacity)
    for i in range(len(A)):
        print(A[i], end='\t')
    A.insert(4, 0)
    print('')
    for i in range(len(A)):
        print(A[i], end='\t')
    print('')
    print(A._n)
    print(A._capacity)

    print('')
    A[1:3].print_lis()
    A.extend([1, 2, 3])
    A.print_lis()
    A[5] = -100
    A.print_lis()
    # A[-6] = 'abc'
    A.print_lis()
    A.pop()
    A.pop(2)
    A.print_lis()
    print(len(A))
    print(A._capacity)
    A.pop()
    A.pop()
    A.pop()
    print(len(A))
    print(A._capacity)
    A.print_lis()
    print(A + 3)
    print(A + [5, 100, -5])
    print(A * 3)
    A.reverse()
    A.print_lis()
    A.append(10)
    A.append(3)
    A.append(-2)
    A.append(0)
    A.append(3)
    A.insert(0, 3)
    A.print_lis()
    A.remove_all(3)
    A.print_lis()
