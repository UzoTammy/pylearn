import logging


logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(asctime)s:- Result: %(message)s', filename='pylearn.log')

# replacing stdout of print with logging

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def minus(a, b):
    return a - b

logging.warning(f"function to add two numbers: add(5, 7) -> {add(5, 7)}")

logging.info(add(3, 4))

