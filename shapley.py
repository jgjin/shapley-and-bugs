"""Calculate Shapley value."""

import os

from read_input import read_input

from collections import defaultdict


def calc_shapley(input_dict):
    counter = defaultdict(int)

    for bugs in input_dict.values():
        for bug in bugs:
            counter[bug] += 1

    for test_case, bugs in sorted(
            input_dict.items(),
            key=lambda tup: sum([1 / counter[bug] for bug in tup[1]]),
            reverse=True,
    ):
        shapley_value = round(
            sum([1 / counter[bug] for bug in bugs]),
            2,
        )

        print(f"For {test_case}, shapley value={shapley_value}:")
        print("\t" +
              ",".join([f"{bug}={round(1 / counter[bug], 3)}"
                        for bug in bugs]))

    print("-" * 12)

    for letter in range(26):
        bug = chr(ord('A') + letter)
        print(f"Bug {bug} caught by:")
        print(", ".join([
            test_case for test_case, bugs in input_dict.items() if bug in bugs
        ]))
    for letter in range(46 - 26):
        bug = chr(ord('a') + letter)
        print(f"Bug {bug} caught by:")
        print(", ".join([
            test_case for test_case, bugs in input_dict.items() if bug in bugs
        ]))

    print("-" * 12)

    for letter in range(26):
        bug = chr(ord('A') + letter)
        if len([
                test_case for test_case, bugs in input_dict.items()
                if bug in bugs
        ]) == 0:
            print(f"Bug {bug} not caught!")
    for letter in range(46 - 26):
        bug = chr(ord('a') + letter)
        if len([
                test_case for test_case, bugs in input_dict.items()
                if bug in bugs
        ]) == 0:
            print(f"Bug {bug} not caught!")


if __name__ == "__main__":
    input_file_name = "input.txt"
    if not os.path.exists(input_file_name):
        print(
            f"{input_file_name} does not exist! Put AG submission output into {input_file_name}"
        )
    else:
        input_dict = read_input(input_file_name)
        calc_shapley(input_dict)
