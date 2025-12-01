"""
Tree Checker Widget
PyQt5 interface for validating tree structures.
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QLineEdit, QPushButton, QTextEdit, QGroupBox,
                             QListWidget, QListWidgetItem, QSpinBox, QSplitter, QScrollArea,
                             QComboBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from backend.tree_checker import TreeChecker


class TreeWidget(QWidget):
    """Widget for tree validation."""
    
    def __init__(self):
        super().__init__()
        self.checker = None
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
        title = QLabel("Tree Structure Validator")
        title.setProperty("class", "header")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Main Splitter
        splitter = QSplitter(Qt.Horizontal)
        
        # Left Panel: Controls
        controls_widget = QWidget()
        controls_layout = QVBoxLayout(controls_widget)
        controls_layout.setContentsMargins(0, 0, 10, 0)
        controls_layout.setSpacing(20)
        
        # Step 1
        step1_group = QGroupBox("1. Define Vertices")
        step1_layout = QVBoxLayout()
        
        self.vertices_input = QLineEdit()
        self.vertices_input.setPlaceholderText("e.g., A, B, C, D")
        step1_layout.addWidget(self.vertices_input)
        
        self.set_vertices_btn = QPushButton("SET VERTICES")
        self.set_vertices_btn.setCursor(Qt.PointingHandCursor)
        self.set_vertices_btn.clicked.connect(self.set_vertices)
        step1_layout.addWidget(self.set_vertices_btn)
        
        self.vertex_count_label = QLabel("No vertices set")
        self.vertex_count_label.setAlignment(Qt.AlignCenter)
        step1_layout.addWidget(self.vertex_count_label)
        
        step1_group.setLayout(step1_layout)
        controls_layout.addWidget(step1_group)
        
        # Step 2
        step2_group = QGroupBox("2. Add Edges")
        step2_layout = QVBoxLayout()
        
        edge_input_layout = QHBoxLayout()
        self.from_input = QLineEdit()
        self.from_input.setPlaceholderText("From")
        self.to_input = QLineEdit()
        self.to_input.setPlaceholderText("To")
        edge_input_layout.addWidget(self.from_input)
        edge_input_layout.addWidget(QLabel("↔"))
        edge_input_layout.addWidget(self.to_input)
        step2_layout.addLayout(edge_input_layout)
        
        self.add_edge_btn = QPushButton("ADD EDGE")
        self.add_edge_btn.setCursor(Qt.PointingHandCursor)
        self.add_edge_btn.clicked.connect(self.add_edge)
        self.add_edge_btn.setEnabled(False)
        step2_layout.addWidget(self.add_edge_btn)
        
        self.clear_edges_btn = QPushButton("CLEAR EDGES")
        self.clear_edges_btn.setProperty("class", "secondary")
        self.clear_edges_btn.setCursor(Qt.PointingHandCursor)
        self.clear_edges_btn.clicked.connect(self.clear_edges)
        self.clear_edges_btn.setEnabled(False)
        step2_layout.addWidget(self.clear_edges_btn)
        
        step2_group.setLayout(step2_layout)
        controls_layout.addWidget(step2_group)
        
        # Validate Button
        self.check_tree_btn = QPushButton("VALIDATE TREE STRUCTURE")
        self.check_tree_btn.setMinimumHeight(60)
        self.check_tree_btn.setCursor(Qt.PointingHandCursor)
        self.check_tree_btn.clicked.connect(self.check_tree)
        self.check_tree_btn.setEnabled(False)
        controls_layout.addWidget(self.check_tree_btn)
        
        controls_layout.addStretch()
        splitter.addWidget(controls_widget)
        
        # Right Panel: Visuals & Results
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(10, 0, 0, 0)
        right_layout.setSpacing(20)
        
        # Edge Status
        status_group = QGroupBox("Edge Status")
        status_layout = QVBoxLayout()
        self.edge_info_label = QLabel("Waiting for vertices...")
        self.edge_info_label.setAlignment(Qt.AlignCenter)
        self.edge_info_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        status_layout.addWidget(self.edge_info_label)
        status_group.setLayout(status_layout)
        right_layout.addWidget(status_group)
        
        # Edge List
        list_group = QGroupBox("Current Edges")
        list_layout = QVBoxLayout()
        self.edges_list = QListWidget()
        list_layout.addWidget(self.edges_list)
        list_group.setLayout(list_layout)
        right_layout.addWidget(list_group)
        
        # Final Result
        result_group = QGroupBox("Validation Result")
        result_layout = QVBoxLayout()
        self.result_label = QLabel("Ready to validate")
        self.result_label.setProperty("class", "result")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setWordWrap(True)
        result_layout.addWidget(self.result_label)
        
        self.details_text = QTextEdit()
        self.details_text.setReadOnly(True)
        self.details_text.setMaximumHeight(150)
        result_layout.addWidget(self.details_text)
        
        result_group.setLayout(result_layout)
        result_group.setLayout(result_layout)
        right_layout.addWidget(result_group)
        
        # Traversals
        traversal_group = QGroupBox("Tree Traversals")
        traversal_layout = QVBoxLayout()
        
        # Root selector
        root_layout = QHBoxLayout()
        root_layout.addWidget(QLabel("Root Vertex:"))
        self.root_combo = QComboBox()
        self.root_combo.currentIndexChanged.connect(self.update_traversals)
        self.root_combo.setEnabled(False)
        root_layout.addWidget(self.root_combo)
        root_layout.addStretch()
        traversal_layout.addLayout(root_layout)
        
        # Results
        self.traversal_text = QTextEdit()
        self.traversal_text.setReadOnly(True)
        self.traversal_text.setMaximumHeight(150)
        traversal_layout.addWidget(self.traversal_text)
        
        traversal_group.setLayout(traversal_layout)
        right_layout.addWidget(traversal_group)
        
        splitter.addWidget(right_widget)
        splitter.setSizes([400, 600])
        
        layout.addWidget(splitter)
        
        # Set scroll widget
        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)
    
    def set_vertices(self):
        """Set the vertices for the tree."""
        try:
            vertices_text = self.vertices_input.text().strip()
            if not vertices_text:
                self.show_error("Please enter vertex names")
                return
            
            # Parse vertices
            vertices = [v.strip() for v in vertices_text.split(',')]
            vertices = [v for v in vertices if v]  # Remove empty strings
            
            if not vertices:
                self.show_error("Please enter at least one vertex")
                return
            
            # Create new checker
            self.checker = TreeChecker(vertices)
            
            # Update UI
            num_vertices = len(vertices)
            expected_edges = num_vertices - 1
            self.vertex_count_label.setText(f"✓ {num_vertices} vertices set: {', '.join(vertices)}")
            self.vertex_count_label.setStyleSheet("color: #00ff88; font-weight: 600;")
            
            self.edge_info_label.setText(
                f"For {num_vertices} vertices, a tree must have exactly {expected_edges} edge(s).\n"
                f"More edges → cycle exists. Fewer edges → disconnected graph."
            )
            self.edge_info_label.setStyleSheet("color: #00d4ff; padding: 10px; font-weight: 600;")
            
            # Enable edge adding
            self.add_edge_btn.setEnabled(True)
            self.clear_edges_btn.setEnabled(True)
            self.check_tree_btn.setEnabled(True)
            
            # Clear previous edges
            self.edges_list.clear()
            
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
    
    def add_edge(self):
        """Add an edge to the graph."""
        if not self.checker:
            self.show_error("Please set vertices first")
            return
        
        try:
            from_vertex = self.from_input.text().strip()
            to_vertex = self.to_input.text().strip()
            
            if not from_vertex or not to_vertex:
                self.show_error("Please enter both vertices for the edge")
                return
            
            # Add edge
            success, message = self.checker.add_edge(from_vertex, to_vertex)
            
            if success:
                # Add to list display
                edge_text = f"{from_vertex} ↔ {to_vertex}"
                self.edges_list.addItem(edge_text)
                
                # Clear inputs
                self.from_input.clear()
                self.to_input.clear()
                self.from_input.setFocus()
                
                # Update edge count info
                num_vertices = len(self.checker.vertices)
                num_edges = len(self.checker.edges)
                expected = num_vertices - 1
                
                if num_edges == expected:
                    status = f"✓ Perfect! {num_edges}/{expected} edges"
                    color = "#00ff88"
                elif num_edges < expected:
                    status = f"⚠ {num_edges}/{expected} edges (need more)"
                    color = "#ffaa00"
                else:
                    status = f"✗ {num_edges}/{expected} edges (too many - cycle likely)"
                    color = "#ff4444"
                
                self.edge_info_label.setText(
                    f"For {num_vertices} vertices, a tree must have exactly {expected} edge(s).\n"
                    f"Current: {status}"
                )
                self.edge_info_label.setStyleSheet(f"color: {color}; padding: 10px; font-weight: 600;")
            else:
                self.show_error(message)
                
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
    
    def clear_edges(self):
        """Clear all edges."""
        if self.checker:
            # Reset checker with same vertices
            vertices = list(self.checker .vertices)
            self.checker = TreeChecker(vertices)
            self.edges_list.clear()
            
            # Update edge info
            num_vertices = len(vertices)
            expected = num_vertices - 1
            self.edge_info_label.setText(
                f"For {num_vertices} vertices, a tree must have exactly {expected} edge(s).\n"
                f"More edges → cycle exists. Fewer edges → disconnected graph."
            )
            self.edge_info_label.setStyleSheet("color: #00d4ff; padding: 10px; font-weight: 600;")
    
    def check_tree(self):
        """Validate if the graph is a tree."""
        if not self.checker:
            self.show_error("Please set vertices first")
            return
        
        try:
            is_tree, explanation, details = self.checker.is_tree()
            
            # Display main result
            self.result_label.setText(explanation)
            if is_tree:
                self.result_label.setProperty("class", "success")
            else:
                self.result_label.setProperty("class", "error")
            self.result_label.setStyle(self.result_label.style())
            
            # Display detailed results
            details_text = "Detailed Analysis:\n\n"
            details_text += f"📊 Vertices: {details['vertex_count']}\n"
            details_text += f"📊 Edges: {len(details['edge_list'])}\n\n"
            
            details_text += "Property Checks:\n"
            details_text += f"  ✓ Edge Count: {details['edge_message']}\n"
            details_text += f"  ✓ Acyclic: {'Yes - ' + details['cycle_message'] if details['acyclic'] else 'No - ' + details['cycle_message']}\n"
            details_text += f"  ✓ Connected: {'Yes - ' + details['connected_message'] if details['connected'] else 'No - ' + details['connected_message']}\n\n"
            
            if details['edge_list']:
                details_text += "Edge List:\n"
                for v1, v2 in details['edge_list']:
                    details_text += f"  {v1} ↔ {v2}\n"
            
            self.details_text.setPlainText(details_text)
            
            # Update Traversal UI
            self.root_combo.clear()
            self.traversal_text.clear()
            
            if is_tree:
                self.root_combo.setEnabled(True)
                # Add all vertices to combo, sorted
                self.root_combo.addItems(sorted(list(self.checker.vertices)))
                # This will trigger update_traversals via signal
            else:
                self.root_combo.setEnabled(False)
                self.traversal_text.setText("Fix tree issues to see traversals.")
            
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
            
    def update_traversals(self):
        """Update traversal results based on selected root."""
        if not self.checker or not self.root_combo.isEnabled():
            return
            
        root = self.root_combo.currentText()
        if not root:
            return
            
        try:
            results = self.checker.get_traversals(root)
            
            text = f"Rooted at '{root}':\n\n"
            
            # Pre-order
            pre = ", ".join(results['pre_order'])
            text += f"➤ Pre-order: {pre}\n"
            
            # In-order
            in_order = results['in_order']
            if isinstance(in_order, list):
                text += f"➤ In-order:  {', '.join(in_order)}\n"
            else:
                text += f"➤ In-order:  {in_order}\n"
                
            # Post-order
            post = ", ".join(results['post_order'])
            text += f"➤ Post-order: {post}\n"
            
            self.traversal_text.setPlainText(text)
            
        except Exception as e:
            self.traversal_text.setPlainText(f"Error calculating traversals: {str(e)}")

    def show_error(self, message):
        """Show error message."""
        self.result_label.setText(f"❌ {message}")
        self.result_label.setProperty("class", "error")
        self.result_label.setStyle(self.result_label.style())
