# Given a list of numbers in random order write a linear time algorithm to find the 𝑘th
# smallest number in the list

def get_kth_smallest(number_list, k):  # runs in O(kn) where k is a constant
    # TODO: check the sanity of the data parameter
    smallest = [number_list[0] for i in range(0, k)]
    count = 0
    while count < k:
        for number in number_list:
            if number < smallest[count] and count == 0:
                smallest[count] = number
            elif smallest[count] > number > smallest[count - 1]:
                smallest[count] = number
        count += 1

    return smallest


print(get_kth_smallest([34, 1, 78, 31, -23, 8, -200], 4))


# 5. Can you improve the algorithm from the previous problem to be 𝑂(𝑛 log(𝑛))?
# yes, we can use a sorting method that runs in nlogn

def get_kth_smallest_2(number_list, k):
    number_list.sort()  # n log(n)
    return number_list[:k]  # constant


print(get_kth_smallest_2([34, 1, 78, 31, -23, 8, -200], 4))
