### Impact Aanlytics Assignment

### Graduation Attendance Calculator

# Problem Statement

    In a university, your attendance determines whether you will be allowed to attend your graduation ceremony.
    You are not allowed to miss classes for four or more consecutive days. Your graduation ceremony is on the last day 
    of the academic year, which is the Nth day.

# Your task is to determine the following:

    1. The number of ways to attend classes over N days.
    2. The probability that you will miss your graduation ceremony.

    Represent the solution in the string format as "Answer of (2) / Answer
    of (1)", don't actually divide or reduce the fraction to decimal

## Test cases:

    for 5 days: 14/29
    for 10 days: 372/773
## Prerequisite
    `Python 3` must be installed in your local machine.

## Series Definitions:

    1. **Initial Series (n=1 to n=4):** [2, 4, 8, 15]
   
    - For n=1 to n=4, the series is [2, 4, 8, 15]. The series takes a new value by summing the previous four days' data.

    2. **Extended Series (n=5 and onwards):** [29, 56, 108, 208, 401, 773, ...]

    - After n=4, the series continues based on the sum of the previous four days' data.

    3. **Graduation Day Adjustment:**
   
    - If there is a graduation day marked (A for Absent), the calculation considers the previous three days' 
      data to prevent four or more consecutive absent days.

## Series Examples:

    For n=10:
    - Initial Series: [2, 4, 8, 15, 29, 56, 108, 208, 401, 773]
    - Graduation Day Adjustment: [1, 2, 4, 7, 14, 27, 52, 100, 193, 372]

## Solution Approach:

    1. Calculate the series up to n=10 using the provided rules.

    2. For each day, check if it's a graduation day (A for Absent) and adjust the calculation accordingly to avoid four 
        or more consecutive absent days.

    3. The solution for a given day 'n' is the value in the series for that day.

    4. For n>10, the solution can be calculated dynamically by continuing the series based on the previous four days' 
        data, adjusting for graduation day as needed.

## Important Considerations:

    - Graduation day absence does not lead to invalid data; adjustments are made to maintain the rule of no four or more 
        consecutive absent days.

    - Solutions should adhere to the defined rules for series calculation.
