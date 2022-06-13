# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def disjoint1(A, B, C):
    """Return True if there is no element common to all three lists."""
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False  # we found a common value
    return True  # if we reach this, sets are disjoint


def disjoint2(A, B, C):
    """Return True if there is no element common to all three lists."""
    for a in A:
        for b in B:
            if a == b:  # only check C if we found match from A and B
                for c in C:
                    if a == c:  # (and thus a == b == c)
                        return False  # we found a common value
    return True  # if we reach this, sets are disjoint


# Assuming it is possible to sort n numbers in O(nlogn) time, show that it is possible to solve the three-way set
# disjointness problem in O(nlogn) time

def disjoint3(A, B, C):
    """Return True if there is no element common to all three lists."""

    combined = sorted(A + B + C)
    for j in range(2, len(combined)):
        if combined[j] == combined[j - 1] == combined[j - 2]:
            return True
    return False


print(disjoint3([-2, 43, 123, 67, 12, 5, 6], [5, 7, -2, 31, 6, 12, -3], [3, 57, 2, 45, 12, 43, -12]))
