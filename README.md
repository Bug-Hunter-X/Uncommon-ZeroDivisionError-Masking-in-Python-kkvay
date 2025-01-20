# Uncommon ZeroDivisionError Masking in Python

This repository demonstrates a subtle bug in Python related to zero division. The `function_with_uncommon_bug` function attempts to handle cases where `x` or `y` are zero, but it does not appropriately handle the case where *both* are zero.  This results in a silent return of 0, instead of the expected `ZeroDivisionError`, potentially leading to incorrect results in larger applications.

The `bug.py` file shows the buggy code. The `bugSolution.py` file demonstrates how to fix this by explicitly checking for both `x` and `y` being zero.

This bug can be difficult to catch without rigorous testing, and highlights the need for careful error handling, especially in functions dealing with division.