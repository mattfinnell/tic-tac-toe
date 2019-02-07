# Tic Tac Toe Solver

## Installing
NOTE: I'm using [Pipenv](https://pipenv.readthedocs.io/en/latest/) to contain the project and [pytest](https://docs.pytest.org/en/latest/) for running test cases.

```sh
git clone https://github.com/mattfinnell/tic-tac-toe
cd tic-tac-toe
pipenv install
```

## Solution
The algorithm for the solution is found in `TicTacToe/Solver.py` and is the `Solver.getWinner(game_board)` method.

I recommend adding your own custom tests within `tests/test_tic_tac_toe.py` of the following form...

```python 
def test_my_custom_case(solver):
    input_board = [[0,0,0], [0,0,0], [0,0,0]]

    assert solver.getWinner(input_board) == "O"
```

Or you can import the solver within your own file (within the project) and run it however you please. The following should be enough for getting started.

```python
from TicTacToe.Solver import Solver

# Construct a new solver object
solver = Solver() 

# Construct a sample gameboard
game_board = [[0,0,0], [0,0,0], [0,0,0]]

# Evaluate the gameboard
result = solver.getWinner(game_board)

# ... whatever else
```

## Running Tests

```
pipenv run python -m pytest
```