"""
Day 4: Giant Squid [PART 2]

Figure out which board will win last.

Question: Once it wins, what would its final score be?
"""
from puzzle1 import ALL_BINGO_BOARDS, CALL_NUMBERS


def simulate_win_last(num_rounds: int = 27) -> int:
    """Simulates the bingo game by pulling from called numbers and applying
    marks to the appropriate bingo boards. Once a card has won it is removed
    and play continues with the remaining cards.

    The objective is to be the last bingo board to win the game. Once the last
    winner is found, we return their score.
    """
    # Some data validation:
    if num_rounds < 1 or num_rounds > len(CALL_NUMBERS):
        raise ValueError(
            f"Number of rounds must be between 1 and {len(CALL_NUMBERS)}."
        )

    # Track the called numbers:
    called_numbers = []
    # Create a copy of the list of bingo boards:
    boards_playing = ALL_BINGO_BOARDS.copy()

    for called_num in CALL_NUMBERS[:num_rounds]:
        # Append the called number to the list of called numbers:
        called_numbers.append(called_num)

        # Play the round on each board:
        for index, board in enumerate(boards_playing):
            i_won = board.play_bingo_round(called_num)
            # [CASE] Board has won:
            if i_won:
                # [CASE] Board is the last one to win:
                if len(boards_playing) == 1:
                    for row in board.card_rows:
                        print(row)
                    return board.calculate_winning_score(called_num)

                # [CASE] Board is not last:
                else:
                    del boards_playing[index]

    return 0


# Find our answer...
# for r in range(1, 100):
#     score = simulate_win_last(r)

#     if score != 0:
#         print(score)
#         break
#     else:
#         print(f"Round {r} -- No winner.")


# Print our results to the console:
print("Part 2:")

score = simulate_win_last(84)
print(f"Last winning board! Score: {score}")
