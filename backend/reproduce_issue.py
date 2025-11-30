
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from backend.logic_checker import LogicChecker

def test_parsing():
    checker = LogicChecker()
    expr1 = "p->q"
    expr2 = "(p->q)"
    
    print(f"Testing expression 1: '{expr1}'")
    try:
        table1 = checker.generate_truth_table(expr1)
        print("Success")
    except Exception as e:
        print(f"Failed: {e}")

    print(f"\nTesting expression 2: '{expr2}'")
    try:
        table2 = checker.generate_truth_table(expr2)
        print("Success")
    except Exception as e:
        print(f"Failed: {e}")

    print(f"\nChecking equivalence between '{expr1}' and '{expr2}'")
    is_equiv, explanation, _, _ = checker.check_equivalence(expr1, expr2)
    print(f"Equivalent: {is_equiv}")
    print(f"Explanation: {explanation}")

if __name__ == "__main__":
    test_parsing()
