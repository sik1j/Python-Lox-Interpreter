class Lox:
    had_error = False

    @staticmethod
    def run(source: str):
        tokens = source.split()
        print(tokens)

    @staticmethod
    def run_file(script_path: str):
        with open(script_path, 'r') as file:
            Lox.run(file.read())
            file.close()

    @staticmethod
    def run_prompt():
        print("to implement run_prompt")

    @staticmethod
    def error(line: int, message: str):
        Lox.report(line, "", message)

    @staticmethod
    def report(line: int, where: str, message: str):
        print("[line " + str(line) + "] Error" + where + ": " + message)
        Lox.had_error = True
