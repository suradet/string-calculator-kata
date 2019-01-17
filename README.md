# String Calculator Kata

This is my (Suradet Jitprapaikulsarn) Python implementation of the string
calculator kata by Roy Osherove (http://osherove.com/tdd-kata-1/).

## The kata
This is kata, we will create a simple calculator accepting a string as an input
and calculate the sum of the numbers in the string.  The input string may
contain 0 - 2 numbers; for instance, "", "1", "2,3", and "4,5,6".

### Step 1: The simplest case
The simplest case is to handle the empty input string which should provide the
result of 0.
Input: ""
Output: 0

### Step 2: Handle one-number cases.
Handle the input of one number.
Input: "123"
Output: 123

### Step 3: Handle two-number cases.
Handle the input of two numbers.
Input: "123, 456"
Output: 579
