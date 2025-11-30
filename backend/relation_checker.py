"""
Relation Checker Module
Checks properties of binary relations including reflexive, symmetric, antisymmetric,
transitive properties and determines if a relation is an equivalence relation.
"""


class RelationChecker:
    """Check properties of binary relations and determine if they are equivalence relations."""
    
    def __init__(self, set_a, relation, set_b=None):
        """
        Initialize the relation checker.
        
        Args:
            set_a: Set of elements (set or list)
            relation: List of tuples representing ordered pairs
            set_b: Optional second set for relations A -> B
        """
        self.set_a = set(set_a) if not isinstance(set_a, set) else set_a
        self.set_b = set(set_b) if set_b and not isinstance(set_b, set) else (set_b or self.set_a)
        self.relation = set(relation) if not isinstance(relation, set) else relation
        
        # Cache for property results
        self._cache = {}
    
    def check_reflexive(self):
        """
        Check if the relation is reflexive.
        A relation is reflexive if (a,a) exists for every element a in set A.
        
        Returns:
            tuple: (bool, str) - (is_reflexive, explanation)
        """
        if 'reflexive' in self._cache:
            return self._cache['reflexive']
        
        missing = []
        for elem in self.set_a:
            if (elem, elem) not in self.relation:
                missing.append(elem)
        
        is_reflexive = len(missing) == 0
        explanation = "Yes - All elements have self-loops" if is_reflexive else \
                     f"No - Missing pairs: {', '.join(f'({x},{x})' for x in missing)}"
        
        result = (is_reflexive, explanation)
        self._cache['reflexive'] = result
        return result
    
    def check_symmetric(self):
        """
        Check if the relation is symmetric.
        A relation is symmetric if (a,b) implies (b,a).
        
        Returns:
            tuple: (bool, str) - (is_symmetric, explanation)
        """
        if 'symmetric' in self._cache:
            return self._cache['symmetric']
        
        violations = []
        for a, b in self.relation:
            if a != b and (b, a) not in self.relation:
                violations.append((a, b))
        
        is_symmetric = len(violations) == 0
        explanation = "Yes - All pairs have reverse pairs" if is_symmetric else \
                     f"No - Missing reverse pairs: {', '.join(f'({b},{a})' for a, b in violations)}"
        
        result = (is_symmetric, explanation)
        self._cache['symmetric'] = result
        return result
    
    def check_antisymmetric(self):
        """
        Check if the relation is antisymmetric.
        A relation is antisymmetric if (a,b) and (b,a) implies a=b.
        
        Returns:
            tuple: (bool, str) - (is_antisymmetric, explanation)
        """
        if 'antisymmetric' in self._cache:
            return self._cache['antisymmetric']
        
        violations = []
        for a, b in self.relation:
            if a != b and (b, a) in self.relation:
                violations.append((a, b))
        
        is_antisymmetric = len(violations) == 0
        explanation = "Yes - No distinct pairs with reverse pairs" if is_antisymmetric else \
                     f"No - Found pairs: {', '.join(f'({a},{b})' for a, b in violations[:3])} with reverses"
        
        result = (is_antisymmetric, explanation)
        self._cache['antisymmetric'] = result
        return result
    
    def check_transitive(self):
        """
        Check if the relation is transitive.
        A relation is transitive if (a,b) and (b,c) implies (a,c).
        
        Returns:
            tuple: (bool, str) - (is_transitive, explanation)
        """
        if 'transitive' in self._cache:
            return self._cache['transitive']
        
        violations = []
        for a, b in self.relation:
            for b2, c in self.relation:
                if b == b2 and (a, c) not in self.relation:
                    violations.append((a, b, c))
        
        is_transitive = len(violations) == 0
        explanation = "Yes - All transitive pairs exist" if is_transitive else \
                     f"No - Missing: {', '.join(f'({a},{c})' for a, b, c in violations[:3])}"
        
        result = (is_transitive, explanation)
        self._cache['transitive'] = result
        return result
    
    def is_equivalence_relation(self):
        """
        Check if the relation is an equivalence relation.
        Requires: reflexive, symmetric, and transitive.
        
        Returns:
            tuple: (bool, str) - (is_equivalence, explanation)
        """
        ref, _ = self.check_reflexive()
        sym, _ = self.check_symmetric()
        trans, _ = self.check_transitive()
        
        is_equiv = ref and sym and trans
        
        if is_equiv:
            explanation = "Yes - The relation is an equivalence relation (reflexive, symmetric, and transitive)"
        else:
            missing = []
            if not ref: missing.append("reflexive")
            if not sym: missing.append("symmetric")
            if not trans: missing.append("transitive")
            explanation = f"No - Missing properties: {', '.join(missing)}"
        
        return (is_equiv, explanation)
    
    def get_matrix(self):
        """
        Generate the zero-one matrix representation of the relation.
        
        Returns:
            tuple: (list of lists, list of elements) - (matrix, ordered_elements)
        """
        elements = sorted(self.set_a)
        n = len(elements)
        matrix = [[0] * n for _ in range(n)]
        
        elem_to_idx = {elem: i for i, elem in enumerate(elements)}
        
        for a, b in self.relation:
            if a in elem_to_idx and b in elem_to_idx:
                i = elem_to_idx[a]
                j = elem_to_idx[b]
                matrix[i][j] = 1
        
        return (matrix, elements)
    
    def get_digraph(self):
        """
        Get directed graph representation as edge list.
        
        Returns:
            list: List of tuples (from, to) representing directed edges
        """
        return sorted(list(self.relation))
    
    def get_all_results(self):
        """
        Get all property check results.
        
        Returns:
            dict: All property results and representations
        """
        return {
            'reflexive': self.check_reflexive(),
            'symmetric': self.check_symmetric(),
            'antisymmetric': self.check_antisymmetric(),
            'transitive': self.check_transitive(),
            'equivalence': self.is_equivalence_relation(),
            'matrix': self.get_matrix(),
            'digraph': self.get_digraph()
        }
