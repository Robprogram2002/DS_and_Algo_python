# better algorithm : O(n) linear
def find_min_v1(number_list):
    min_value = number_list[0]
    for num in number_list:
        if num < min_value:
            min_value = num
        else:
            continue
    return min_value


# worse algorithm: O(n^2) Quadratic
def find_min_v2(number_list):
    min_value = 0
    for num_a in number_list:
        min_value = num_a
        for num_b in number_list:
            if num_b < min_value:
                min_value = num_b
            else:
                continue
    return min_value


print(find_min_v1([2, 4, 67, 68, 12, 43, 12, -2, -113, 0, -10]))
print(find_min_v2([2, 4, 67, 68, 12, 43, 12, -2, -113, 0, -12]))


# An Anagram Detection Example

# Solution 1: Checking Off

# Our first solution to the anagram problem will check to see that each character in the first
# string actually occurs in the second. If it is possible to “checkoff” each character, then the
# two strings must be anagrams. Checking off a character will be accomplished by replacing it
# with the special Python value None. However, since strings in Python are immutable, the first
# step in the process will be to convert the second string to a list. Each character from the first
# string can be checked against the characters in the list and if found, checked off by replacement.

def anagram_solution_v1(word_a, word_b):
    word_b_list = list(word_b)
    pos1 = 0
    still_ok = True

    while pos1 < len(word_b_list) and still_ok is True:
        pos2 = 0
        found = False
        while pos2 < len(word_b_list) and not found:
            if word_a[pos1] == word_b_list[pos2]:
                found = True
            else:
                pos2 += 1

        if found is True:
            word_b_list[pos2] = None
        else:
            still_ok = False
        pos1 += 1

    return still_ok


print(anagram_solution_v1("abcd", "dcba"))


# To analyze this algorithm, we need to note that each of the 𝑛 characters in s1 will cause an
# iteration through up to 𝑛 characters in the list from s2. Each of the 𝑛 positions in the list will
# be visited once to match a character from s1. The number of visits then becomes the sum of
# he integers from 1 to n.
# Therefore, this solution is 𝑂(𝑛^2).


# Solution 2: Sort and Compare

# we will make use of the fact that even though s1 and s2
# are different, they are anagrams only if they consist of exactly the same characters. So, if we
# begin by sorting each string alphabetically, from a to z, we will end up with the same string if
# the original two strings are anagrams

def anagram_solution2(word_a, word_b):
    word_a_list = list(word_a)
    word_b_list = list(word_b)

    word_a_list.sort()
    word_b_list.sort()

    pos = 0
    matches = True
    while pos < len(word_a_list) and matches:
        if word_a_list[pos] == word_b_list[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches


print(anagram_solution2('abcde', 'edcba'))


# At first glance you may be tempted to think that this algorithm is 𝑂(𝑛), since there is one simple
# iteration to compare the 𝑛 characters after the sorting process. However, the two calls to the
# Python sort method are not without their own cost  so the sorting operations dominate the iteration. In the
# end, this algorithm will have the same order of magnitude as that of the sorting process.

# Solution 4: Count and Compare

# any two anagrams will have the same number of a’s, the same number of b’s, the same number of c’s, and so on.
# In order to decide whether two strings are anagrams, we will first count the number of times
# each character occurs. Since there are 26 possible characters, we can use a list of 26 counters,
# one for each possible character. Each time we see a particular character, we will increment the
# counter at that position. In the end, if the two lists of counters are identical, the strings must be
# anagrams.

def anagram_solution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    still_ok = True

    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False
    return still_ok


print(anagram_solution4('apple', 'pleap'))

# unlike the first solution, none of them
# are nested. The first two iterations used to count the characters are both based on 𝑛. The third
# iteration, comparing the two lists of counts, always takes 26 steps since there are 26 possible
# characters in the strings. Adding it all up gives us 𝑇(𝑛) = 2𝑛 + 26 steps. That is 𝑂(𝑛). We
# have found a linear order of magnitude algorithm for solving this problem

# Before leaving this example, we need to say something about space requirements. Although
# the last solution was able to run in linear time, it could only do so by using additional storage to
# keep the two lists of character counts. In other words, this algorithm sacrificed space in order
# to gain time.
#
# This is a common occurrence. On many occasions you will need to make decisions between
# time and space trade-offs. In this case, the amount of extra space is not significant. However,
# if the underlying alphabet had millions of characters, there would be more concern.
