# DEBUG is better because you can keep the lines of code by changing the log levels and/or removing logging

# logging.debug()
# logging.info()
# logging.warning()
# logging.error()
# logging.critical()


import logging

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.critical())
logging.basicConfig(filename='logfile.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial (%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is: {} and total is {}'.format(i, total))

    logging.debug('Return value is {}'.format(total))
    return total

print(factorial(5))

logging.debug('End of program')