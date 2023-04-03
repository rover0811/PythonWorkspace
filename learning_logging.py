import logging

# set up logging configuration
logging.basicConfig(filename='example.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# example function
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logging.error("Tried to divide by zero")
    else:
        logging.info(f"{x} / {y} = {result}")

# call the function
divide(10, 2)
divide(5, 0)


#Show me a example with decorator in Python