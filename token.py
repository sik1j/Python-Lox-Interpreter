from tokenType import TokenType


class Token:
    def __init__(self, token_type: TokenType, lexeme: str, literal: object, line: int):
        self.type = token_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return self.type.name + " " + self.lexeme + " " + str(self.literal)
