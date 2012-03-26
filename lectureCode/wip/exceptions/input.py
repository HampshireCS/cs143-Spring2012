#!/usr/bin/env python

class InputError(Exception):
    def __init__(self, message):
        self.message = message


while True:
    try:
        inp = raw_input("Enter two numbers: ")
        inp = inp.replace(",", " ").split()

        if len(inp) > 2:
            raise InputError("Too many numbers")
        elif len(inp) == 1:
            raise InputError("Too few numbers")


        print float(inp[0]) / float(inp[1])

    except InputError, ex:
        print "Error:", ex.message
    except ValueError:
        print "Error:  One or more values were not a valid number"
    except ZeroDivisionError:
        print "Error:  You cannot divide by zero"
    
    except (KeyboardInterrupt, EOFError):
        print "\nByeBye"
        break

