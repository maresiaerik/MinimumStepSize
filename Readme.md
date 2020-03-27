# Recursive functions with Python

What is the **smallest** possible step size _i_ to loop through all of the values in a list of length _n_, without going over the same value twice, given that _i_ > 1 and _n_ > 2?

> If _i = 1_, 1 would be the answer to all possible scenarios, regardless of the value of _n_

> If _n <= 2_, _i_ would be 1

##### Example:

Given a list where ```n = 5```:
```python
list_of_numbers = [1, 2, 3, 4, 5]
```
the correct minimum step size _i_ would be **2**: 
```
Current truth_list:     ['.', '.', '.', '.', '.']

Current truth_list:     ['X', '.', '.', '.', '.']

Current truth_list:     ['X', '.', 'X', '.', '.']

Current truth_list:     ['X', '.', 'X', '.', 'X']

Current truth_list:     ['X', 'X', 'X', '.', 'X']

Current truth_list:     ['X', 'X', 'X', 'X', 'X'],
```
where `X` is a value that has been _visited_ and `.` not yet.

---

Given a list where ```n = 6```:

```python
list_of_numbers = [1, 2, 3, 4, 5, 6]
```

the correct minimum step size _i_ would be **5**:

```
Current truth_list:     ['.', '.', '.', '.', '.', '.']

Current truth_list:     ['X', '.', '.', '.', '.', '.']

Current truth_list:     ['X', '.', '.', '.', '.', 'X']

Current truth_list:     ['X', '.', '.', '.', 'X', 'X']

Current truth_list:     ['X', '.', '.', 'X', 'X', 'X']

Current truth_list:     ['X', '.', 'X', 'X', 'X', 'X']

Current truth_list:     ['X', 'X', 'X', 'X', 'X', 'X'],
```
where `X` is a value that has been _visited_ and `.` not yet.

And so on.
