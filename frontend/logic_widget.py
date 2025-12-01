"""
Logic Checker Widget
PyQt5 interface for checking logical equivalence between expressions.
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QLineEdit, QPushButton, QTextEdit, QGroupBox,
                             QTableWidget, QTableWidgetItem, QSplitter, QScrollArea)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from backend.logic_checker import LogicChecker


class LogicWidget(QWidget):
    """Widget for logical equivalence checking."""
    
    def __init__(self):
        super().__init__()
        self.checker = LogicChecker()
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface."""
        # Main layout with ScrollArea
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Scroll Area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(0) # No border
        scroll.setStyleSheet("background-color: transparent;") # Transparent to match theme
        
        # Content Widget
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)
        layout.setSpacing(25)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Header
        title = QLabel("Logical Equivalence Checker")
        title.setProperty("class", "header")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Instructions
        info_label = QLabel("Supported Operators: ~ (NOT), v (OR), ^ (AND), -> (IMPLIES), <-> (BICONDITIONAL)")
        info_label.setAlignment(Qt.AlignCenter)
        info_label.setStyleSheet("color: #888; font-size: 14px; margin-bottom: 10px;")
        layout.addWidget(info_label)
        
        # Main Content Splitter
        splitter = QSplitter(Qt.Vertical)
        
        # Input Section
        input_widget = QWidget()
        input_layout = QVBoxLayout(input_widget)
        input_layout.setContentsMargins(0, 0, 0, 0)
        input_layout.setSpacing(20)
        
        # Expression 1
        expr1_group = QGroupBox("First Expression")
        expr1_layout = QVBoxLayout()
        self.expr1_input = QLineEdit()
        self.expr1_input.setPlaceholderText("e.g., p -> q")
        self.expr1_input.setMinimumHeight(50)
        expr1_layout.addWidget(self.expr1_input)
        
        # Operators 1
        op_layout1 = QHBoxLayout()
        operators = ['~', 'v', '^', '->', '<->', 'p', 'q', 'r']
        for op in operators:
            btn = QPushButton(op)
            btn.setProperty("class", "operator")
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, o=op: self.insert_operator(self.expr1_input, o))
            op_layout1.addWidget(btn)
        op_layout1.addStretch()
        expr1_layout.addLayout(op_layout1)
        expr1_group.setLayout(expr1_layout)
        input_layout.addWidget(expr1_group)
        
        # Expression 2
        expr2_group = QGroupBox("Second Expression")
        expr2_layout = QVBoxLayout()
        self.expr2_input = QLineEdit()
        self.expr2_input.setPlaceholderText("e.g., ~p v q")
        self.expr2_input.setMinimumHeight(50)
        expr2_layout.addWidget(self.expr2_input)
        
        # Operators 2
        op_layout2 = QHBoxLayout()
        for op in operators:
            btn = QPushButton(op)
            btn.setProperty("class", "operator")
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, o=op: self.insert_operator(self.expr2_input, o))
            op_layout2.addWidget(btn)
        op_layout2.addStretch()
        expr2_layout.addLayout(op_layout2)
        expr2_group.setLayout(expr2_layout)
        input_layout.addWidget(expr2_group)
        
        # Check button
        self.check_btn = QPushButton("CHECK EQUIVALENCE")
        self.check_btn.setCursor(Qt.PointingHandCursor)
        self.check_btn.clicked.connect(self.check_equivalence)
        self.check_btn.setMinimumHeight(60)
        input_layout.addWidget(self.check_btn)
        
        splitter.addWidget(input_widget)
        
        # Results Section
        results_widget = QWidget()
        results_layout = QVBoxLayout(results_widget)
        results_layout.setContentsMargins(0, 20, 0, 0)
        results_layout.setSpacing(15)
        
        self.result_label = QLabel("Enter expressions above to compare")
        self.result_label.setProperty("class", "result")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setWordWrap(True)
        results_layout.addWidget(self.result_label)
        
        # Truth Tables
        tables_layout = QHBoxLayout()
        tables_layout.setSpacing(20)
        
        # Table 1
        t1_container = QWidget()
        t1_layout = QVBoxLayout(t1_container)
        t1_header = QLabel("Truth Table 1")
        t1_header.setProperty("class", "subheader")
        t1_header.setAlignment(Qt.AlignCenter)
        t1_layout.addWidget(t1_header)
        self.table1 = QTableWidget()
        t1_layout.addWidget(self.table1)
        tables_layout.addWidget(t1_container)
        
        # Table 2
        t2_container = QWidget()
        t2_layout = QVBoxLayout(t2_container)
        t2_header = QLabel("Truth Table 2")
        t2_header.setProperty("class", "subheader")
        t2_header.setAlignment(Qt.AlignCenter)
        t2_layout.addWidget(t2_header)
        self.table2 = QTableWidget()
        t2_layout.addWidget(self.table2)
        tables_layout.addWidget(t2_container)
        
        results_layout.addLayout(tables_layout)
        splitter.addWidget(results_widget)
        
        layout.addWidget(splitter)
        
        # Set scroll widget
        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)
    
    def insert_operator(self, line_edit, operator):
        """Insert operator at cursor position."""
        cursor_pos = line_edit.cursorPosition()
        current_text = line_edit.text()
        new_text = current_text[:cursor_pos] + operator + current_text[cursor_pos:]
        line_edit.setText(new_text)
        line_edit.setCursorPosition(cursor_pos + len(operator))
        line_edit.setFocus()
    
    def check_equivalence(self):
        """Check if expressions are logically equivalent."""
        try:
            expr1 = self.expr1_input.text().strip()
            expr2 = self.expr2_input.text().strip()
            
            if not expr1 or not expr2:
                self.show_error("Please enter both expressions")
                return
            
            # Check equivalence
            is_equiv, explanation, table1_data, table2_data = self.checker.check_equivalence(expr1, expr2)
            
            # Display result
            self.result_label.setText(explanation)
            if is_equiv:
                self.result_label.setProperty("class", "success")
            else:
                self.result_label.setProperty("class", "error")
            self.result_label.setStyle(self.result_label.style())
            
            # Display truth tables
            self.display_truth_table(self.table1, table1_data, expr1)
            self.display_truth_table(self.table2, table2_data, expr2)
            
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
    
    def display_truth_table(self, table_widget, table_data, expression):
        """Display truth table in table widget."""
        variables, rows = table_data
        
        if not variables:
            table_widget.clear()
            table_widget.setRowCount(1)
            table_widget.setColumnCount(1)
            table_widget.setHorizontalHeaderLabels(['Result'])
            if rows:
                _, result = rows[0]
                item = QTableWidgetItem('T' if result else 'F')
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(0, 0, item)
            return
        
        # Setup table
        num_vars = len(variables)
        num_rows = len(rows)
        table_widget.clear()
        table_widget.setRowCount(num_rows)
        table_widget.setColumnCount(num_vars + 1)
        
        # Set headers
        headers = variables + ['Result']
        table_widget.setHorizontalHeaderLabels(headers)
        
        # Fill table
        for row_idx, (values_dict, result) in enumerate(rows):
            # Variable columns
            for col_idx, var in enumerate(variables):
                val = values_dict[var]
                item = QTableWidgetItem('T' if val else 'F')
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row_idx, col_idx, item)
            
            # Result column
            result_item = QTableWidgetItem('T' if result else 'F')
            result_item.setTextAlignment(Qt.AlignCenter)
            # Highlight result column
            font = result_item.font()
            font.setBold(True)
            result_item.setFont(font)
            if result:
                result_item.setForeground(Qt.cyan)
            table_widget.setItem(row_idx, num_vars, result_item)
        
        # Adjust column widths
        table_widget.resizeColumnsToContents()
        table_widget.horizontalHeader().setStretchLastSection(True)
        
        # Adjust row heights and table height to fit content
        table_widget.resizeRowsToContents()
        
        # Calculate total height needed
        header_height = table_widget.horizontalHeader().height()
        rows_height = table_widget.verticalHeader().length()
        # Add a small buffer for borders/frame
        total_height = header_height + rows_height + 4
        
        # Set fixed height to prevent internal scrollbars
        # The main page scrollbar will handle overflow
        table_widget.setMinimumHeight(total_height)
        table_widget.setMaximumHeight(total_height)
    
    def show_error(self, message):
        """Show error message."""
        self.result_label.setText(f"❌ {message}")
        self.result_label.setProperty("class", "error")
        self.result_label.setStyle(self.result_label.style())
        self.table1.clear()
        self.table2.clear()
