import importlib
import inspect
from solver import Evaluator
from exp_parser import Parser


def get_module_functions(module_name):
    """
    Importa un módulo por nombre y retorna un diccionario {nombre_función: función}.
    """
    module = importlib.import_module(module_name)
    functions = {}
    for name, func in inspect.getmembers(module, inspect.isfunction):
        sig = inspect.signature(func)
        params = [(param.name, str(param.annotation)) for param in sig.parameters.values()]
        functions[name] = (func, params)
    return functions

class Logic:
    def __init__(self, sheet_connector = {}):
        functions = get_module_functions("basic")
        self.solv = Evaluator(sheet_connector, functions)

    def add_function(self, functions = {}):
        self.solv.functions = self.solv.functions | functions

    def evaluate(self, expression):
        p = Parser()
        tree = p.parse(expression)
        return self.solv.transform(tree)