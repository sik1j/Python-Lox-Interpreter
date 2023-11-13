from tokenType import TokenType


# represents Lox tokens
class Token:
    def __init__(self, token_type: TokenType, lexeme: str, literal: object, line: int):
        self.type = token_type
        self.lexeme = lexeme
        # numbers, strings, and identifiers
        self.literal = literal
        # line no. token found on
        self.line = line

    def __str__(self):
        return self.type.name + " " + self.lexeme + " " + str(self.literal)
