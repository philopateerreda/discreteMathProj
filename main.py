"""
Discrete Mathematics Toolkit
A professional PyQt5 application for discrete mathematics analysis.

Modules:
- Relation Checker: Verify equivalence relations and properties
- Logic Checker: Check logical equivalence between expressions
- Tree Validator: Validate tree structures

Author: Discrete Mathematics Project
"""

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

# Import frontend components
from frontend.main_window import MainWindow
from frontend.styles import apply_stylesheet


def main():
    """Main application entry point."""
    # Enable High DPI scaling
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName("Discrete Mathematics Toolkit")
    
    # Apply modern dark mode stylesheet
    apply_stylesheet(app)
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Run application
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
