from src.solver import Evaluator
from src.exp_parser import Parser

def test_solver_maths():
    p = Parser()
    evaluator = Evaluator()
    tree = p.parse("3+5+7+(-2*2-3/2)")
    result = evaluator.transform(tree)
    assert result == 3+5+7+(-2*2-3/2)
    
    tree = p.parse("-2")
    result = evaluator.transform(tree)
    assert result == -2

    tree = p.parse("2.4+5.2")
    result = evaluator.transform(tree)
    assert result == 2.4+5.2

    tree = p.parse("3/1+2*7")
    result = evaluator.transform(tree)
    assert result == 3/1+2*7

