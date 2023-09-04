from minimum_step_size_calculator import MinimumStepSizeCalculator
from utils import create_list_of_length, print_array


def main():
    print(
        "\nPlese input a list length to find out what is the smallest possible step-size to loop through all of the values in a list, without going over the same value twice.\n\nThe given list length should be larger than 2. It is advisable that the list length would be less than 100."
    )

    while True:
        try:
            list_length = int(input("\nList length: \t"))
        except:
            print("\nInput must be an integer.")
            continue

        if list_length < 3:
            print("\nList length too small.")
            continue

        if list_length > 80:
            prompt = input(
                f"\nAre you sure to have a list_length of {list_length}?, your browser might crash. [y/n]: "
            )
            prompt = prompt.lower()
            if prompt == "n" or prompt == "no":
                continue

        user_list = create_list_of_length(list_length)

        print(f"\nYour list: \t{print_array(user_list)}")

        minimum_calculator = MinimumStepSizeCalculator(list_length)

        minimum = minimum_calculator.calculate_minimum()

        print(f"\nMinimum: \t{minimum}\n\n")

        minimum_calculator.reset_truth_list()


if __name__ == "__main__":
    main()
