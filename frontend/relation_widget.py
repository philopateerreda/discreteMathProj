"""
Relation Checker Widget
PyQt5 interface for checking relation properties and equivalence relations.
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QLineEdit, QPushButton, QTextEdit, QGroupBox,
                             QTableWidget, QTableWidgetItem, QSplitter, QScrollArea)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from backend.relation_checker import RelationChecker


class RelationWidget(QWidget):
    """Widget for relation property checking."""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface."""
        # Main layout with ScrollArea
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Scroll Area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(0)
        scroll.setStyleSheet("background-color: transparent;")
        
        # Content Widget
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)
        layout.setSpacing(25)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Header
        title = QLabel("Equivalence Relation Checker")
        title.setProperty("class", "header")
        title.setAlignment(Qt.AlignCenter) # Center title
        layout.addWidget(title)
        
        # Input Section
        input_group = QGroupBox("Input Configuration")
        input_layout = QVBoxLayout()
        input_layout.setSpacing(20)
        
        # Set A input
        set_a_layout = QVBoxLayout() # Changed to vertical for better mobile/resize flow
        set_a_label = QLabel("Set A Elements")
        set_a_label.setStyleSheet("color: #00E5FF; font-weight: bold;")
        self.set_a_input = QLineEdit()
        self.set_a_input.setPlaceholderText("e.g., 1, 2, 3, 4")
        set_a_layout.addWidget(set_a_label)
        set_a_layout.addWidget(self.set_a_input)
        input_layout.addLayout(set_a_layout)
        
        # Set B input (optional)
        set_b_layout = QVBoxLayout()
        set_b_label = QLabel("Set B Elements (Optional)")
        self.set_b_input = QLineEdit()
        self.set_b_input.setPlaceholderText("Leave empty for relation on A")
        set_b_layout.addWidget(set_b_label)
        set_b_layout.addWidget(self.set_b_input)
        input_layout.addLayout(set_b_layout)
        
        # Relation input
        rel_layout = QVBoxLayout()
        rel_label = QLabel("Relation Pairs")
        rel_label.setStyleSheet("color: #00E5FF; font-weight: bold;")
        self.relation_input = QLineEdit()
        self.relation_input.setPlaceholderText("e.g., (1,1), (1,2), (2,2)")
        rel_layout.addWidget(rel_label)
        rel_layout.addWidget(self.relation_input)
        input_layout.addLayout(rel_layout)
        
        # Analyze button
        self.analyze_btn = QPushButton("ANALYZE RELATION")
        self.analyze_btn.setCursor(Qt.PointingHandCursor)
        self.analyze_btn.clicked.connect(self.analyze_relation)
        self.analyze_btn.setMinimumHeight(55) # Taller button
        input_layout.addWidget(self.analyze_btn)
        
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)
        
        # Results Splitter (Horizontal split for results vs visuals)
        splitter = QSplitter(Qt.Horizontal)
        
        # Left Side: Text Results
        results_widget = QWidget()
        results_layout = QVBoxLayout(results_widget)
        results_layout.setContentsMargins(0, 0, 10, 0)
        
        props_label = QLabel("Property Analysis")
        props_label.setProperty("class", "subheader")
        results_layout.addWidget(props_label)
        
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)
        self.results_text.setMinimumHeight(200)
        results_layout.addWidget(self.results_text)
        
        equiv_label = QLabel("Conclusion")
        equiv_label.setProperty("class", "subheader")
        results_layout.addWidget(equiv_label)
        
        self.equiv_result = QLabel("Ready to analyze")
        self.equiv_result.setProperty("class", "result")
        self.equiv_result.setAlignment(Qt.AlignCenter)
        self.equiv_result.setWordWrap(True)
        results_layout.addWidget(self.equiv_result)
        
        splitter.addWidget(results_widget)
        
        # Right Side: Visuals
        visuals_widget = QWidget()
        visuals_layout = QVBoxLayout(visuals_widget)
        visuals_layout.setContentsMargins(10, 0, 0, 0)
        
        matrix_label = QLabel("Zero-One Matrix")
        matrix_label.setProperty("class", "subheader")
        visuals_layout.addWidget(matrix_label)
        
        self.matrix_table = QTableWidget()
        visuals_layout.addWidget(self.matrix_table)
        
        digraph_label = QLabel("Digraph Edges")
        digraph_label.setProperty("class", "subheader")
        visuals_layout.addWidget(digraph_label)
        
        self.digraph_text = QTextEdit()
        self.digraph_text.setReadOnly(True)
        self.digraph_text.setMaximumHeight(100)
        visuals_layout.addWidget(self.digraph_text)
        
        splitter.addWidget(visuals_widget)
        
        # Set initial sizes for splitter
        splitter.setSizes([500, 500])
        
        layout.addWidget(splitter, 1) # Give it stretch factor
        
        # Set scroll widget
        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)
    
    def parse_set(self, text):
        """Parse comma-separated set input."""
        if not text.strip():
            return set()
        elements = [elem.strip() for elem in text.split(',')]
        # Try to convert to int if possible
        result = []
        for elem in elements:
            try:
                result.append(int(elem))
            except ValueError:
                result.append(elem)
        return set(result)
    
    def parse_relation(self, text):
        """Parse relation input like (1,2), (2,3)."""
        if not text.strip():
            return set()
        
        # Extract all pairs
        import re
        pairs = re.findall(r'\(([^,]+),([^)]+)\)', text)
        result = []
        for a, b in pairs:
            a = a.strip()
            b = b.strip()
            # Try to convert to int
            try:
                a = int(a)
            except ValueError:
                pass
            try:
                b = int(b)
            except ValueError:
                pass
            result.append((a, b))
        return set(result)
    
    def analyze_relation(self):
        """Analyze the relation and display results."""
        try:
            # Parse inputs
            set_a = self.parse_set(self.set_a_input.text())
            set_b = self.parse_set(self.set_b_input.text())
            relation = self.parse_relation(self.relation_input.text())
            
            if not set_a:
                self.show_error("Please enter Set A")
                return
            
            if not relation:
                self.show_error("Please enter at least one relation pair")
                return
            
            # Create checker
            if set_b:
                checker = RelationChecker(set_a, relation, set_b)
            else:
                checker = RelationChecker(set_a, relation)
            
            # Get all results
            results = checker.get_all_results()
            
            # Display property results
            props_text = ""
            props_text += f"✓ Reflexive: {results['reflexive'][1]}\n\n"
            props_text += f"✓ Symmetric: {results['symmetric'][1]}\n\n"
            props_text += f"✓ Antisymmetric: {results['antisymmetric'][1]}\n\n"
            props_text += f"✓ Transitive: {results['transitive'][1]}\n"
            self.results_text.setPlainText(props_text)
            
            # Display equivalence result
            is_equiv, equiv_msg = results['equivalence']
            self.equiv_result.setText(equiv_msg)
            if is_equiv:
                self.equiv_result.setProperty("class", "success")
            else:
                self.equiv_result.setProperty("class", "error")
            # Reapply stylesheet
            self.equiv_result.setStyle(self.equiv_result.style())
            
            # Display matrix
            matrix, elements = results['matrix']
            self.display_matrix(matrix, elements)
            
            # Display digraph
            digraph = results['digraph']
            digraph_text = "Edges (directed arrows):\n"
            for a, b in digraph:
                digraph_text += f"  {a} → {b}\n"
            self.digraph_text.setPlainText(digraph_text)
            
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
    
    def display_matrix(self, matrix, elements):
        """Display zero-one matrix in table widget."""
        n = len(elements)
        self.matrix_table.clear()
        self.matrix_table.setRowCount(n)
        self.matrix_table.setColumnCount(n)
        
        # Set headers
        headers = [str(elem) for elem in elements]
        self.matrix_table.setHorizontalHeaderLabels(headers)
        self.matrix_table.setVerticalHeaderLabels(headers)
        
        # Fill matrix
        for i in range(n):
            for j in range(n):
                item = QTableWidgetItem(str(matrix[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                # Color 1s differently
                if matrix[i][j] == 1:
                    item.setForeground(Qt.cyan)
                    font = item.font()
                    font.setBold(True)
                    item.setFont(font)
                self.matrix_table.setItem(i, j, item)
        
        # Adjust column widths and row heights
        self.matrix_table.resizeColumnsToContents()
        self.matrix_table.verticalHeader().setDefaultSectionSize(45) # Taller rows
    
    def show_error(self, message):
        """Show error message."""
        self.results_text.setPlainText(f"❌ {message}")
        self.equiv_result.setText("Please fix input errors")
        self.equiv_result.setProperty("class", "error")
        self.equiv_result.setStyle(self.equiv_result.style())
