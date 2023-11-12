class Lox:
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