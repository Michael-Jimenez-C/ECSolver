from ecsolver.solver import Evaluator
from ecsolver.exp_parser import Parser
import numpy as np
from ecsolver.sheet_connector import TestSheetConnector
    

def test_solver_cell_range():
    cm = TestSheetConnector()
    p = Parser()
    evaluator = Evaluator(cm)
    tree = p.parse("A1:B20")
    result = evaluator.transform(tree)
    assert np.mean(result)== np.mean(cm.get_range("A1", "B20"))


def test_solver_cell():
    cm = TestSheetConnector()
    p = Parser()
    evaluator = Evaluator(cm)
    tree = p.parse("A6")
    result = evaluator.transform(tree)
    assert np.mean(result)== np.mean(cm.get("A6"))