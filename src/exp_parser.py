from rules import rules
from lark import Lark

class Parser:
    def __init__(self, grammar):
        self.parser = Lark(grammar, start='start')
    
    @staticmethod
    def tree_to_dict(tree):
        if hasattr(tree, 'data'):
            return {
                'type': tree.data,
                'children': [Parser.tree_to_dict(c) for c in tree.children]
            }
        else:
            return str(tree)

    def parse(self, formula):
        return Parser.tree_to_dict(self.parser.parse(formula))