# Modify the given code so that the final list only contains a single copy of each letter.
def exercise1():
    word_list = ['cat', 'dog', 'rabbit']
    letter_list = []
    for a_word in word_list:
        for a_letter in a_word:
            if a_letter not in letter_list:
                letter_list.append(a_letter)

    return letter_list


def exercise1_v2():
    word_list = ["cat", 'dog', 'rabbit']
    all_letters = [letter for word in word_list for letter in word]
    return list(set(all_letters))


# expected to be: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
print(exercise1())
print(exercise1_v2())
