"""
Tree Checker Module
Validates if a graph is a tree by checking:
1. Number of edges = number of vertices - 1
2. Graph is acyclic (no cycles)
3. Graph is connected
"""

from collections import defaultdict, deque


class TreeChecker:
    """Check if a graph is a tree."""
    
    def __init__(self, vertices=None):
        """
        Initialize the tree checker.
        
        Args:
            vertices: List of vertex names/labels
        """
        self.vertices = set(vertices) if vertices else set()
        self.edges = []
        self.adjacency = defaultdict(set)
    
    def set_vertices(self, vertices):
        """
        Set the vertices of the graph.
        
        Args:
            vertices: List of vertex names
        """
        self.vertices = set(vertices)
        # Clear edges that may reference old vertices
        self.edges = []
        self.adjacency = defaultdict(set)
    
    def add_edge(self, v1, v2):
        """
        Add an edge to the graph.
        
        Args:
            v1: First vertex
            v2: Second vertex
            
        Returns:
            tuple: (bool, str) - (success, message)
        """
        if v1 not in self.vertices:
            return (False, f"Vertex '{v1}' not in graph")
        if v2 not in self.vertices:
            return (False, f"Vertex '{v2}' not in graph")
        if (v1, v2) in self.edges or (v2, v1) in self.edges:
            return (False, f"Edge ({v1}, {v2}) already exists")
        
        self.edges.append((v1, v2))
        # For undirected graph, add both directions
        self.adjacency[v1].add(v2)
        self.adjacency[v2].add(v1)
        
        return (True, f"Added edge ({v1}, {v2})")
    
    def add_edges(self, edges):
        """
        Add multiple edges at once.
        
        Args:
            edges: List of tuples (v1, v2)
            
        Returns:
            list: List of (success, message) for each edge
        """
        results = []
        for v1, v2 in edges:
            results.append(self.add_edge(v1, v2))
        return results
    
    def check_edge_count(self):
        """
        Check if edge count equals vertex count - 1.
        
        Returns:
            tuple: (bool, str) - (valid_count, explanation)
        """
        v_count = len(self.vertices)
        e_count = len(self.edges)
        expected = v_count - 1
        
        if e_count == expected:
            return (True, f"Correct: {e_count} edges for {v_count} vertices")
        elif e_count < expected:
            return (False, f"Too few edges: {e_count} < {expected} (graph is disconnected)")
        else:
            return (False, f"Too many edges: {e_count} > {expected} (contains cycle)")
    
    def has_cycle(self):
        """
        Check if the graph contains a cycle using DFS.
        
        Returns:
            tuple: (bool, str) - (has_cycle, explanation)
        """
        if not self.vertices:
            return (False, "No vertices")
        
        visited = set()
        
        def dfs(node, parent):
            visited.add(node)
            for neighbor in self.adjacency[node]:
                if neighbor not in visited:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    # Found a back edge (cycle)
                    return True
            return False
        
        # Check from any starting vertex
        for start in self.vertices:
            if start not in visited:
                if dfs(start, None):
                    return (True, "Cycle detected")
        
        return (False, "No cycles found")
    
    def is_connected(self):
        """
        Check if the graph is connected using BFS.
        
        Returns:
            tuple: (bool, str) - (is_connected, explanation)
        """
        if not self.vertices:
            return (True, "Empty graph is connected")
        
        # Start BFS from any vertex
        start = next(iter(self.vertices))
        visited = set([start])
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            for neighbor in self.adjacency[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        is_conn = len(visited) == len(self.vertices)
        
        if is_conn:
            return (True, "All vertices are reachable")
        else:
            disconnected = self.vertices - visited
            return (False, f"Disconnected vertices: {', '.join(sorted(disconnected))}")
    
    def is_tree(self):
        """
        Check if the graph is a tree.
        A tree must satisfy:
        1. |E| = |V| - 1
        2. No cycles
        3. Connected
        
        Returns:
            tuple: (bool, str, dict) - (is_tree, explanation, details)
        """
        if not self.vertices:
            return (False, "No vertices defined", {})
        
        # Check edge count first (quick rejection)
        edge_ok, edge_msg = self.check_edge_count()
        
        # Check for cycles
        has_cycle, cycle_msg = self.has_cycle()
        
        # Check connectivity
        connected, conn_msg = self.is_connected()
        
        details = {
            'edge_count': edge_ok,
            'edge_message': edge_msg,
            'acyclic': not has_cycle,
            'cycle_message': cycle_msg,
            'connected': connected,
            'connected_message': conn_msg,
            'vertex_count': len(self.vertices),
            'edge_list': self.edges
        }
        
        is_tree_result = edge_ok and not has_cycle and connected
        
        if is_tree_result:
            explanation = f"✓ Yes - This is a valid tree with {len(self.vertices)} vertices and {len(self.edges)} edges"
        else:
            reasons = []
            if not edge_ok:
                reasons.append(edge_msg)
            if has_cycle:
                reasons.append("Contains cycle")
            if not connected:
                reasons.append("Graph is disconnected")
            explanation = f"✗ No - Not a tree. Issues: {'; '.join(reasons)}"
        
        return (is_tree_result, explanation, details)
    
    def get_traversals(self, root):
        """
        Get Pre-order, In-order, and Post-order traversals rooted at 'root'.
        
        Args:
            root: The starting vertex for the tree.
            
        Returns:
            dict: {
                'pre_order': list,
                'in_order': list or str (if not binary),
                'post_order': list
            }
        """
        if root not in self.vertices:
            return {
                'pre_order': [],
                'in_order': "Invalid root",
                'post_order': []
            }
            
        # Build directed adjacency list (parent -> children) for the given root
        # Since edges are undirected, we need to traverse BFS/DFS to establish direction
        children_map = defaultdict(list)
        visited = set([root])
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            # Get neighbors, sort them alphabetically for deterministic output
            neighbors = sorted(list(self.adjacency[node]))
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    children_map[node].append(neighbor)
                    queue.append(neighbor)
        
        # Pre-order: Root -> Children
        pre_order_result = []
        def dfs_pre(node):
            pre_order_result.append(node)
            for child in children_map[node]:
                dfs_pre(child)
        dfs_pre(root)
        
        # Post-order: Children -> Root
        post_order_result = []
        def dfs_post(node):
            for child in children_map[node]:
                dfs_post(child)
            post_order_result.append(node)
        dfs_post(root)
        
        # In-order: Left -> Root -> Right (Binary Tree only)
        in_order_result = []
        is_binary = True
        
        def dfs_in(node):
            nonlocal is_binary
            children = children_map[node]
            count = len(children)
            
            if count > 2:
                is_binary = False
                return
            
            if count == 0:
                in_order_result.append(node)
            elif count == 1:
                # Ambiguity: Is the single child left or right?
                # Standard convention for single child in general tree -> treat as left?
                # Or strictly: if we don't know, maybe just do Child -> Root?
                # Let's assume: Left -> Root
                dfs_in(children[0])
                if not is_binary: return
                in_order_result.append(node)
            elif count == 2:
                dfs_in(children[0]) # Left
                if not is_binary: return
                in_order_result.append(node) # Root
                dfs_in(children[1]) # Right
                if not is_binary: return

        dfs_in(root)
        
        return {
            'pre_order': pre_order_result,
            'in_order': in_order_result if is_binary else "N/A (Not a Binary Tree)",
            'post_order': post_order_result
        }

    def get_visualization_data(self):
        """
        Get data for visualization.
        
        Returns:
            dict: Vertices and edges for display
        """
        return {
            'vertices': sorted(list(self.vertices)),
            'edges': self.edges,
            'adjacency': dict(self.adjacency)
        }
