from TicTacToe.Solver import Solver

import pytest

@pytest.fixture
def solver():
    return Solver()

@pytest.fixture
def example_board():
    return [[0, 1, 0],[1, 1, 0],[0, 1, 0]]

@pytest.fixture
def invalid_board():
    return [[0, 1, 0],[1, 0, 0],[0, 1, 0]]

@pytest.fixture
def board_valid_row():
    return [[0, 0, 0],[1, 1, 1],[0, 0, 0]]

@pytest.fixture
def board_no_valid_row():
    return invalid_board()

@pytest.fixture
def board_valid_column():
    return [[0, 1, 0],[0, 1, 0],[0, 1, 0]]

@pytest.fixture
def board_no_valid_column():
    return invalid_board()

@pytest.fixture
def board_valid_diagonal():
    return [[1, 0, 0],[0, 1, 0],[0, 0, 1]]

@pytest.fixture
def board_no_valid_diagonal():
    return invalid_board()

def test_solver_on_example_board(solver, example_board):
    assert solver.solve(example_board)