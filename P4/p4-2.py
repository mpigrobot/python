try:
    num1 = int(input('Enter the first number:'))
    num2 = int(input('Enter the second number:'))
    print num1/num2
except ValueError as err :
    print 'Please input a digit!'
    print err
