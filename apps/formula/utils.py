import ast

def get_function_variables(formula):
    tree = ast.parse(formula)
    function_def = next(node for node in tree.body if isinstance(node, ast.FunctionDef))
    variables = [arg.arg for arg in function_def.args.args]
    return variables