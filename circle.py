# create a function to calculate the perimeter of a circle using radius


import numpy as np

def perform_calculation_circle(radius: float, operation: str) -> float:
    """
    Perform a calculation for the perimeter or area of a circle.
    
    Parameters:
        radius (float):The radius of the circle.
        operation (str): The operation to perform. Can be either "perimeter" or "area"

    Returns:
        float: The result of the operation.

    """
    if operation == 'perimeter':
        result = 2*np.pi* radius
    elif operation == 'area':
        result = np.pi*radius**2
    else:
        raise ValueError(f"Unsupported operation: '{operation}'. Use 'perimeter' or 'area'.")
 
    return result


def convert_to_float(value: str) -> float:
    """
    Convert string to floating point number.

    Parameters:
        value (str): The value to convert.

    Returns:
        float: The converted float value of input value.

    Raises:
        ValueError: If value cannot be converted to a float.
    """

    float_value = float(value)

    return float_value