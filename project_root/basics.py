import logging

# replacing stdout of print with logging

def add(a, b):
    return a + b


logging.warning(f"function to add two numbers: add(5, 7) -> {add(5, 7)}")
    