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
- It's possible to predict the next random number if we have the seed. The seed is used to initialize the random number generator and determine the sequence of random numbers that the generator will produce. When we provide the same seed to the generator, it will generate the same sequence of random numbers each time it runs. Below is an example:
```python

import random

def predict_random():
    # Generate a random seed
    seed = random.randint(0, 100000)
    
    # Initialize a random number generator with the corresponding seed
    random.seed(seed)
    
    # Generate a sequence of random numbers
    random_numbers = [random.random() for _ in range(10)]
    
    # Retrieve the seed and initialize the random number generator with the retrieved seed
    random.seed(seed)
    
    # Generate the sequence of random numbers again
    predicted_numbers = [random.random() for _ in range(10)]
    
    # Compare the generated sequences of random numbers
    if random_numbers == predicted_numbers:
        return True
    else:
        return False

# Check whether the result of the random() function can be predicted based on the seed
if predict_random():
    print("The result of the random() function can be predicted based on the seed.")
else:
    print("The result of the random() function cannot be predicted based on the seed.")
  
  ```
Result:
```
% python predict.py
The result of the random() function can be predicted based on the seed.
```
## 2. Discussion on Finding K and Elements Less Than K
- Finding K
    + The `binary_search` function function performs a binary search on the sorted list to find the position of K.
    + Complexity: O(log(n)) .
    + Average number of trials: log(n).
- Finding Elements Less Than K
    + From the position of K found above, we simply iterate backward through the list to get the elements smaller than K.
    + Complexity: O(x) with x is position of K in list.
## 3. Which problems can be solved by quantum computing

### Problems of classic computer:
- As we can see from the previous section, there are some problems with generating random numbers on classical computers:
    + They are not actually generated randomly, but rather through algorithms. Even though the Mersenne Twister algorithm has a large period, as shown in the test above, it still produces some repetitions of results.
    + The sequence can be predicted if the seed is known.
- Find K in list:
    + In order to be as fast as possible, I sorted the initial list from smallest to largest when generating random numbers. Therefore, when applying binary search, its complexity is only O(log(N)). However, if a list is not sorted, searching for an element K in the list can take up to O(N).
- Elements less than K in list:
    + Since the list is sorted from smallest to largest and the position of element K has been sorted in the list, the complexity is only O(x) where x is the position of K in the list. However, if the list is not sorted, other methods such as iterating through all elements must be used, which will result in a complexity of O(N).
### How can quantum computers solve these problems?
- Random number:
    + Quantum computers can generate truly random numbers using quantum effects such as superposition and entanglement. We will not know what their state is until we measure it and collapse occurs.
- Find K in list:
    + If we apply Grover's algorithm on a quantum computer, the complexity of finding K is only O(sqrt(N)).
- Elements less than K in list:
    + If we use Grover's algorithm for each search for an element less than K, the complexity will be O(sqrt(N) * M), where M is the number of elements less than K.





