import json
import random

from tabulate import tabulate

chore_list = {}
board = []


def select_random_chore():
    selected_chore = random.choice(chore_list)
    chore_list.remove(selected_chore)
    return selected_chore


def load_chores():
    with open("chores.json") as chore_file:
        chores_json = chore_file.read()
        return json.loads(chores_json)


def setup_board(helpers):
    for helper in helpers:
        board.append({'name': helper, 'chores': []})


def output_board():
    print(tabulate(board))


if __name__ == "__main__":
    staff = ["Jodie", "Pete", "Maya", "Lucy"]
    # print("Staff", staff)
    chore_list = load_chores()
    # print("Chores", chore_list)
    setup_board(staff)
    # print(board)

    while len(chore_list) > 0:
        for row in board:
            row['chores'].append(select_random_chore())
            # print("row", row)

    output_board()