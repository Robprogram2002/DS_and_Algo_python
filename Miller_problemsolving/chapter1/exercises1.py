from random import randint


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


def exercise1_v3(data: [str]):
    return list(set(''.join(data)))


# expected to be: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
print(exercise1())
print(exercise1_v2())
print(exercise1_v3(["cat", 'dog', 'rabbit']))

# How long do you think it would take for a Python function to generate just one sentence
# of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”

# The way we will simulate this is to write a function that generates a string that is 27 characters long
# by choosing random letters from the 26 letters in the alphabet plus the space. We will write
# another function that will score each generated string by comparing the randomly generated
# string to the goal.

# A third function will repeatedly call generate and score, then if 100% of the letters are correct
# we are done. If the letters are not correct then we will generate a whole new string. To make
# it easier to follow your program’s progress this third function should print out the best string
# generated so far and its score every 1000 tries.

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z', ' ']

obj = "me thinks it is like a weasel"


def generate_sentence(alphabet: [str], length=27):
    sequence = []
    for k in range(length):
        sequence.append(alphabet[randint(0, len(alphabet) - 1)])
    return ''.join(sequence)


def score_sentence(string: str, target: str):
    score = 0
    for k in range(len(target)):
        if string[k] == target[k]:
            score += 1
    return (score / len(target)) * 100


def monkey():
    best = [0, '']
    tries = 0
    score = 0
    while score < 50:
        sentence = generate_sentence(abc, len(obj))
        score = score_sentence(sentence, obj)
        tries += 1
        if score > best[0]:
            best = [score, sentence]
        if tries % 1000 == 0:
            print('the best result so far: ', best)


# monkey()


# See if you can improve upon the program in the self check by keeping letters that are correct
# and only modifying one character in the best string so far. This is a type of algorithm in the
# class of “hill climbing” algorithms, that is we only keep the result if it is better than the previous
# one

def generate_sentence_v2(best_string, target: str):
    if best_string is None:
        return generate_sentence(abc, len(target))
    else:
        sequence = []
        for k in range(len(target)):
            if best_string[k] == target[k]:
                sequence.append(best_string[k])
            else:
                sequence.append(abc[randint(0, len(abc) - 1)])
        return ''.join(sequence)


def monkey_v2():
    best = [0, None]
    tries = 0
    score = 0
    while score < 99:
        sentence = generate_sentence_v2(best[1], obj)
        score = score_sentence(sentence, obj)
        tries += 1
        if score > best[0]:
            best = [score, sentence]
        if tries % 1000 == 0:
            # print('the current sequence is :', sentence)
            print('the best result so far: ', best)

    print('number of tries: ', tries)
    print('the best result was: ', best[1])


monkey_v2()
