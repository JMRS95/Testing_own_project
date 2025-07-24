import os
import time

def menu():
    print("----------- MENU -----------")
    print("0: Count in python")
    print("1: Count in C++")
    print("q: Quit")

def python_count():
    # Set path and start_time
    file = "count.py"
    start_time = time.time()

    # Run the code
    os.system(f"python3 {file}")

    # Calculate and display runtime
    end_time = time.time()
    run_time = end_time - start_time
    print(f"\tRun time: {run_time:.4f} seconds\n") 

def cpp_count():
    # Set path and start_time
    file = "count.exe"
    start_time = time.time()

    # Run the code
    os.system(f"./{file}")
    
    # Calculate and display runtime
    end_time = time.time()
    run_time = end_time - start_time
    print(f"\tRun time: {run_time:.4f} seconds\n") 


def condition(user_input:str):
    quit = "q"
    root = "/mnt/f/"
    folder = "Maestria/Code/GIT/Project_1/Python-C++_Codes/"
    path = root+folder
    start_time = time.time()

    if (user_input == "0"):
        os.chdir(path)
        python_count()
    elif (user_input=="1"):
        os.chdir(path)
        cpp_count()
    elif (user_input.lower()==quit):
        print("Program finished\n")
        return False
    else:
        print("Unknown option")
    return True

def main():
    user_input = ""
    N = 450000000
    print("This program compares the speed of Python and C++ counting",end=" ")
    print(f"up to number {N}\n\t")
    cond = True
    while cond:
        menu()
        user_input = input("Select an option: ").lower()
        cond = condition(user_input)

if __name__ == "__main__":
    main()