"""
Assignment 2: Automatic Puzzle Solver
==============================
This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

=== Module Description ===
This module contains the class required to solve word ladder puzzles.
"""

from __future__ import annotations
from typing import Set, Union
from puzzle import Puzzle


class WordLadderPuzzle(Puzzle):
    """
    A word-ladder puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, from_word: str, to_word: str, ws: Set[str]) -> None:
        """
        Create a new word-ladder puzzle with the aim of stepping
        from from_word to to_word using words in ws, changing one
        character at each step.
        """
        # Private Attributes
        # _from_word
        #   the initial word the puzzle begins with
        # _to_word
        #   the goal word the puzzle wants to change to
        # _word_set
        #   the set of all words that are possible valid words to change into
        # _chars
        #   a string of all possible characters that a word may consist of

        _from_word: str
        _to_word: str
        _word_set: Set[str]
        _chars: str

        (self._from_word, self._to_word, self._word_set) = (from_word,
                                                            to_word, ws)
        # set of characters to use for 1-character changes
        self._chars = "abcdefghijklmnopqrstuvwxyz"

    def __eq__(self, other: Union[word_ladder_puzzle, Any]) -> bool:
        """
        return whether this wordladderPuzzle is equivalent to the <other>.
        """
        return (type(other) == type(self) and
                self._from_word == other._from_word and
                self._word_set == other._word_set and
                self._to_word == other._to_word)

    def extensions(self) -> List[word_ladder_puzzzle]:
        """
        Return list of extensions of word_ladder puzzle self.
        """
        lst = []
        for i in range(len(self._from_word)):
            for letter2 in self._chars:
                word = self._from_word[:i] + letter2 + self._from_word[i+1:]
                if word in self._word_set and word != self._from_word:
                    lst.append(WordLadderPuzzle(word, self._to_word, self._word_set))
        return lst

    def is_solved(self) -> bool:
        """
        Return whether this word ladder puzzle is solved.
        """
        return self._from_word == self._to_word

    def __str__(self) -> str:
        """
        Return a human-readable string representation of this word_ladder_puzzle.
        """
        return '{} → {}'.format(self._from_word, self._to_word)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # Comment out the code below as you solve necessary parts of the assignment
    """
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    with open("words", "r") as words:
        word_set = set(words.read().split())
    # read file and create the word set. It has 99171 words in word set. omg.
    w = WordLadderPuzzle("same", "cost", word_set)
    start = time()
    sol = breadth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    # for breadth first solve, it will give you the shortest or most optimal path
    # leads to the solution.it's searching broadly in a level order. It will go through each extension and
    # check if the extension is solved. The path is much shorter than the depth first solve.
    # It just needs 4 steps towards the solution.
    start = time()
    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    # depth first solve will not give you the shortest path to the solution because
    # it's searching deeply. So it will give the the most left side solution in a
    # tree. So it will take roundabout ways. Probably the most optimal solution is not that branch
    # for the wordladder Puzzle the depth first search is slower than breadth first search
    # it needs to take much more steps towards the solution compared to breadth first solve.
    """


