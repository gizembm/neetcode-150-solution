# 238. Product of Array Except Self

## 🔗 Problem

Given an integer array `nums`, return an array `output` where `output[i]` is equal to the product of every element in `nums` except `nums[i]`.

The solution should run in **O(n)** time and must not use division.

---

## Example 1

```text
Input:

nums = [1,2,4,6]

Output:

[48,24,12,8]
```

Explanation:

```text
output[0] = 2 × 4 × 6 = 48
output[1] = 1 × 4 × 6 = 24
output[2] = 1 × 2 × 6 = 12
output[3] = 1 × 2 × 4 = 8
```

---

## Example 2

```text
Input:

nums = [-1,0,1,2,3]

Output:

[0,-6,0,0,0]
```

Explanation:

The zero causes every product that includes it to become `0`.

For the index containing `0`, the product of all other elements is:

```text
-1 × 1 × 2 × 3 = -6
```

---

## Difficulty

Medium

---

## Topics

- Array
- Prefix Product
- Suffix Product

---

## Approach

This solution uses **prefix and suffix products**.

For every index, the answer can be calculated as:

```text
product of elements on the left
×
product of elements on the right
```

Instead of creating separate prefix and suffix arrays, the output array is first filled with prefix products.

Then, a single variable is used to track the suffix product while traversing the array from right to left.

---

### Step 1

Create an output array filled with `1`.

```python
output = [1] * len(nums)
```

---

### Step 2

Traverse the array from left to right.

Store the product of all elements to the left of each index.

Example:

```text
nums = [1,2,4,6]

Prefix products:

[1,1,2,8]
```

---

### Step 3

Traverse the array from right to left.

Keep a running `suffix` product.

Multiply the current output value by the suffix.

---

### Step 4

Update the suffix after processing each position.

This produces the final result without using division.

---

## Alternative Solutions

### 1. Brute Force

For every index, multiply all other elements.

- Time Complexity: **O(n²)**
- Space Complexity: **O(1)**

This approach is too slow for large inputs.

---

### 2. Division

Calculate the product of the entire array and divide it by each element.

- Time Complexity: **O(n)**
- Space Complexity: **O(1)**

However, the problem specifically asks for a solution without division.

It also requires additional handling when the array contains zeros.

---

### 3. Prefix and Suffix Arrays

Create two arrays:

```text
prefix[i]
suffix[i]
```

Then calculate:

```text
output[i] = prefix[i] × suffix[i]
```

- Time Complexity: **O(n)**
- Space Complexity: **O(n)**

This is easy to understand, but it uses more memory.

---

### 4. Prefix + Running Suffix ✅

Store prefix products directly inside the output array.

Then calculate suffix products using a single variable.

- Time Complexity: **O(n)**
- Extra Space Complexity: **O(1)**

This is the chosen solution.

---

## Solution

```python
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
```

---

## Dry Run

Example:

```text
nums = [1,2,4,6]
```

### Prefix Pass

Start with:

```text
output = [1,1,1,1]
prefix = 1
```

| Index | nums[i] | Stored Prefix | Prefix After |
|------:|--------:|--------------:|-------------:|
| 0 | 1 | 1 | 1 |
| 1 | 2 | 1 | 2 |
| 2 | 4 | 2 | 8 |
| 3 | 6 | 8 | 48 |

After the prefix pass:

```text
output = [1,1,2,8]
```

---

### Suffix Pass

Start with:

```text
suffix = 1
```

| Index | Output Before | Suffix | Output After | Suffix After |
|------:|--------------:|-------:|-------------:|-------------:|
| 3 | 8 | 1 | 8 | 6 |
| 2 | 2 | 6 | 12 | 24 |
| 1 | 1 | 24 | 24 | 48 |
| 0 | 1 | 48 | 48 | 48 |

Final result:

```text
[48,24,12,8]
```

---

## Key Idea

The product for each index can be split into two independent parts:

```text
left product × right product
```

Store the left product directly in the output array, then multiply it by a running right-side product.

This avoids both division and extra prefix/suffix arrays.

---

## Time Complexity

```text
O(n)
```

The array is traversed twice:

- Left to right: `O(n)`
- Right to left: `O(n)`

Therefore:

```text
O(n)
```

---

## Space Complexity

```text
O(1)
```

Ignoring the required output array, only two variables are used:

```text
prefix
suffix
```

---

## What I Learned

- How prefix and suffix products work.
- How to solve an array problem without using division.
- How to reduce an O(n²) brute-force solution to O(n).
- How to reuse the output array to reduce extra memory.
- Why running prefix and suffix values are useful in array problems.
- How to correctly handle arrays containing zero.