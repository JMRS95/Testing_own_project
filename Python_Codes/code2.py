def menu():
    print("----------- MENU -----------")
    print("c: Count up to number 1000")
    print("h: Say hello")
    print("q: Quit")

def condition(user_input):
    if user_input == "q":
        print("Program finished")
        return False
    elif user_input == "h":
        print("Hello!")
    elif user_input == "c":
        print("Counting up to number 1000:")
        for i in range(1001):
            print(f"Number: {i}")
    else:
        print("Unknown option. Try again")
    return True

def main():
    user_input = ""
    print("Initiating program:")
    cond = True
    while cond:
        menu()
        user_input = input("Select an option: ")
        cond = condition(user_input)

if __name__ == "__main__":
    main()