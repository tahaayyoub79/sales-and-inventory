from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from config import APP_CONFIG

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_CONFIG.app_name)
        self.setMinimumSize(1200, 700)
        self.setLayoutDirection(Qt.RightToLeft)
        
        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # الشريط الجانبي
        sidebar = QFrame()
        sidebar.setFixedWidth(250)
        sidebar.setStyleSheet("background-color: #0f0f23;")
        sidebar_layout = QVBoxLayout(sidebar)
        
        header = QLabel("🏪 نظام المبيعات")
        header.setAlignment(Qt.AlignCenter)
        header.setFont(QFont("Arial", 16, QFont.Bold))
        header.setStyleSheet("background: #e94560; color: white; padding: 20px;")
        sidebar_layout.addWidget(header)
        
        for icon, text in [("📊","لوحة التحكم"),("🛒","نقطة البيع"),("📦","المخزون"),("👥","العملاء")]:
            btn = QPushButton(f"  {icon}  {text}")
            btn.setStyleSheet("text-align: right; padding: 15px;")
            sidebar_layout.addWidget(btn)
        
        sidebar_layout.addStretch()
        layout.addWidget(sidebar)
        
        # المحتوى
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(30, 30, 30, 30)
        
        title = QLabel("🎉 مرحباً بك في نظام إدارة المبيعات")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #00fff5;")
        content_layout.addWidget(title)
        
        info = QLabel("✅ النظام جاهز للعمل!\n📌 الإصدار: 1.0.0")
        info.setStyleSheet("font-size: 16px; padding: 20px;")
        content_layout.addWidget(info)
        content_layout.addStretch()
        
        layout.addWidget(content)
