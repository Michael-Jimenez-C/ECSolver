from rules import rules
from lark import Lark

class Parser:
    def __init__(self):
        self.parser = Lark(rules, start='start')
    
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
        return self.parser.parse(formula)