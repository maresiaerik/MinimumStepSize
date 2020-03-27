#   Reset all values to False
def reset_truth_list():
    for x in range(1, list_length + 1):
        truth_list[x] = False

def are_all_true():
    for x in truth_list:
        if not truth_list[x]:
            return False
    return True

def draw_truth_list():
    output_list = [] #  List to print out to show progress
    for x in truth_list:
        char = 'X' if truth_list[x] else '.' #  X represents a True value in truth_list while . False
        output_list.append(char)
    print('\nCurrent truth_list: \t{}'.format(print_array(output_list)))

#   Utility function to prevent [object Object] displaying on the browser
def print_array(arr):
    res = '['
    i = 1
    for x in arr:
        res += "'{}'".format(x)
        if i < len(arr):
        res += ','
        i += 1
    res += ']'
    return res

def calculate_minimum(step_size):
    global latest_step_size # Workaround to avoid UnboundLocalError: local variable referenced before assignment
    reset_truth_list()
    i = 1 # truth_list index starts from 1
    while True:
        draw_truth_list()
        if truth_list[i]:
            #   This value has already been 'visited' by the loop -> increase step size and call itself again
            latest_step_size = step_size + 1
            calculate_minimum(step_size=latest_step_size)
        truth_list[i] = True
        if are_all_true():
            #   All values are True -> minimum found
            draw_truth_list()
            return latest_step_size
        i += step_size
        if i > len(user_list):
            #   Make i always a value inside the truth_list
            i = 1 if i % len(user_list) == 0 else (i % len(user_list))

while True:
    try:
      list_length = int(input('\nList length: \t'))
    except:
      print("\nInput must be an integer.")
      continue

    if list_length < 3:
      print('\nList length too small.')
      continue

    if list_length > 80:
        prompt = input('\nAre you sure to have a list_length of {}?, your browser might crash. [y/n]: '.format(list_length))
        prompt = prompt.lower()
        if prompt == 'n' or prompt == 'no':
            continue

    #   Create list from 1 until given value
    user_list = [x for x in range(1, list_length  + 1)]

    print('\nYour list: \t{}'.format(print_array(user_list)))

    truth_list = {}
    latest_step_size = 2

    minimum = calculate_minimum(step_size=latest_step_size)

    print('\nMinimum: \t{}\n\n'.format(minimum))
