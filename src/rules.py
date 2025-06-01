rules = \
"""
start: expr

?expr: expr "+" term     -> add
     | expr "-" term     -> sub
     | term

?term: term "*" factor   -> mul
     | term "/" factor   -> div
     | factor

?factor: function_call
       | cell_range
       | cell
       | NUMBER          -> number
       | "(" expr ")"

function_call: NAME "(" function_args? ")"     -> func_call
?function_args: expr_or_range (";" expr_or_range)*

?expr_or_range: cell_range
              | cell
              | NUMBER
              | expr

cell_range: cell ":" cell            -> cell_range
cell: /[A-Z]+\d+/                    -> cell

%import common.CNAME -> NAME
%import common.NUMBER
%import common.WS
%ignore WS
"""