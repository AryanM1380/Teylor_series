# e_power_x Calculator

This Python script calculates the value of e raised to the power of x using a Taylor series expansion. It provides an approximation of the exponential function.

## Usage

To use the script, simply call the `e_power_x()` function with the desired value of x and the number of terms to include in the Taylor series expansion. The function returns the calculated value of e^x.

```python
from math import factorial

def e_power_x(x, term):
    sum = 0
    for i in range(term+1):
        sum += (x**i) / (factorial(i))
    return sum

print(e_power_x(3, 2))  # Example usage: calculates e^3 with 2 terms
```

## Parameters

- `x`: The exponent to which e is raised.
- `term`: The number of terms to include in the Taylor series expansion. Higher values provide more accurate results.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.
