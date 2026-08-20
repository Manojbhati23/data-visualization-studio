# Problem 05: Create a Scatter Plot

## Question

Create a scatter plot showing relationship  

## Solution

```python
import matplotlib.pyplot as plt

 #Scatter plot

BikeModel =["Royal Enfiled","KTM","Yamaha","Hero","BMW"]

Price =[250000,180000,175000,150000,300000]

plt.scatter(BikeModel,Price)

plt.title("Bike Price for 2026 Year")
plt.xlabel("Bike Model")
plt.ylabel("Price")

plt.show()
```

## Output

Points displayed without connecting lines.

## Explanation

- `scatter()` creates individual points.
- Useful for finding relationships between variables.

## Interview Notes

Interviewers often ask:

"What is the difference between plot() and scatter()?"

Answer:

- `plot()` creates connected lines.
- `scatter()` creates individual points.

![Output Image for Scatter plot](image.png)