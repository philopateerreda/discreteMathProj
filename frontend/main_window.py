"""
Main Window for Discrete Mathematics Application
Tabbed interface containing all three analysis modules.
"""

from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from frontend.relation_widget import RelationWidget
from frontend.logic_widget import LogicWidget
from frontend.tree_widget import TreeWidget


class MainWindow(QMainWindow):
    """Main application window with tabbed interface."""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Discrete Mathematics Toolkit")
        self.setMinimumSize(1000, 800)
        self.resize(1200, 900)
        
        # Center window on screen
        self.center_on_screen()
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        central_widget.setLayout(layout)
        
        # Create tab widget
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        
        # Add tabs
        self.relation_tab = RelationWidget()
        self.logic_tab = LogicWidget()
        self.tree_tab = TreeWidget()
        
        self.tabs.addTab(self.relation_tab, "🔗 Relations")
        self.tabs.addTab(self.logic_tab, "⚡ Logic")
        self.tabs.addTab(self.tree_tab, "🌳 Trees")
        
        layout.addWidget(self.tabs)
        
        # Set status bar
        self.statusBar().showMessage("Ready - Select a module to begin")
        self.statusBar().setStyleSheet("background-color: #252525; color: #00d4ff; padding: 5px;")
    
    def center_on_screen(self):
        """Center the window on the screen."""
        from PyQt5.QtWidgets import QDesktopWidget
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        x = (screen.width() - size.width()) // 2
        y = (screen.height() - size.height()) // 2
        self.move(x, y)
