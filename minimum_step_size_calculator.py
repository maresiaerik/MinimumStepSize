from typing import Optional, List
from utils import create_list_of_length, print_array


class MinimumStepSizeCalculator:
    _DEFAULT_STEP_SIZE = 2

    def __init__(self, input_list_length: List[int]):
        self._latest_step_size = 2
        self.truth_list = {}
        self._input_list_length = input_list_length
        self._list_from_input = create_list_of_length(self._input_list_length)

    def _are_all_values_of_truth_list_true(self) -> bool:
        for x in self.truth_list:
            if not self.truth_list[x]:
                return False
        return True

    def _draw_truth_list(self):
        output_list = []

        for x in self.truth_list:
            # 'X' represents a True value in self.truth_list while '.' False
            char = "X" if self.truth_list[x] else "."
            output_list.append(char)

        print(f"\nCurrent truth_list: \t{print_array(output_list)}")

    def reset_truth_list(self):
        for x in range(1, self._input_list_length + 1):
            self.truth_list[x] = False

    def calculate_minimum(self, step_size: Optional[int] = _DEFAULT_STEP_SIZE) -> int:
        self.reset_truth_list()

        def has_loop_visited_value(idx: int) -> bool:
            return self.truth_list[idx]

        def get_idx_value_for_next_round_of_steps(idx: int) -> int:
            return (
                1
                if idx % len(self._list_from_input) == 0
                else idx % len(self._list_from_input)
            )

        i = 1

        while True:
            self._draw_truth_list()

            if has_loop_visited_value(i):
                self._latest_step_size = step_size + 1
                self.calculate_minimum(step_size=self._latest_step_size)

            self.truth_list[i] = True

            if self._are_all_values_of_truth_list_true():
                self._draw_truth_list()

                return self._latest_step_size

            i += step_size

            if i > len(self._list_from_input):
                i = get_idx_value_for_next_round_of_steps(i)
