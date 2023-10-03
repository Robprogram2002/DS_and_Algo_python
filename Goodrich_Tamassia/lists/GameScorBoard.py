from datetime import date


# Objective : Storing a sequence of high score entries for a video game.
# we consider what information to include in an object representing a high score entry.

class GameEntry:
    """Represents one entry of a list of high scores."""

    def __init__(self, name, score, score_date, tries):
        """Create an entry with given name and score."""
        if not isinstance(score, (int, float)):
            raise TypeError('score must be a numeric value')
        if not isinstance(name, str):
            raise TypeError('name must be a string')
        if not isinstance(score_date, date):
            raise TypeError('third argument must be of date type')
        self._score = score
        self._name = name
        self._date = score_date
        self._tries = tries

    def get_score(self):
        return self._score

    def get_name(self):
        return self._name

    def get_date(self):
        return self._date

    def get_tries(self):
        return self._tries

    def __str__(self):
        return '({0}, {1}, {2}, {3})'.format(self._name, self._score, self._date.isoformat(), self._tries)


# A scoreboard is limited to a certain number of high scores that can be saved; once that
# limit is reached, a new score only qualifies for the scoreboard if it is strictly higher
# than the lowest “high score” on the board


class Scoreboard:
    """Fixed-length sequence of high scores in increasing order."""

    def __init__(self, capacity=10):
        """Initialize scoreboard with given maximum capacity.

        All entries are initially None.
        """
        self._board = [None] * capacity  # reserve space for future scores
        self._n = 0  # number of actual entries

    def __getitem__(self, k):
        """Return entry at index k."""
        return self._board[k]

    def __str__(self):
        """Return string representation of the high score list."""
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def _rearrange(self):
        for k in range(self._n, 1, -1):
            if self._board[k - 1].get_score() > self._board[k - 2].get_score():
                self._board[k - 2], self._board[k - 1] = self._board[k - 1], self._board[k - 2]
            else:
                break

    def add(self, item: GameEntry):
        """Consider adding entry to high scores."""
        if self._n == len(self._board):
            # the list is full, we must check if the score is grater than the lower score in the list
            if item.get_score() > self._board[-1].get_score():
                self._board[-1] = item
                self._rearrange()
        else:
            # since the list is not full we can add the new score regardless of its value
            self._board[self._n] = item
            self._n += 1
            self._rearrange()

    # Another way of implement the same method
    # def add(self, entry):
    #     """Consider adding entry to high scores."""
    #     score = entry.get_score()
    #
    #     # Does new entry qualify as a high score?
    #     # answer is yes if board not full or score is higher than last entry
    #     good = self._n < len(self._board) or score > self._board[-1].get_score()
    #
    #     if good:
    #         if self._n < len(self._board):  # no score drops from list
    #             self._n += 1  # so overall number increases
    #
    #         # shift lower scores rightward to make room for new entry
    #         j = self._n - 1
    #         while j > 0 and self._board[j - 1].get_score() < score:
    #             self._board[j] = self._board[j - 1]  # shift entry from j-1 to j
    #             j -= 1  # and decrement j
    #         self._board[j] = entry  # when done, add new entry


if __name__ == '__main__':
    board = Scoreboard(5)
    for e in (
            ('Rob', 750, date(2012, 6, 14), 4), ('Mike', 1105, date(2011, 9, 1), 8),
            ('Rose', 590, date(2002, 10, 12), 2), ('Jill', 740, date(2012, 6, 14), 4),
            ('Jack', 510, date(2012, 6, 14), 4), ('Anna', 660, date(2012, 6, 14), 4),
            ('Paul', 720, date(2012, 6, 14), 4), ('Bob', 400, date(2012, 6, 14), 4),
    ):
        ge = GameEntry(e[0], e[1], e[2], e[3])
        board.add(ge)
        print('After considering {0}, scoreboard is:'.format(ge))
        print(board)
        print()
