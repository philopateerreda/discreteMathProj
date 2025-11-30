"""
Logic Checker Module
Parses logical expressions, generates truth tables, and checks logical equivalence.
Supports operators: ~ (NOT), v (OR), ^ (AND), -> (IMPLIES), <-> (BICONDITIONAL)
"""

import re
from itertools import product


class LogicChecker:
    """Parse logical expressions and check for logical equivalence."""
    
    def __init__(self):
        """Initialize the logic checker."""
        self.variables = set()
    
    def _extract_variables(self, expression):
        """
        Extract propositional variables from expression.
        
        Args:
            expression: String logical expression
            
        Returns:
            set: Set of variable names (p, q, r, s, etc.)
        """
        # Find all single letters that are variables (not operators)
        variables = set(re.findall(r'\b[p-z]\b', expression.lower()))
        return variables
    
    def _transform_logic(self, expr):
        """
        Recursively transform logical expression to Python syntax.
        Handles parentheses and operator precedence.
        """
        expr = expr.strip()
        
        # Helper to find matching paren
        def find_matching_paren(text, start):
            count = 1
            for i in range(start + 1, len(text)):
                if text[i] == '(':
                    count += 1
                elif text[i] == ')':
                    count -= 1
                if count == 0:
                    return i
            return -1

        # Helper to check if fully enclosed in parens
        def is_fully_enclosed(text):
            if not (text.startswith('(') and text.endswith(')')):
                return False
            # Check if the outer parens are a matching pair
            return find_matching_paren(text, 0) == len(text) - 1

        # 1. Strip outer parentheses
        while is_fully_enclosed(expr):
            expr = expr[1:-1].strip()
            
        # Helper to find operator at depth 0
        def find_operator(text, op):
            nesting = 0
            i = 0
            while i < len(text):
                if text[i] == '(':
                    nesting += 1
                elif text[i] == ')':
                    nesting -= 1
                elif nesting == 0 and text.startswith(op, i):
                    return i
                i += 1
            return -1

        # 2. Handle <-> (Biconditional)
        idx = find_operator(expr, '<->')
        if idx != -1:
            left = expr[:idx]
            right = expr[idx+3:]
            return f"({self._transform_logic(left)} == {self._transform_logic(right)})"

        # 3. Handle -> (Implication)
        idx = find_operator(expr, '->')
        if idx != -1:
            left = expr[:idx]
            right = expr[idx+2:]
            return f"(not {self._transform_logic(left)} or {self._transform_logic(right)})"

        # 4. Handle sub-expressions in parentheses
        # If we reached here, there are no top-level -> or <->
        # But there might be v, ^, ~ or nested expressions in parens
        result = []
        i = 0
        while i < len(expr):
            if expr[i] == '(':
                end = find_matching_paren(expr, i)
                if end == -1:
                    raise ValueError("Unbalanced parentheses")
                inner = expr[i+1:end]
                result.append(f"({self._transform_logic(inner)})")
                i = end + 1
            else:
                result.append(expr[i])
                i += 1
        
        return "".join(result)

    def _evaluate(self, expression, values):
        """
        Evaluate a logical expression given variable values.
        
        Args:
            expression: String logical expression
            values: Dictionary mapping variables to True/False
            
        Returns:
            bool: Result of evaluation
        """
        try:
            # Transform logic syntax to Python syntax
            # We do this first to handle -> and <-> and nested structures
            expr = self._transform_logic(expression.lower())
            
            # Replace remaining operators
            expr = expr.replace('v', ' or ')
            expr = expr.replace('^', ' and ')
            expr = expr.replace('~', ' not ')
            
            # Replace variables with their values
            # Sort variables by length desc to avoid replacing substrings (though vars are single char here)
            for var, val in values.items():
                # Use word boundary to avoid replacing inside keywords if any (though p,q,r are safe from 'or','and')
                expr = re.sub(r'\b' + var + r'\b', str(val), expr)
            
            return eval(expr)
        except Exception as e:
            # raise ValueError(f"Invalid expression: {expression} ({str(e)})")
            raise ValueError(f"Invalid expression: {expression}")
    
    def generate_truth_table(self, expression):
        """
        Generate truth table for a logical expression.
        
        Args:
            expression: String logical expression
            
        Returns:
            tuple: (variables_list, rows) where rows is list of (values_dict, result)
        """
        variables = sorted(self._extract_variables(expression))
        
        if not variables:
            # No variables, just evaluate
            try:
                result = self._evaluate(expression, {})
                return ([], [({}, result)])
            except:
                raise ValueError("Invalid expression with no variables")
        
        rows = []
        # Generate all combinations of True/False for variables
        for values_tuple in product([False, True], repeat=len(variables)):
            values_dict = dict(zip(variables, values_tuple))
            result = self._evaluate(expression, values_dict)
            rows.append((values_dict, result))
        
        return (variables, rows)
    
    def check_equivalence(self, expr1, expr2):
        """
        Check if two logical expressions are equivalent.
        
        Args:
            expr1: First logical expression
            expr2: Second logical expression
            
        Returns:
            tuple: (bool, str, table1, table2) - (are_equivalent, explanation, truth_table1, truth_table2)
        """
        # Get all variables from both expressions
        all_vars = sorted(self._extract_variables(expr1) | self._extract_variables(expr2))
        
        if not all_vars:
            # No variables, just compare results
            result1 = self._evaluate(expr1, {})
            result2 = self._evaluate(expr2, {})
            is_equiv = result1 == result2
            explanation = "Yes - Both expressions evaluate to the same value" if is_equiv else \
                         "No - Expressions evaluate to different values"
            return (is_equiv, explanation, [([], result1)], [([], result2)])
        
        # Generate truth tables with same variable set
        table1 = []
        table2 = []
        is_equiv = True
        first_diff = None
        
        for values_tuple in product([False, True], repeat=len(all_vars)):
            values_dict = dict(zip(all_vars, values_tuple))
            result1 = self._evaluate(expr1, values_dict)
            result2 = self._evaluate(expr2, values_dict)
            
            table1.append((values_dict, result1))
            table2.append((values_dict, result2))
            
            if result1 != result2 and is_equiv:
                is_equiv = False
                first_diff = values_dict.copy()
        
        if is_equiv:
            explanation = "Yes - Both expressions have identical truth tables"
        else:
            diff_str = ", ".join(f"{k}={first_diff[k]}" for k in sorted(first_diff.keys()))
            explanation = f"No - Different results when {diff_str}"
        
        return (is_equiv, explanation, (all_vars, table1), (all_vars, table2))
    
    def format_truth_table(self, truth_table_data):
        """
        Format truth table for display.
        
        Args:
            truth_table_data: Tuple of (variables, rows)
            
        Returns:
            str: Formatted truth table
        """
        variables, rows = truth_table_data
        
        if not variables:
            return "No variables"
        
        # Header
        header = " | ".join(variables) + " | Result"
        separator = "-" * len(header)
        
        lines = [header, separator]
        
        # Rows
        for values_dict, result in rows:
            row_values = [str(values_dict[v])[0] for v in variables]  # T or F
            row_str = " | ".join(row_values) + " | " + str(result)[0]
            lines.append(row_str)
        
        return "\n".join(lines)
