"""Read input to calculate Shapley value."""


def read_input():
    """Read input to calculate Shapley value."""
    input_dict = {}

    with open("input.txt") as input_file:
        for line in filter(
                lambda line: line.startswith("student test case") and
                "caused error" not in line,
                input_file,
        ):
            line = line.strip()
            test_case = line.split()[3]
            contributions = line[line.index(":") + 2:]

            input_dict[test_case] = [
                contribution for contribution in contributions
            ]

    return input_dict


if __name__ == "__main__":
    print(read_input())
