import sys

# Lab 1:
# Create a Python program that prints my name and
# displays the Python version currently being used.

def main():
    # Print my name
    print("Name: Gursimar")

    # Print the Python interpreter version
    print(f"Python Version: {sys.version}")


# Entry point of the program.
# This ensures main() runs only when this file
# is executed directly.
if __name__ == "__main__":
    main()
