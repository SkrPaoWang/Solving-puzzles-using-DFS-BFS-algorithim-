"""
Assignment 2: Automatic Puzzle Solver
==============================
This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

=== Module Description ===
This module contains the class required to solve grid peg solitaire puzzles.
"""
from __future__ import annotations
from typing import List, Set, Union, Any
from puzzle import Puzzle


class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker: List[List[str]], marker_set: Set[str]):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        Note: The symbol "#" is for unused, "*" is for peg, "." is for empty

        Precondition:
        - marker is a non-empty list of lists representing an m x n grid
        - the strings in marker are all a valid string from marker_set
        """
        # Private Attributes
        # _marker
        #   the m x n solitaire grid with some pegs, spaces and unused spots
        # _marker_set
        #   the possible symbols on the grid, representing different spots

        _marker: str
        _marker_set: str
        self._marker, self._marker_set = marker, marker_set

    def __eq__(self, other: Union[GridPegSolitairePuzzle, Any]) -> bool:
        """
        Return whether this gridpegsolitairepuzzle is equivalent to the <other>.

         >>> grid = [["*", "*", "*", "*", "*"],["*", "*", ".", "*", "*"],["*", "*", "*", "*", "*"]]

        >>> grid2 = [["*", "*", "*", "*", "*"],["*", "*", ".", "*", "*"],["*", "*", "*", "*", "*"]]
        >>> gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> gpsp2 = GridPegSolitairePuzzle(grid2, {"*", ".", "#"})
        >>> gpsp.__eq__(gpsp2)
        True
        >>> grid3 = []
        >>> gpsp3 = GridPegSolitairePuzzle(grid3, {"*", ".", "#"})
        >>> gpsp.__eq__(gpsp3)
        False
        """
        return type(other) == type(self) and self._marker == other._marker and self._marker_set == other._marker_set

    def __str__(self) -> str:
        """
        Return a human-readable string representation of this grid_peg_solitaire_puzzle.

        >>> grid = [["*", "*", "*", "*", "*"],["*", ".", "*", "*", "*"], ["*", "*", "*", "*", "*"]]
        >>> gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> print(gpsp)
        ●●●●●
        ●○●●●
        ●●●●●
        """
        s = ''
        for i in range(len(self._marker)):
            for j in range(len(self._marker[i])):
                if self._marker[i][j] == '*':
                    s += '●'
                elif self._marker[i][j] == '.':
                    s += '○'
                elif self._marker[i][j] == '#':
                    s += ' '
            s += '\n'
        return s.rstrip()

    def extensions(self) -> List[GridPegSolitairePuzzle]:
        """
        Return list of extensions of grid_peg_solitaire self.
        """
        lst = []
        for i in range(len(self._marker)):
            for j in range(len(self._marker[i])):
                if i <= len(self._marker)-3 and self._marker[i][j] == '*' \
                        and self._marker[i+1][j] == '*' and self._marker[i+2][j] == ".":
                    grid1 = [lst[:] for lst in self._marker]
                    grid1[i+2][j], grid1[i+1][j], grid1[i][j] = '*', '.', '.'
                    lst.append(GridPegSolitairePuzzle(grid1, self._marker_set))
                elif i > 1 and self._marker[i][j] == '*' \
                        and self._marker[i-1][j] == '*' and self._marker[i-2][j] == ".":
                    grid2 = [lst[:] for lst in self._marker]
                    grid2[i-2][j], grid2[i-1][j], grid2[i][j] = '*', '.', '.'
                    lst.append(GridPegSolitairePuzzle(grid2, self._marker_set))
                elif j <= len(self._marker[0])-3 and self._marker[i][j] == '*' \
                        and self._marker[i][j+1] == '*' and self._marker[i][j+2] == '.':
                    grid3 = [lst[:] for lst in self._marker]
                    grid3[i][j+2], grid3[i][j+1], grid3[i][j] = '*', '.', '.'
                    lst.append(GridPegSolitairePuzzle(grid3, self._marker_set))
                elif j > 1 and self._marker[i][j] == '*' and\
                        self._marker[i][j-1] == '*' and self._marker[i][j-2] == '.':
                    grid4 = [lst[:] for lst in self._marker]
                    grid4[i][j-2], grid4[i][j-1], grid4[i][j] = '*', '.', '.'
                    lst.append(GridPegSolitairePuzzle(grid4, self._marker_set))
        return lst

    def is_solved(self) -> bool:
        """
        Return whether this grid_peg_solitaire_puzzle is solved.
        """
        a = sum(ch.count('*') for ch in self._marker)
        return a == 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    from puzzle_tools import depth_first_solve
    grid = [["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"], ["*", "*", ".", "*", "*"], ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    import time
    start = time.time()
    solution = depth_first_solve(gpsp)
    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))



