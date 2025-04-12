# index.py

# Basic Python code to print a welcome message and perform simple math

def welcome():
    print("Welcome to the Python script!")

def add_numbers(a, b):
    return a + b

def main():
    welcome()
    result = add_numbers(5, 3)
    print(f"The result of addition is: {result}")

if __name__ == "__main__":
    main()
