<div dir="rtl">

# 🏪 نظام إدارة المبيعات والمخازن الشامل

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![PySide6](https://img.shields.io/badge/PySide6-6.6+-green.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 نظرة عامة

نظام متكامل لإدارة المبيعات والمخازن مبني بلغة Python باستخدام PySide6 وPostgreSQL، يدعم اللغة العربية بالكامل.

## ✨ المميزات

- 🛒 نقطة بيع (POS) سريعة وسهلة
- 📦 إدارة مخزون متعددة المخازن
- 👥 إدارة العملاء والموردين
- 💰 متابعة الديون والحسابات
- 📊 تقارير شاملة وتحليلات
- 📋 إدارة الطلبات
- 🔐 نظام صلاحيات متقدم
- 🎨 واجهة عصرية داكنة

## 🚀 التثبيت

```bash
# استنساخ المستودع
git clone https://github.com/tahaayyoub79/sales-and-inventory.git
cd sales-and-inventory

# إنشاء البيئة الافتراضية
python -m venv venv
source venv/bin/activate  # Linux/Mac
# أو
venv\Scripts\activate  # Windows

# تثبيت المكتبات
pip install -r requirements.txt

# إعداد قاعدة البيانات
createdb -U postgres sales_inventory_db

# نسخ ملف البيئة
cp .env.example .env
# عدّل .env بمعلومات قاعدة البيانات

# تشغيل النظام
python main.py
admin
admin
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2024 Taha Ayyoub

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
