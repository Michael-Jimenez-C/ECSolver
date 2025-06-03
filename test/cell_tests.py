from src.solver import Evaluator
from src.exp_parser import Parser
import random
import re
import numpy as np

class TestCells():
    def __init__(self):
        self.cache = {}

    def get_range(self, start, end):
        print(start, end)
        if f"{start}:{end}" in self.cache:
            return self.cache[f"{start}:{end}"]
        pattern = re.compile(r'([A-Z]+)([0-9]+)')
        start_val = pattern.match(start).groups()[:]
        end_val = pattern.match(end).groups()[:]

        start_col = sum([(ord(i)-ord('A')+1)*(ord('Z')-ord('A')+1)**j for j, i in enumerate(reversed(start_val[0]))])
        end_col = sum([(ord(i)-ord('A')+1)*(ord('Z')-ord('A')+1)**j for j, i in enumerate(reversed(end_val[0]))])
        range = (int(start_val[1]), start_col, int(end_val[1]), end_col)

        self.cache[f"{start}:{end}"]=np.random.randint(1, 255, (range[2]-range[0]+1, range[3]-range[1]+1))
        return self.cache[f"{start}:{end}"]
    def get(self, cell):
        if cell in self.cache:
            return self.cache[cell]
        self.cache[cell] = random.randint(1, 255)
        return self.cache[cell]
    

def test_solver_cell_range():
    cm = TestCells()
    p = Parser()
    evaluator = Evaluator(cm)
    tree = p.parse("A1:B20")
    result = evaluator.transform(tree)
    assert np.mean(result)== np.mean(cm.get_range("A1", "B20"))


def test_solver_cell():
    cm = TestCells()
    p = Parser()
    evaluator = Evaluator(cm)
    tree = p.parse("A6")
    result = evaluator.transform(tree)
    assert np.mean(result)== np.mean(cm.get("A6"))