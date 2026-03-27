import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt
from ui.styles import apply_dark_theme
from ui.main_window import MainWindow
from database.connection import init_database, db
from config import APP_CONFIG

print("🚀 تشغيل نظام إدارة المبيعات والمخازن\n")

def main():
    app = QApplication(sys.argv)
    app.setLayoutDirection(Qt.RightToLeft)
    apply_dark_theme(app)
    
    print("📦 تهيئة قاعدة البيانات...")
    if init_database():
        print("✅ قاعدة البيانات جاهزة!\n")
    else:
        QMessageBox.critical(None, "خطأ", "فشل الاتصال بقاعدة البيانات!")
        return
    
    window = MainWindow()
    window.showMaximized()
    
    print(f"✅ النظام جاهز! الإصدار: {APP_CONFIG.app_version}\n")
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
