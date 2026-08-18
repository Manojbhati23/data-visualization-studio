# Problem 01: Create a Basic Line Plot

## Question

Create a line plot using the following data:

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
```

Add:

- Title
- X-axis label
- Y-axis label

## Solution

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.title("Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()
```

## Output

A straight line connecting all points.

## Explanation

- `plot()` creates a line chart.
- `title()` adds a heading.
- `xlabel()` labels the x-axis.
- `ylabel()` labels the y-axis.

## Interview Notes

Line plots are used to visualize trends and continuous data.