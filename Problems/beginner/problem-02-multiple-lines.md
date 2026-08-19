# Problem 02: Plot Multiple Lines

## Question

Plot two datasets in the same graph.

```python
x = [1,2,3,4,5]

sales = [10,20,30,40,50]
profit = [2,4,6,8,10]
```

## Solution

```python
import matplotlib.pyplot as plt

x = [1,2,3,4,5]

sales = [10,20,30,40,50]
profit = [2,4,6,8,10]

plt.plot(x, sales)
plt.plot(x, profit)

plt.show()
```

## Output

Two lines displayed on the same graph.

## Explanation

Multiple calls to `plot()` place multiple lines on the same figure.

## Interview Notes

Useful for comparing datasets.