# Piyavskii-Shubert
Piyavskii-Shubert algorithm implementation in python.

In the repository there are:
1. src - folder which contains the algorithm implementation
2. functions.py - file which contains test functions
3. results.txt - file which contains the results of test

Run with:
```
python3 main.py
```

Result:
```
-------------------------------------------------------------------

Piyavski Schubert per f20 in [-10,10] con L=1.3
con eps=0.0001 e n=10000
con hmax=10 e 1052 nodi potati

(xstar,ystar): (1.1957360964153374,-0.0634904810184893)

k: 1402
time: 0:00:01.453111
mode: True

-------------------------------------------------------------------
```

If the display mode is setted, it can be possible to interact with a window which plots the input function and the solution.
The scrollbar under the plot is defined to display, for each iteration, the node to expand and the other candidate nodes that are contained in the queue.

![Figure_1](https://github.com/user-attachments/assets/4df35d3f-11c2-4f28-94fe-1e2f0474abba)

