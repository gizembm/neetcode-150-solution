# 271. Encode and Decode Strings

## 🔗 Problem

Design an algorithm that can **encode a list of strings into a single string** and later **decode that string back into the original list**.

The encoded string may be transmitted over a network, so the decoding process must be able to reconstruct the original strings exactly.

The strings may contain any valid ASCII characters, including characters that could normally be used as separators.

---

## Example 1

```text
Input:

strs = ["Hello", "World"]

Encoded:

"5#Hello5#World"

Decoded:

["Hello", "World"]
```

Explanation:

Each string is stored using the following format:

```text
length#string
```

Therefore:

```text
"Hello" → "5#Hello"
"World" → "5#World"
```

Combining them gives:

```text
5#Hello5#World
```

The decoder first reads the length, then reads exactly that many characters.

---

## Example 2

```text
Input:

strs = [""]

Encoded:

"0#"

Decoded:

[""]
```

Explanation:

The empty string has length `0`, so it is encoded as:

```text
0#
```

The decoder reads a length of `0` and correctly reconstructs the empty string.

---

## Example 3

```text
Input:

strs = ["Hello#World", "Python"]

Encoded:

"11#Hello#World6#Python"
```

Even though the first string contains `#`, the algorithm still works correctly.

The decoder reads:

```text
11#
```

and knows that the next **11 characters** belong to the first string.

Therefore, the `#` inside `"Hello#World"` is treated as normal data.

---

## Difficulty

Medium

---

## Topics

- String
- Design

---

## Approach

This solution uses **length-prefixed encoding**.

Each string is converted into the following format:

```text
length#string
```

For example:

```text
"Hello"

↓

5#Hello
```

Multiple encoded strings can then be concatenated safely.

```text
["Hello", "World"]

↓

5#Hello5#World
```

The decoder uses the length stored before `#` to determine exactly how many characters belong to each string.

---

### Step 1 — Encode Each String

Traverse every string in the input list.

```python
for s in strs:
```

For each string, store:

```text
length + "#" + string
```

For example:

```text
"cat"

↓

3#cat
```

---

### Step 2 — Combine the Encoded Strings

Suppose the input is:

```text
["cat", "hello", "x"]
```

The encoded representation becomes:

```text
3#cat5#hello1#x
```

This single string can now be transmitted or stored.

---

### Step 3 — Find the Length During Decoding

Start at index `i` and search for the next `#`.

```python
j = i

while s[j] != "#":
    j += 1
```

Everything between `i` and `j` represents the length.

For example:

```text
5#Hello
^
i
```

After finding `#`:

```text
5 # Hello
^ ^
i j
```

Extract the length:

```python
length = int(s[i:j])
```

Now:

```text
length = 5
```

---

### Step 4 — Read Exactly `length` Characters

Move past the `#`:

```python
i = j + 1
```

Then calculate where the current string ends:

```python
j = i + length
```

Extract the string:

```python
s[i:j]
```

---

### Step 5 — Continue Decoding

Add the decoded string to the result:

```python
res.append(s[i:j])
```

Then move `i` to the beginning of the next encoded string:

```python
i = j
```

Repeat until the entire encoded string has been processed.

---

## Alternative Solutions

### 1. Simple Delimiter

A simple idea would be to join strings using a special character.

For example:

```text
["Hello", "World"]

↓

Hello#World
```

However, this approach is unsafe.

Consider:

```text
["Hello#World", "Python"]
```

Now it becomes difficult to determine whether `#` is a separator or part of the original string.

Therefore, a delimiter alone is not enough.

---

### 2. Escaping Special Characters

Another approach is to escape every occurrence of the delimiter inside the strings.

This can work, but it introduces additional rules and makes both encoding and decoding more complicated.

---

### 3. Length-Prefixed Encoding ✅ (Chosen Solution)

Store the length of each string before the string itself.

```text
length#string
```

Example:

```text
5#Hello
```

The decoder knows exactly how many characters to read after the separator.

This works even when the original string contains `#` or other special characters.

---

## Solution

```python
class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            i = j + 1
            j = i + length

            res.append(s[i:j])

            i = j

        return res
```

---

## Dry Run

Consider:

```text
strs = ["Hello", "World"]
```

### Encoding

Start with:

```text
res = ""
```

Process `"Hello"`:

```text
length = 5

res = "5#Hello"
```

Process `"World"`:

```text
length = 5

res = "5#Hello5#World"
```

Final encoded string:

```text
5#Hello5#World
```

---

### Decoding

Encoded input:

```text
5#Hello5#World
```

#### First String

Find `#`:

```text
5#Hello5#World
^^
ij
```

Read:

```text
length = 5
```

Move past `#` and read exactly 5 characters:

```text
Hello
```

Result:

```text
["Hello"]
```

---

#### Second String

The next encoded section is:

```text
5#World
```

Read:

```text
length = 5
```

Then read the next 5 characters:

```text
World
```

Result:

```text
["Hello", "World"]
```

The original list has been successfully reconstructed.

---

## Key Idea

Do not rely on a special delimiter to separate strings.

Instead, store the **length of each string before its content**:

```text
length#string
```

The decoder uses the length to determine exactly where each string ends.

Because of this, the original strings may contain `#` or other special characters without breaking the encoding format.

---

## Time Complexity

### Encode

```text
O(n)
```

Where `n` is the total number of characters across all strings.

Every character must be included in the encoded result.

### Decode

```text
O(n)
```

The encoded string is processed sequentially.

### Overall

```text
O(n)
```

---

## Space Complexity

```text
O(n)
```

The encoded string and decoded strings require space proportional to the total number of characters.

---

## What I Learned

- How to design a custom encoding format.
- How length-prefixed encoding works.
- Why using only a delimiter is not always safe.
- How to safely encode strings containing special characters.
- How to use two pointers (`i` and `j`) while parsing a string.
- How string slicing can extract a known number of characters.
- How an encoder and decoder must follow the same data format.