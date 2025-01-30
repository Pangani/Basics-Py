import os 

def function():
    """
    This function prints the current directory and its contents.
    """
    current_dir = os.getcwd()
    print(f"Current Directory: {current_dir}")

def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)
    

result = factorial(5)
print(f"{result}")