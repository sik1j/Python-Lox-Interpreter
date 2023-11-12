import sys
from lox import Lox

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("Usage: plox [script]")
    elif len(sys.argv) == 2:
        Lox.run_file(sys.argv[1])
    else:
        Lox.run_prompt()
