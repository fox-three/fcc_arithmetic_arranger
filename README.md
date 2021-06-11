### FreeCodeCamp Arithmetic Arranger Project

`arithmetic_arranger.py` contains a function that vertically arranges simple arithmetic problems. It accepts a list of problems as strings. Errors are thrown when the following four criteria are not met:

* The list of problems cannot be longer than five.
* The operator must be either `+` or `-`.
* Each operand can contain no more than four digits.
* Each operand must ONLY contain digits.

The function optionally accepts a second boolean argument that is `False` by default. When `True`, the answer will be printed in addition to the problem.

For example:

```py
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```
Output:

```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

When the second argument is true:

```py
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Output:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```
