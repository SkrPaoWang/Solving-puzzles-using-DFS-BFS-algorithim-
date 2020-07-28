"""
Assignment 2: Sudoku Puzzle
==============================
This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

=== Module Description ===
This module contains the abstract Puzzle class.
"""

from __future__ import annotations

class Puzzle:
    """"
    Snapshot of a full-information puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def fail_fast(self) -> bool:
        """
        Return True iff Puzzle self can never be extended to a solution.

        Override this in a subclass where you can determine early that
        this Puzzle cann't be solved.
        """
        
        return False

    def is_solved(self) -> bool:
        """
        Return True iff Puzzle self is solved.

        This is an abstract method that must be implemented
        in a subclass.

        @type self: Puzzle
        @rtype: bool
        """
        
        raise NotImplementedError

    def extensions(self) -> Puzzle:
        """
        Return list of legal extensions of Puzzle self.

        This is an abstract method that must be implemented
        in a subclass.
        """
        
        raise NotImplementedError
