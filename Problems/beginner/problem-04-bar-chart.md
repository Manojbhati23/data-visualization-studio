# Problem 04: Create a Bar Chart

## Question

Visualize sales data using a bar chart.

```python
products = ["Laptop","Mobile","Tablet"]
sales = [100,150,80]
```

## Solution

```python
import matplotlib.pyplot as plt

product=["Laptop","Phone","PC","Bike","AC"]
sales=[32000,15000,30000,170000,27000]

plt.bar(product,sales)

plt.title("Product-Sales Bar chart")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()

## Output

Three bars representing sales.

## Explanation

`bar()` creates vertical bars.

## Interview Notes

Bar charts compare categories.