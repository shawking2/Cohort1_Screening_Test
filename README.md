# Discussion
## 1. Discussion about method using random number
- The method `random.randint(a, b)` is part of the `random` module in python, which is a pseudo-random number generator (PRNG). 
- According to the Python documentation, this method uses the Mersenne Twister algorithm. It generates floating-point numbers with 53-bit precision and has a cycle of 2**19937-1. Generating identical sequences is only feasible when the number of bits used for randomization is very small. Below is a piece of code used to find the nth occurrence with n = 3, trying with the generate_random_list function in the above program:

```python
import random

def generate_random_list(n: int):
    list_n = []
    while len(list_n) < 2 * n:    
        random_number = random.randint(1, 2**n - 1) 
        if random_number not in list_n:
            list_n.append(random_number)
    return list_n

def count_matching_lists(n: int, num_trials=10000):
    target_list_n = generate_random_list(n)
    count = 0
    for _ in range(num_trials):
        list_n = generate_random_list(n)
        if list_n == target_list_n:
            count += 1
            print(_)
    return count

num_trials_until_match = count_matching_lists(3)
print(f"The number of times needed to get the same result: {num_trials_until_match}")
```
- Out of 10,000 trials, the number of occurrences where the sequence of numbers matches the comparison sequence fluctuates between 1 and 4.
```
Cohort1_Screening_Test % python count_matching_lists.py
563
2022
2154
4024
The number of times needed to get the same result: 4
```
## Discussion on Finding K and Elements Less Than K
- Finding K
    + The `binary_search` function function performs a binary search on the sorted list to find the position of K.
    + Complexity: O(log(2n)) because the list has a length of `2*n`.
    + Average number of trials: log(2n).
- Finding Elements Less Than K
    + From the position of K found above, we simply iterate backward through the list to get the elements smaller than K.
    + Complexity: O(n)
