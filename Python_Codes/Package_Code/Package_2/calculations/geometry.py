import math
from shapes.circle import Circle

def calculate_volume(shape, height=None):
    """Calculate volume for different shapes"""
    if hasattr(shape, 'area'):
        if height is not None:
            # For prism-like shapes (rectangular prism, cylinder)
            return shape.area() * height
        else:
            # For sphere (using radius as the only dimension)
            if isinstance(shape, Circle):
                return (4/3) * math.pi * shape.radius ** 3
    raise ValueError("Unsupported shape for volume calculation")