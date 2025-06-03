from lark import Transformer

class Evaluator(Transformer):
    def __init__(self, sheet_connector=None, functions={}):
        self.sheet_connector = sheet_connector
        self.functions = functions

    def number(self, args):
        return float(args[0])

    def cell(self, args):
        name = str(args[0])
        return name

    def cell_range(self, args):
        if len(args) == 1:
            return self.sheet_connector.get(str(args[0]))
        else:
            start = str(args[0])
            end = str(args[1])
            return self.sheet_connector.get_range(start, end)

    def func_call(self, args):
        name = str(args[0]).upper()
        arguments = args[1:]
        if len(arguments) == 1 and isinstance(arguments[0], list):
            arguments = arguments[0]
        if name in self.functions:
            func = self.functions[name][0]
            if callable(func):
                return func(*arguments)
            else:
                raise ValueError(f"Function {name} is not callable.")
    
    def function_args(self, args):
        return args

    def add(self, args):
        return args[0] + args[1]

    def sub(self, args):
        return args[0] - args[1]

    def mul(self, args):
        return args[0] * args[1]

    def div(self, args):
        return args[0] / args[1]

    def neg(self, args):
        return -args[0]

    def pos(self, args):
        return args[0]

    def start(self, args):
        return args[0]