# Problem 03: Add Legend

## Question

Display a legend for two lines.

## Solution

```python
import matplotlib.pyplot as plt
import numpy as np

# Display a legend for two lines.

x =[1,2,3,4,5]

x1=[23,7,20,8,40]
x2=[10,20,30,40,50]

plt.title("Legend Problem")

plt.plot(x,x1, label='Profit')
plt.plot(x,x2,label='Sales')

plt.legend()

plt.show()
```

## Output

Legend box:

Squares
Linear

## Explanation

- `label` gives each line a name.
- `legend()` displays the legend.

## Interview Notes

One of the most frequently asked Matplotlib questions.