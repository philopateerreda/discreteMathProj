"""
Professional Modern Dark Mode Stylesheet
High-contrast, large typography, and spacious design for a premium feel.
"""

MODERN_STYLE = """
/* Global Reset & Base Settings */
* {
    outline: none;
}

QMainWindow, QWidget {
    background-color: #121212;
    color: #E0E0E0;
    font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
    font-size: 14px; /* Increased base font size */
}

/* -------------------------------------------------------------------------
   Typography & Labels
   ------------------------------------------------------------------------- */
QLabel {
    color: #B0B0B0;
    font-size: 14px;
    padding: 4px;
    font-weight: 500;
}

QLabel[class="header"] {
    font-size: 28px; /* Much larger header */
    font-weight: 800;
    color: #00E5FF; /* Cyan accent */
    padding: 20px 0px 10px 0px;
    letter-spacing: 0.5px;
}

QLabel[class="subheader"] {
    font-size: 18px;
    font-weight: 700;
    color: #FFFFFF;
    padding: 15px 0px 5px 0px;
    border-bottom: 2px solid #333;
    margin-bottom: 10px;
}

QLabel[class="result"] {
    font-size: 16px;
    font-weight: 600;
    padding: 20px;
    border-radius: 12px;
    background-color: #1E1E1E;
    border: 1px solid #333;
}

QLabel[class="success"] {
    color: #00E676; /* Bright Green */
    background-color: rgba(0, 230, 118, 0.1);
    border: 1px solid rgba(0, 230, 118, 0.3);
}

QLabel[class="error"] {
    color: #FF5252; /* Bright Red */
    background-color: rgba(255, 82, 82, 0.1);
    border: 1px solid rgba(255, 82, 82, 0.3);
}

/* -------------------------------------------------------------------------
   Inputs (LineEdits, TextEdits)
   ------------------------------------------------------------------------- */
QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox {
    background-color: #1E1E1E;
    border: 2px solid #333333;
    border-radius: 10px;
    padding: 12px 16px; /* Larger padding */
    color: #FFFFFF;
    font-size: 16px; /* Larger input text */
    selection-background-color: #00E5FF;
    selection-color: #000000;
}

QLineEdit:hover, QTextEdit:hover {
    border: 2px solid #555555;
    background-color: #252525;
}

QLineEdit:focus, QTextEdit:focus {
    border: 2px solid #00E5FF;
    background-color: #252525;
}

QLineEdit::placeholder {
    color: #666666;
    font-style: italic;
}

/* -------------------------------------------------------------------------
   Buttons
   ------------------------------------------------------------------------- */
QPushButton {
    background-color: #00E5FF; /* Cyan Primary */
    color: #000000;
    border: none;
    border-radius: 10px;
    padding: 14px 28px; /* Larger buttons */
    font-weight: 700;
    font-size: 15px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

QPushButton:hover {
    background-color: #84FFFF;
    margin-top: -2px; /* Subtle lift effect */
    margin-bottom: 2px;
}

QPushButton:pressed {
    background-color: #00B8D4;
    margin-top: 2px;
    margin-bottom: -2px;
}

QPushButton:disabled {
    background-color: #333333;
    color: #777777;
    margin: 0;
}

QPushButton[class="secondary"] {
    background-color: #424242;
    color: #FFFFFF;
}

QPushButton[class="secondary"]:hover {
    background-color: #616161;
}

QPushButton[class="operator"] {
    background-color: #2C2C2C;
    color: #00E5FF;
    font-family: 'Consolas', 'Monaco', monospace;
    font-size: 18px;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px;
    min-width: 45px;
}

QPushButton[class="operator"]:hover {
    background-color: #3E3E3E;
    border: 1px solid #00E5FF;
}

/* -------------------------------------------------------------------------
   Tab Widget
   ------------------------------------------------------------------------- */
QTabWidget::pane {
    border: 1px solid #333;
    background-color: #121212;
    border-radius: 12px;
    top: -1px; 
}

QTabBar::tab {
    background-color: #1E1E1E;
    color: #888888;
    padding: 15px 30px;
    margin-right: 4px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    font-weight: 600;
    font-size: 15px;
    min-width: 140px;
}

QTabBar::tab:hover {
    background-color: #2C2C2C;
    color: #FFFFFF;
}

QTabBar::tab:selected {
    background-color: #121212; /* Blend with body */
    color: #00E5FF;
    border-bottom: 3px solid #00E5FF;
}

/* -------------------------------------------------------------------------
   Group Box
   ------------------------------------------------------------------------- */
QGroupBox {
    border: 1px solid #333333;
    border-radius: 12px;
    margin-top: 24px; /* Space for title */
    padding-top: 24px;
    padding-bottom: 16px;
    padding-left: 16px;
    padding-right: 16px;
    background-color: #181818;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 20px;
    padding: 0 10px;
    background-color: #121212; /* Match parent bg to look floating */
    color: #00E5FF;
    font-weight: 700;
    font-size: 16px;
}

/* -------------------------------------------------------------------------
   Tables & Lists
   ------------------------------------------------------------------------- */
QTableWidget, QListWidget {
    background-color: #1E1E1E;
    border: 1px solid #333;
    border-radius: 10px;
    gridline-color: #333;
    font-size: 15px;
}
    border: none;
    background: #121212;
    width: 14px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background: #424242;
    min-height: 30px;
    border-radius: 7px;
    margin: 2px;
}

QScrollBar::handle:vertical:hover {
    background: #00E5FF;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
"""


def apply_stylesheet(app):
    """Apply the modern dark mode stylesheet to the application."""
    app.setStyleSheet(MODERN_STYLE)
