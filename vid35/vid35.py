import traceback

# assert statements should be used for programmer errors
# assertions are used as sanity checks - the program should end early
# try and except blocks should be used for user errors


try:
    42 / 0
except ZeroDivisionError:
    print('Division by 0')

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        try:
            raise Exception('"symbol" needs to be a string of length 1.')
        except:
            errorFile = open('error_log.txt', 'a')
            errorFile.write(traceback.format_exc())
            errorFile.close()
            print('Error was written to error log.')
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

boxPrint('*', 15, 5)