DARK_STYLE = """
QMainWindow, QWidget {
    background-color: #1a1a2e;
    color: #eaeaea;
    font-size: 14px;
}
QPushButton {
    background-color: #0f3460;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 24px;
    min-height: 40px;
}
QPushButton:hover { background-color: #1a4a7a; }
QPushButton#primary { background-color: #e94560; }
QPushButton#success { background-color: #00b894; }
QPushButton#danger { background-color: #d63031; }
QLineEdit, QTextEdit {
    background-color: #0f3460;
    color: white;
    border: 2px solid #1a4a7a;
    border-radius: 8px;
    padding: 10px;
}
QTableWidget {
    background-color: #16213e;
    color: white;
    border-radius: 10px;
}
QHeaderView::section {
    background-color: #0f3460;
    color: #00fff5;
    padding: 12px;
    font-weight: bold;
}
"""

def apply_dark_theme(app):
    app.setStyleSheet(DARK_STYLE)
