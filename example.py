# example.py
def greet_user(name):
    """Greet the user with their name."""
    if not isinstance(name, str):
        raise ValueError("Name must be a string")
    print(f"Hello, {name}!")


def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    return a + b


def main():
    """Main function to run the script."""
    try:
        greet_user("Alice")
        result = calculate_sum(10, 20)
        print(f"The sum is: {result}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
