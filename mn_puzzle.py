"""
Assignment 2: Automatic Puzzle Solver
==============================
This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

=== Module Description ===
This module contains the class required to solve mn puzzles.
"""

from __future__ import annotations
from typing import Tuple
from puzzle import Puzzle


class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """
    # Private Attributes
    # _n
    #   the height of the grid
    # _m
    #   the width of the grid
    # _from_grid
    #   the initial grid arrangement this puzzle begins at
    # _to_grid
    #   the goal grid arrangement this puzzle aims to reach
    _n: int
    _m: int
    _from_grid: Tuple
    _to_grid: Tuple

    def __init__(self, from_grid: Tuple, to_grid: Tuple) -> None:
        """
        MNPuzzle in state from_grid, working towards
        state to_grid.

        Note:
            Grid symbols are represented as letters or numerals
            The empty space is represented as a "*"

        Preconditions:
        - both from_grid and to_grid are rectangular m x n grids
        """

        self._n, self._m = len(from_grid), len(from_grid[0])
        self._from_grid, self._to_grid = from_grid, to_grid

    def __str__(self) -> str:
        """
        Return a human-readable string representation of this mn_puzzle.
        """
        s = ''
        for i in range(self._n):
            for j in range(self._m):
                s += self._from_grid[i][j]
                s += ' '
            s += '\n'
        return s.rstrip()

    def __eq__(self, other) -> bool:
        """
        return whether this mnPuzzle is equivalent to the <other>.
        """

        return type(other) == type(self) and self._from_grid == other._from_grid and self._to_grid == other._to_grid

    def extensions(self) -> List[mn_puzzle]:
        """
        Return list of extensions of mn_puzzle puzzle self.
        """
        lst = []
        for i in range(self._n):
            for j in range(self._m):
                if j < self._m - 1 and self._from_grid[i][j+1] == '*':
                    x = [list(a) for a in self._from_grid]
                    x[i][j+1], x[i][j] = x[i][j], x[i][j+1]
                    lst.append(MNPuzzle(tuple([tuple(l) for l in x]), self._to_grid))
                elif j != 0 and self._from_grid[i][j - 1] == '*':
                    x = [list(a) for a in self._from_grid]
                    x[i][j - 1], x[i][j] = x[i][j], x[i][j - 1]
                    lst.append(MNPuzzle(tuple([tuple(l) for l in x]), self._to_grid))
                elif i < self._n - 1 and self._from_grid[i+1][j] == '*':
                    x = [list(a) for a in self._from_grid]
                    x[i+1][j], x[i][j] = x[i][j], x[i+1][j]
                    lst.append(MNPuzzle(tuple([tuple(l) for l in x]), self._to_grid))
                elif i != 0 and self._from_grid[i-1][j] == '*':
                    x = [list(a) for a in self._from_grid]
                    x[i-1][j], x[i][j] = x[i][j], x[i-1][j]
                    lst.append(MNPuzzle(tuple([tuple(l) for l in x]), self._to_grid))
        return lst

    def is_solved(self) -> bool:
        """
        Return whether this mn puzzle is solved.
        """
        return self._from_grid == self._to_grid


if __name__ == "__main__":

    import doctest
    doctest.testmod(verbose=True)
    # Comment out the code below as you solve necessary parts of the assignment
    """
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    start = time()
    solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    end = time()
    print("BFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    # breadth first solve will give you the shortest path to the solution because
    # it's searching broadly in a level order. It will go through each extension and
    # check if the extension is solved.
    start = time()
    solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    end = time()
    print("DFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    # depth first solve will not give you the shortest path to the solution because
    # it's searching deeply. So it will give the the most left side solution in a
    # tree. So it will take roundabout ways. Probably the most optimal solution is not that branch
    # for the MN Puzzle the depth first search is slower than breadth first search
    """



