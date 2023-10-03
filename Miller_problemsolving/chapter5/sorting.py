# Thecode below shows the complete bubble_sort function. It takes the list as a parameter, and
# modifies it by exchanging items as necessary.
def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        print("pass number: {}".format(pass_num))
        for i in range(pass_num):
            print("exchange step: {}".format(i))
            if a_list[i] > a_list[i + 1]:
                # exchange or swap using a temporarily variable
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp


# lets test it
num_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(num_list)
print(num_list)


# Note : The exchange operation, sometimes called a “swap,” is slightly different in Python than in
# most other programming languages. Typically, swapping two elements in a list requires a
# temporary storage location (an additional memory location). A code fragment such as

# temp = a_list[i]
# a_list[i] = a_list[j]
# a_list[j] = temp

# will exchange the 𝑖th and 𝑗th items in the list. Without the temporary storage, one of the values
# would be overwritten.

# In Python, it is possible to perform simultaneous assignment. The statement a, b = b, a
# will result in two assignment statements being done at the same time . Using
# simultaneous assignment, the exchange operation can be done in one statement

def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        # if during a pass there are no exchanges, then we know that the list must be sorted.
        exchanges = False
        print("pass number: {}".format(pass_num))
        for i in range(pass_num):
            print("exchange step: {}".format(i))
            if a_list[i] > a_list[i + 1]:
                # exchange or swap using simultaneous assignment
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                # since was exchanged was made we update the variable
                exchanges = True
        pass_num = pass_num - 1


my_list = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
short_bubble_sort(my_list)
print(my_list)


def selection_sort(a_list):
    # On each pass, the largest remaining item is selected and then placed in its proper location
    for fill_slot in range(len(a_list) - 1, 0, -1):
        max_val_index = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[max_val_index]:
                max_val_index = location
        # swap the las corresponding items to place the greater item at the end
        a_list[fill_slot], a_list[max_val_index] = a_list[max_val_index], a_list[fill_slot]


# lets test it

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(my_list)
print(my_list)


# --------------------------------------------------------------------------

# The merge_sort function shown below begins by asking the base case question. If the length
# of the list is less than or equal to one, then we already have a sorted list and no more processing
# is necessary. If, on the other hand, the length is greater than one, then we use the Python
# slice operation to extract the left and right halves. It is important to note that the list may not
# have an even number of items. That does not matter, as the lengths will differ by at most one.
def merge_sort(a_list):
    print("Splitting the list: ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        # Once the merge_sort function is invoked on the left half and the right half
        #  it is assumed they are sorted. The rest of the function is responsible for merging the
        # two smaller sorted lists into a larger sorted list. Notice that the merge operation places the items
        # back into the original list (a_list) one at a time by repeatedly taking the smallest item from
        # the sorted lists.

        # The algorithm maintains three pointers, one for each of the two arrays and one for maintaining the current
        # index of the final sorted array.
        i = 0
        j = 0
        k = 0

        # Have we reached the end of any of the arrays?
        #     No:
        #         Compare current elements of both arrays
        #         Copy smaller element into sorted array
        #         Move pointer of element containing smaller element

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[k] = right_half[j]
                j += 1
            k += 1

        #     Yes:
        #         Copy all remaining elements of non-empty array

        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j += 1
            k += 1
    print("Merging ", a_list)


# let's test it

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(my_list)
print(my_list)


# Recall that the slicing operator is 𝑂(𝑘) where 𝑘 is the size of the slice. In order to guarantee
# that merge_sort will be 𝑂(𝑛 log 𝑛) we will need to remove the slice operator. Again, this is
# possible if we simply pass the starting and ending indices along with the list when we make the
# recursive call.

def merge_sort_v2(a_list, start, end):
    print("Splitting the list: ", a_list[start:end + 1], "\t start: {} , end {}".format(start, end))
    if end > start:
        mid_point = (start + end - 1) // 2
        print("mid:", mid_point)
        merge_sort_v2(a_list, start, mid_point)
        merge_sort_v2(a_list, mid_point + 1, end)

        #   Initial indexes of first and second subarrays
        i = start
        j = mid_point
        # Initial index of merged subarray array
        k = start

        # while i < mid_point + 1 and j < end:
        #     if a_list[i] < a_list[j+1]:
        #         a_list[k] = a_list[i]
        #         i += 1
        #     else:
        #         a_list[k] = a_list[j+1]
        #         j += 1
        #     k += 1
        #
        # # Copy remaining elements of left half if any
        # while i < mid_point + 1:
        #     a_list[k] = a_list[i]
        #     i += 1
        #     k += 1
        #
        # # Copy remaining elements of right half if any
        # while j < end:
        #     a_list[k] = a_list[j]
        #     j += 1
        #     k += 1
    print("Merging ", a_list[start:end + 1])


# To sort an entire array, we need to call merge_sort_v2(list, 0, length(list)-1).
#
# my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# merge_sort_v2(my_list, 0, len(my_list) - 1)
# print(my_list)

# --------------------------------------------------------------------------

def quick_sort(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)

        quick_sort(a_list, first, split_point - 1)
        quick_sort(a_list, split_point + 1, last)


def partition(a_list, first, last):
    pivot_value = a_list[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] < pivot_value:
            left_mark += 1
        while right_mark >= left_mark and a_list[right_mark] >= pivot_value:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]

    a_list[right_mark], a_list[first] = a_list[first], a_list[right_mark]
    print("a split point {} for pivot {}".format(right_mark, pivot_value))
    return right_mark


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(my_list, 0, len(my_list) - 1)
print(my_list)
