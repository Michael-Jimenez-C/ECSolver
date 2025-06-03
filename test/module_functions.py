from src.logic import Logic
from src.sheet_connector import TestSheetConnector
import numpy as np


def test_functions():
    conector = TestSheetConnector()
    l = Logic(conector)
    assert l.evaluate("SUM(1;2;3;5;7;9)") == sum([1,2,3,5,7,9])
    assert l.evaluate("SUM(1;2;3;5;A1:C14)") == sum([1,2,3,5,np.sum(conector.get_range("A1","C14"))])
    assert l.evaluate("SUM(1;2;3;5;7;9)+PROD(2;3;4)-MIN(A2:B55)") == np.sum([1,2,3,5,7,9]) + np.prod([2,3,4]) - np.min(conector.get_range("A2","B55"))