import module1
import module2


def main():
    name = "Alice"
    
    # Use functions from module1
    print(module1.greet(name))
    print(f"5 + 3 = {module1.add(5, 3)}")
    
    # Use functions from module2
    print(module2.farewell(name))
    print(f"5 * 3 = {module2.multiply(5, 3)}")

if __name__ == "__main__":
    main()