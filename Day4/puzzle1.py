"""
Day 4: Giant Squid [PART 1]

The submarine has a bingo subsystem to help passengers (currently, you and
the giant squid) pass the time. It automatically generates a random order in
which to draw numbers and a random set of boards (your puzzle input).

To guarantee victory against the giant squid, figure out which board will
win first.

Question: What will your final score be if you choose that board?
"""


def get_call_numbers(filepath: str = "Day4/day4-input.txt") -> list[int]:
    """Returns an integer generated from the collection of numbers called
    during the bingo game.

    Returns
    -------
    int
        The next number called during the bingo game.
    """
    with open(filepath, 'r') as file:
        # Read only the first line:
        first_line = file.readlines(1)
        return [int(x) for x in first_line[0].split(',')]


def get_bingo_cards(filepath: str = "Day4/day4-input.txt") -> list[list[int]]:
    """Returns a list of lists representing rows and numbers on the bingo
    card.

    Returns
    -------
    list[list[int]]
        A list representation of the bingo card rows and their numbers.
    """
    with open(filepath, 'r') as file:
        # Read only the second line:
        read_lines = file.readlines()[2:]
        all_boards = []
        board = []
        for line in read_lines:
            # [CASE] Blank line:
            if line == '\n':
                all_boards.append(board)
                board = []

            # [CASE]: Line with numbers:
            else:
                row = [int(x) for x in line.split()]
                board.append(row)

        # Append last line:
        all_boards.append(board)

        return all_boards


class BingoBoard:
    """A class representing a bingo board. """

    def __init__(self, identifier: int, card_rows: list[list[int]]):
        """Initializes a bingo board with the given card rows. """

        # An identifier for the bingo board:
        self.id = identifier
        # A list of lists representing the rows of the bingo board:
        self.card_rows: list[list[int]] = card_rows
        # Determine the card columns:
        self.card_cols: list[list[int]] = self._find_card_columns()
        # A list of numbers on the card that haven't been called yet:
        self.unmarked_numbers: list[int] = self._init_unmarked_nums()
        # A list of numbers that have been called on the board:
        self.marked_numbers: list[int] = []
        # Create a dict for tracking hits per row + column:
        self.hits_tracker: dict = {'rows': [0, 0, 0, 0, 0],
                                   'columns': [0, 0, 0, 0, 0]}

    def play_bingo_round(self, call_number: int) -> bool:
        """Plays a round of bingo, marking the given number on the board.
        Returns True if the round has won, False otherwise.
        """
        # Check if the called number is on the board:
        if call_number in self.unmarked_numbers:
            # Mark the number on the board:
            self.marked_numbers.append(call_number)
            self.unmarked_numbers.remove(call_number)

            # Find the row and column of the called number:
            _coords = self._find_number_coordinates(call_number)

            # Update the hits tracker:
            self.hits_tracker['rows'][_coords[0]] += 1
            self.hits_tracker['columns'][_coords[1]] += 1

        # Check if the round has won:
        return self._test_win_condition()

    def calculate_winning_score(self, last_call_number: int) -> int:
        """Calculates the winning score given the last call number. """
        return last_call_number * sum(self.unmarked_numbers)

    def _test_win_condition(self) -> bool:
        """Used to check whether the bingo card has won the game, i.e. all if
        a row or column have been marked. """
        _hits = self.hits_tracker
        # Check if any rows are all marked:
        for count in _hits['rows']:
            if count == 5:
                return True
        # Check if any columns are all marked:
        for count in _hits['columns']:
            if count == 5:
                return True
        return False

    def _find_number_coordinates(self, call_number: int) -> tuple:
        """Used to find the coordinates of the given number on the board.
        Returns a tuple of the (row, column) coordinates of the number.
        """
        for row_i in range(5):
            for col_i in range(5):
                if self.card_rows[row_i][col_i] == call_number:
                    return (row_i, col_i)
        return None

    def _find_card_columns(self) -> list[list[int]]:
        """Used to construct the card columns from the card rows. """
        _rows = self.card_rows
        _cols = []

        for col_i in range(5):
            col = []
            for row_i in range(5):
                col.append(_rows[row_i][col_i])
            _cols.append(col)

        return _cols

    def _init_unmarked_nums(self) -> list[int]:
        """Used to initialize a list of all the unmarked numbers on the
        board. """
        _nums_on_card = []
        for row in self.card_rows:
            _nums_on_card.extend(row)
        return _nums_on_card

    def __str__(self) -> None:
        """Provides a string representation of the bingo board. """
        print("Bingo Board: " + str(self.card_rows))


# ------------------------ CONSTANTS ------------------------ #
CALL_NUMBERS = get_call_numbers()
BINGO_CARD_DATA = get_bingo_cards()
ALL_BINGO_BOARDS = [BingoBoard(i+1, card)
                    for i, card in enumerate(BINGO_CARD_DATA)]

# ----------------------------------------------------------- #


def simulate_bingo_game(num_rounds: int) -> int:
    """Simulates the bingo game by pulling from called numbers and applying
    marks to the appropriate bingo boards. Returns the final score if a board
    has won, else zero.
    """
    # Some data validation:
    if num_rounds < 1 or num_rounds > len(CALL_NUMBERS):
        raise ValueError(
            f"Number of rounds must be between 1 and {len(CALL_NUMBERS)}."
        )

    # Track the called numbers:
    called_numbers = []

    for i, called_num in enumerate(CALL_NUMBERS[:num_rounds]):
        # Append the called number to the list of called numbers:
        called_numbers.append(called_num)

        # Play the round on each board:
        for board in ALL_BINGO_BOARDS:
            i_won = board.play_bingo_round(called_num)
            # [CASE] Board has won -> return the final score:
            if i_won:
                score = board.calculate_winning_score(called_num)
                # print(f"\n*** WINNER! WINNER! WINNER! Score: {score} ***\n")
                # print(f"ID: {board.id}")
                for row in board.card_rows:
                    print(row)
                return score

    return 0


# Print our answer to the console:
print("\nDAY 4\n-----")
print("Part 1:")

winner = simulate_bingo_game(27)
print("Winning Score:", winner)
