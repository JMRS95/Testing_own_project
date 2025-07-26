# We use a dot to recongize code inside a package (Really useful)
from package.rectangle import Rectangle
from package.circle import Circle


# We use our package
def main():
    # Create a rectangle
    rect = Rectangle(5, 3)
    print(rect)
    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")
    
    print()  # Blank line
    
    # Create a circle
    circle = Circle(4)
    print(circle)
    print(f"Area: {circle.area():.2f}")
    print(f"Circumference: {circle.circumference():.2f}")

if __name__ == "__main__":
    main()