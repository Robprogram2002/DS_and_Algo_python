from random import randint


class MonkeyGenerator:

    def __init__(self, target: str, alphabet: [str]):
        self._target = target
        self._alphabet = alphabet

    def _generate_sentence(self, best_string):
        if best_string is None:
            sequence = [self._alphabet[randint(0, len(self._alphabet) - 1)] for k in range(len(self._target))]
        else:
            sequence = []
            for k in range(len(self._target)):
                if best_string[k] == self._target[k]:
                    sequence.append(best_string[k])
                else:
                    sequence.append(self._alphabet[randint(0, len(self._alphabet) - 1)])

        return ''.join(sequence)

    def _score_sentence(self, string: str):
        score = 0
        for k in range(len(self._target)):
            if string[k] == self._target[k]:
                score += 1
        return (score / len(self._target)) * 100

    def run_monkey(self, verbose=False, step=20):
        best = [0, None]
        tries = 0
        score = 0
        while score < 99:
            sentence = self._generate_sentence(best[1])
            score = self._score_sentence(sentence)
            tries += 1
            if score > best[0]:
                best = [score, sentence]
            if verbose and tries % 20 == 0:
                # print('the current sequence is :', sentence)
                print('the best result so far: ', best)

        print('the best result so far: ', best)
        print('number of tries: ', tries)


if __name__ == '__main__':
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', ' ']
    monkey1 = MonkeyGenerator("to be or not to be that is the question", abc)
    monkey1.run_monkey(verbose=True)
