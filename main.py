"""
نقطة بداية التطبيق
Sales & Inventory Management System
"""

import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

print("🚀 بدء تشغيل نظام إدارة المبيعات والمخازن...")
print("⏳ جاري التحميل...")

def main():
    """الدالة الرئيسية"""
    
    # إنشاء التطبيق
    app = QApplication(sys.argv)
    app.setLayoutDirection(Qt.RightToLeft)
    
    # رسالة ترحيب مؤقتة
    msg = QMessageBox()
    msg.setWindowTitle("نظام إدارة المبيعات والمخازن")
    msg.setText("🎉 مرحباً بك في نظام إدارة المبيعات والمخازن!\n\n"
                "⚠️ النظام قيد التطوير\n\n"
                "الملفات الأساسية تم إنشاؤها بنجاح ✅")
    msg.setIcon(QMessageBox.Information)
    msg.exec()
    
    print("✅ النظام جاهز!")
    
    sys.exit(0)


if __name__ == "__main__":
    main()
