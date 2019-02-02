from TicTacToe.Solver import Solver

import pytest

def test_solver_on_example_board(solver, example_board):
    result = solver._getWinner(example_board)

    assert result == 1

def test_solver_returning_player_string_given_valid_board(solver, example_board):
    assert solver.getWinner(example_board) == "X"

def test_solver_returning_tie_given_invalid_board(solver, invalid_board):
    assert solver.getWinner(invalid_board) == "<tie>"

def test_column_solver_on_valid_columns(solver, board_valid_column):
    result = solver._column_winner(board_valid_column)

    assert result == 0

def test_column_solver_on_invalid_columns(solver, invalid_board):
    result = solver._column_winner(invalid_board) 

    assert not result

def test_row_solver_on_valid_rows(solver, board_valid_row):
    result = solver._row_winner(board_valid_row)

    assert result == 1

def test_row_solver_on_invalid_rows(solver, invalid_board):
    result = solver._row_winner(invalid_board) 

    assert not result

def test_diagonal_solver_on_valid_diagonals(solver, board_valid_diagonal):
    result = solver._diagonal_winner(board_valid_diagonal)

    assert result == 1

def test_diagonal_solver_on_invalid_diagonals(solver, invalid_board):
    result = solver._diagonal_winner(invalid_board) 

    assert not result

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
    return [[1, 0, 0],[1, 1, 1],[0, 1, 0]]

@pytest.fixture
def board_no_valid_row():
    return invalid_board()

@pytest.fixture
def board_valid_column():
    return [[0, 1, 0],[0, 0, 0],[0, 1, 0]]

@pytest.fixture
def board_no_valid_column():
    return invalid_board()

@pytest.fixture
def board_valid_diagonal():
    return [[1, 0, 0],[0, 1, 0],[0, 0, 1]]

@pytest.fixture
def board_no_valid_diagonal():
    return invalid_board()