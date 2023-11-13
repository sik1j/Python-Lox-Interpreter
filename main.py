import sys
from lox import Lox

if __name__ == '__main__':
    if len(sys.argv) > 2:  # too many command line arguments provided
        print("Usage: plox [script]")
    elif len(sys.argv) == 2:  # interpret script file
        Lox.run_file(sys.argv[1])
    else:  # run as REPL
        Lox.run_prompt()
