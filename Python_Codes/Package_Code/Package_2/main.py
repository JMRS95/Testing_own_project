# Cleaner code thanks to __init__
from shapes import Rectangle, Circle
from calculations import calculate_volume, VectorCalculator

def main():
    # Create 2D shapes
    rect = Rectangle(5, 3)
    circle = Circle(4)
    
    # Calculate volumes (extruding 2D shapes into 3D)
    print(f"Volume of rectangular prism: {calculate_volume(rect, height=2)}")
    print(f"Volume of cylinder: {calculate_volume(circle, height=5):.2f}")
    print(f"Volume of sphere: {calculate_volume(circle):.2f}")
    
    # Vector calculations
    v1 = VectorCalculator(1, 2, 3)
    v2 = VectorCalculator(4, 5, 6)
    print(f"\nDot product: {v1.dot_product(v2)}")
    print(f"Cross product: {v1.cross_product(v2)}")

if __name__ == "__main__":
    main()