"""
Assignment 2: Sudoku Puzzle
==============================
This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

=== Module Description ===
This module contains the class required to solve sudoku puzzles.
"""

from __future__ import annotations
from typing import List, Set, Union, Any
from puzzle import Puzzle


class SudokuPuzzle(Puzzle):
    """
    A sudoku puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, n: int, symbols: List[List[str]], symbol_set: Set[str]):
        """
        Create a new nxn SudokuPuzzle with symbols
        from symbol_set already selected.

        Note:
            Grid symbols are represented as letters or numerals
            The empty space is represented as a "*"

        Preconditions:
        - n is a positive integer, n > 0
        - there are n symbols in the given symbol_set
        - there are n lists in symbols, and each list has n strings
        """
        # Private attributes
        # _n
        #   The number of rows/columns in this puzzle's grid
        # _symbols
        #   All the symbols filled in so far in this puzzle; each sublist
        #   represents one row of symbols filled in
        # _symbol_set
        #   The set of all symbols that each row/column/subsquare must have
        #   exactly one of, for this puzzle to be solved
        _n: int
        _symbols: List[List[str]]
        _symbol_set: Set[str]

        self._n, self._symbols, self._symbol_set = n, symbols, symbol_set

    def __eq__(self, other: Union[SudokuPuzzle, Any]) -> bool:
        """
        Return whether this SudokuPuzzle is equivalent to the <other>.

        >>> r1 = ["A", "B", "C", "D"]
        >>> r2 = ["D", "C", "B", "A"]
        >>> r3 = ["*", "D", "*", "*"]
        >>> r4 = ["*", "*", "*", "*"]
        >>> s1 = SudokuPuzzle(4, [r1, r2, r3, r4], {"A", "B", "C", "D"})
        >>> r1_2 = ["A", "B", "C", "D"]
        >>> r2_2 = ["D", "C", "B", "A"]
        >>> r3_2 = ["*", "D", "*", "*"]
        >>> r4_2 = ["*", "*", "*", "*"]
        >>> s2 = SudokuPuzzle(4, [r1_2, r2_2, r3_2, r4_2], {"A", "B", "C", "D"})
        >>> s1.__eq__(s2)
        True
        >>> r1_3 = ["A", "B", "C", "D"]
        >>> r2_3 = ["D", "C", "B", "A"]
        >>> r3_3 = ["*", "D", "*", "*"]
        >>> r4_3 = ["*", "A", "*", "*"]
        >>> s3 = SudokuPuzzle(4, [r1_3, r2_3, r3_3, r4_3], {"A", "B", "C", "D"})
        >>> s1.__eq__(s3)
        False
        """

        return (type(other) == type(self) and
                self._n == other._n and self._symbols == other._symbols and
                self._symbol_set == other._symbol_set)

    def __str__(self) -> str:
        """
        Return a human-readable string representation of this SudokuPuzzle.

        >>> r1 = ["A", "B", "C", "D"]
        >>> r2 = ["D", "C", "B", "A"]
        >>> r3 = ["*", "D", "*", "*"]
        >>> r4 = ["*", "*", "*", "*"]
        >>> s = SudokuPuzzle(4, [r1, r2, r3, r4], {"A", "B", "C", "D"})
        >>> print(s)
        AB|CD
        DC|BA
        -----
        *D|**
        **|**
        """

        def row_pickets(row: List[str]) -> str:
            """
            A nested helper function for __str__.
            Return string of characters in row with | divider
            between groups of sqrt(n).
            """

            string_list = []
            r = round(self._n ** (1 / 2))
            for i in range(self._n):
                if i > 0 and i % r == 0:
                    string_list.append("|")
                string_list.append(row[i])
            return "".join(string_list)

        s = ''
        num = round(self._n ** (1 / 2))
        div = "-" * (self._n + 1) + "\n"
        for i in range(len(self._symbols)):
            if i > 0 and i % num == 0:
                s += div
            s += row_pickets(self._symbols[i])
            s += "\n"
        return s.rstrip()

    def is_solved(self) -> bool:
        """
        Return whether this SudokuPuzzle is solved.

        >>> r1 = ["A", "B", "C", "D"]
        >>> r2 = ["C", "D", "A", "B"]
        >>> r3 = ["B", "A", "D", "C"]
        >>> r4 = ["D", "C", "B", "A"]
        >>> grid = [r1, r2, r3, r4]
        >>> s = SudokuPuzzle(4, grid, {"A", "B", "C", "D"})
        >>> s.is_solved()
        True
        >>> r3[1] = "D"
        >>> r3[2] = "A"
        >>> grid = [r1, r2, r3, r4]
        >>> s = SudokuPuzzle(4, grid, {"A", "B", "C", "D"})
        >>> s.is_solved()
        False
        """

        # temporary variables to give convenient names to each attribute
        n, symbols = self._n, self._symbols

        # check that there is no "*" left and
        # all rows, column, subsquares have correct symbols
        return (not any("*" in row for row in symbols)) \
               and all([(self._row_set(i) == self._symbol_set and
                      self._column_set(j) == self._symbol_set and
                      self._subsquare_set(i, j) ==
                      self._symbol_set) for i in range(n) for j in range(n)])

    def extensions(self) -> List[SudokuPuzzle]:
        """
        Return list of extensions of SudokuPuzzle self.

        >>> r1 = ["A", "B", "C", "D"]
        >>> r2 = ["C", "D", "A", "B"]
        >>> r3 = ["B", "A", "D", "C"]
        >>> r4 = ["D", "C", "B", "*"]
        >>> grid = [r1, r2, r3, r4]
        >>> s = SudokuPuzzle(4, grid, {"A", "B", "C", "D"})
        >>> L1 = list(s.extensions())
        >>> grid[-1][-1] = "A"
        >>> L2 = [SudokuPuzzle(4, grid, {"A", "B", "C", "D"})]
        >>> len(L1) == len(L2)
        True
        >>> all([s in L2 for s in L1])
        True
        >>> all([s in L1 for s in L2])
        True
        """

        # temporary variables to give convenient names to each attribute
        symbols, symbol_set, n = self._symbols, self._symbol_set, self._n
        if not any("*" in row for row in symbols):
            return []
        else:
            # get position of first empty position
            r = 0  # row with first empty position
            while "*" not in symbols[r]:
                r += 1
            c = symbols[r].index("*")  # column with first empty position

            # allowed symbols at position (r, c)
            # A | B == A.union(B)
            allowed_symbols = (self._symbol_set -
                               (self._row_set(r) |
                                self._column_set(c) |
                                self._subsquare_set(r, c)))

            # list of SudokuPuzzles with each legal digit at position i
            return_lst = []
            for symbol in allowed_symbols:
                new_puzzle = SudokuPuzzle(n, symbols[:r] + \
                                          [symbols[r][:c] + [symbol] + symbols[r][c+1:]] + \
                                          symbols[r+1:], symbol_set)
                return_lst.append(new_puzzle)
            return return_lst

    def fail_fast(self) -> bool:
        """
        Return whether some unfilled position has no allowable symbols
        remaining to choose from, and hence this SudokoPuzzle can never
        be completed.

        >>> s = SudokuPuzzle(4, \
        [["A", "B", "C", "D"], \
        ["C", "D", "*", "*"], \
        ["*", "*", "*", "*"], \
        ["*", "*", "*", "*"]], {"A", "B", "C", "D"})
        >>> s.fail_fast()
        False
        >>> s = SudokuPuzzle(4, \
        [["B", "D", "A", "C"], \
        ["C", "A", "B", "D"], \
        ["A", "B", "*", "*"], \
        ["*", "*", "*", "*"]], {"A", "B", "C", "D"})
        >>> s.fail_fast()
        True
        """
        symbols, symbol_set = self._symbols, self._symbol_set
        for i in range(len(symbols)):
            for j in range(len(symbols[i])):
                if symbols[i][j] == '*':
                    set1, set2, set3 = self._row_set(i), self._column_set(j), self._subsquare_set(i, j)
                    big = set1 | set2 | set3
                    big.remove('*')
                    if big == symbol_set:
                        return True
        return False
       
    # some private helper methods (note the private docstrings for each of them)

    def _row_set(self, r: int) -> Set[str]:
        # Return set of symbols in row of SudokuPuzzle self's symbols
        # where position m occurs.

        # set of elements from symbols[r]
        return set(self._symbols[r])

    def _column_set(self, c: int) -> Set[str]:
        # Return set of symbols in column of SudokuPuzzle self's symbols
        # where position m occurs.

        # set of elements from symbols[0][c], symbols[1][c],
        # ... symbols[len(symbols)-1][c]
        return set([row[c] for row in self._symbols])

    def _subsquare_set(self, r: int, c: int) -> Set[str]:
        # Return set of symbols in subsquare of SudokuPuzzle self's symbols
        # where position m occurs.

        # convenient names
        n, symbols = self._n, self._symbols
        # length of subsquares
        ss = round(n ** (1 / 2))
        # upper-left position of m's subsquare
        ul_row = (r // ss) * ss
        ul_col = (c // ss) * ss

        subsquare_symbols = []
        for i in range(ss):
            for j in range(ss):
                subsquare_symbols.append(symbols[ul_row + i][ul_col + j])
        return set(subsquare_symbols)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Comment out the code below as you solve necessary parts of the assignment
    """
    s = SudokuPuzzle(9,
                     [["*", "*", "*", "7", "*", "8", "*", "1", "*"],
                      ["*", "*", "7", "*", "9", "*", "*", "*", "6"],
                      ["9", "*", "3", "1", "*", "*", "*", "*", "*"],
                      ["3", "5", "*", "8", "*", "*", "6", "*", "1"],
                      ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
                      ["1", "*", "6", "*", "*", "9", "*", "4", "8"],
                      ["*", "*", "*", "*", "*", "1", "2", "*", "7"],
                      ["8", "*", "*", "*", "7", "*", "4", "*", "*"],
                      ["*", "6", "*", "3", "*", "2", "*", "*", "*"]],
                     {"1", "2", "3", "4", "5", "6", "7", "8", "9"})
    print("solving sudoku from July 9 2015 Star... \n\n{}\n\n".format(s))
    # I test when we use depth first search it will take about 0 ~ 5 seconds
    # to solve for these three puzzles
    from time import time
    from puzzle_tools import depth_first_solve

    start = time()
    sol = depth_first_solve(s)  # Using depth first solve to find the solution
    print(sol)  # print out the a path from PuzzleNode(puzzle) to a PuzzleNode containing a solution
    # if there is no solution for that, then just print None
    while sol.children:
        sol = sol.children[0]  # a loop that make the variable sol point to the solution of this puzzle
    end = time()
    print("time to solve 9x9 using depth_first: "
          "{} seconds\n".format(end - start))  # print out the time to solve this puzzle
    print(sol)  # print the final solution for this puzzle

    s = SudokuPuzzle(9,
                     [["*", "*", "*", "9", "*", "2", "*", "*", "*"],
                      ["*", "9", "1", "*", "*", "*", "6", "3", "*"],
                      ["*", "3", "*", "*", "7", "*", "*", "8", "*"],
                      ["3", "*", "*", "*", "*", "*", "*", "*", "8"],
                      ["*", "*", "9", "*", "*", "*", "2", "*", "*"],
                      ["5", "*", "*", "*", "*", "*", "*", "*", "7"],
                      ["*", "7", "*", "*", "8", "*", "*", "4", "*"],
                      ["*", "4", "5", "*", "*", "*", "8", "1", "*"],
                      ["*", "*", "*", "3", "*", "6", "*", "*", "*"]],
                     {"1", "2", "3", "4", "5", "6", "7", "8", "9"})

    print("solving 3-star sudoku from \"That's Puzzling\","
          "November 14th 2015\n\n{}\n\n".format(s))
    start = time()
    sol = depth_first_solve(s)  # Using depth first solve to find the solution
    while sol.children:
        sol = sol.children[0]  # a loop that make the variable sol point to the solution of this puzzle
    end = time()
    print("time to solve 9x9 using depth_first: {} seconds\n".format(
        end - start))
    # print the final solution for this puzzle
    print(sol)

    s = SudokuPuzzle(9,
                     [["5", "6", "*", "*", "*", "7", "*", "*", "9"],
                      ["*", "7", "*", "*", "4", "8", "*", "3", "1"],
                      ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
                      ["4", "3", "*", "*", "*", "*", "*", "*", "*"],
                      ["*", "8", "*", "*", "*", "*", "*", "9", "*"],
                      ["*", "*", "*", "*", "*", "*", "*", "2", "6"],
                      ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
                      ["1", "9", "*", "3", "6", "*", "*", "7", "*"],
                      ["7", "*", "*", "1", "*", "*", "*", "4", "2"]],
                     {"1", "2", "3", "4", "5", "6", "7", "8", "9"})

    print(
        "solving 4-star sudoku from \"That's Puzzling\", "
        "November 14th 2015\n\n{}\n\n".format(
            s))
    start = time()
    sol = depth_first_solve(s)  # Using depth first solve to find the solution
    while sol.children:
        sol = sol.children[0]  # a loop that make the variable sol point to the solution of this puzzle
    end = time()
    print("time to solve 9x9 using depth_first: {} seconds\n".format(
        end - start))
    print(sol)
    """
